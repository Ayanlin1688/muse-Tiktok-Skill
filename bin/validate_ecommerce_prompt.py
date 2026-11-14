#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Muse v6.2 电商提示词硬检脚本

用途：在交付前对提示词文本做确定性扫描，拦截：
1. 价格与货币符号（$, ￥, 元, 折, cheapest, lowest price...）
2. 尺寸数字与单位（inch, cm, mm, ft, ml, oz, pcs, "...）
3. 夸大/医疗/新广告法极限词（best, #1, guaranteed, cures, 最好, 第一, 治疗...）
4. 抽象 AI 摄影词（cinematic, bokeh, 8k, masterpiece, 电影感...）
5. 美区/抖音中英文混杂串台风险
6. 正向段误用否定词（仅检查 Restrictions 之前的段落）

用法:
  python validate_ecommerce_prompt.py --market us --file prompt.txt
  python validate_ecommerce_prompt.py --market cn --text "..."
"""
import argparse
import re
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8", errors="replace")

PRICE_PATTERNS = [
    r"\$\s*\d+",
    r"￥\s*\d+",
    r"\d+\s*元",
    r"\d+(?:\.\d+)?\s*折",
    r"\b(?:cheapest|lowest price|limited time|flash sale|discount price|only \$)\b",
    r"(?:最低价|全网最低|亏本|原价|秒杀价|限时抢购)",
]

SIZE_UNIT_PATTERNS = [
    r"\b\d+(?:\.\d+)?\s*(?:inch|inches|in|cm|mm|ft|feet|m|ml|oz|fl\.?\s*oz|pcs|pc|pack|packs|g|kg|lb|lbs)\b",
    r"\b\d+(?:\.\d+)?\"",
    r"\d+(?:\.\d+)?\s*(?:厘米|毫米|英寸|英尺|毫升|克|千克|斤|件套|只装|片装)",
]

BANNED_CLAIMS = [
    r"\b(?:best|top\s*1|#1|number\s*one|perfect|guaranteed|forever|miracle|magic|cures|prevents|indestructible|100%)\b",
    r"(?:最好|绝对|全网销冠|国家级|顶级|永久|100%|零甲醛|彻底解决|修复细胞|治疗|防脱发|根治)",
    r"(?:第一名|第一品牌|全网第一|销量第一|行业第一|排行第一)",
]

ABSTRACT_AI_WORDS = [
    r"\b(?:cinematic|bokeh|rim light|studio lighting|8k|4k ultra|masterpiece|stunning|photorealistic|hyperrealistic|unreal engine)\b",
    r"(?:电影感|大片感|完美无瑕|惊艳|单反虚化|商业棚拍)",
]

POSITIVE_NEGATION_WORDS = [
    r"\b(?:no|not|never|without|avoid)\b",
]

# 允许的相机光学参数（非产品尺寸，不视为违规）
CAMERA_PARAM_WHITELIST = [
    r"\b24\s*mm\b", r"\b26\s*mm\b", r"\b28\s*mm\b", r"\b35\s*mm\b", r"\b50\s*mm\b",
    r"\bf\s*/\s*1\.\d+\b", r"\b1\.78\b",
]


def split_positive_and_negative(text: str):
    markers = [
        "【L5",
        "[L5",
        "[Restrictions",
        "Restrictions:",
        "限制清单：",
        "限制清单:",
        "[硬性限制清单",
        "硬性限制清单",
        "Negative Lock",
    ]
    cut = len(text)
    for m in markers:
        idx = text.find(m)
        if idx != -1 and idx < cut:
            cut = idx
    return text[:cut], text[cut:]


def scan(text: str, market: str):
    errors = []
    warnings = []
    pos_part, neg_part = split_positive_and_negative(text)

    # 先把相机光学参数遮掉，避免误判为产品尺寸
    def mask_camera(s):
        out = s
        for wp in CAMERA_PARAM_WHITELIST:
            out = re.sub(wp, "<CAM>", out, flags=re.IGNORECASE)
        return out

    masked_pos = mask_camera(pos_part)

    # 规则只作用于「正向描述段」；末尾限制清单本就该出现这些词
    for label, patterns in [
        ("价格/促销违规", PRICE_PATTERNS),
        ("尺寸/数量数字违规", SIZE_UNIT_PATTERNS),
        ("夸大/医疗/极限词违规", BANNED_CLAIMS),
        ("抽象AI摄影词", ABSTRACT_AI_WORDS),
    ]:
        for pat in patterns:
            for m in re.finditer(pat, masked_pos, flags=re.IGNORECASE):
                errors.append(f"[{label}] 正向段命中 `{m.group(0)}`")

    # 限制清单区只查「带真实数字/金额」的硬违规（避免误伤 "price tags" 这类否定表述）
    hard_price = re.compile(r"(?:\$\s*\d|￥\s*\d|\d+\s*元|\d+(?:\.\d+)?\s*折)")
    hard_size = re.compile(
        r"\b\d+(?:\.\d+)?\s*(?:inch|inches|cm|mm|ft|feet|ml|oz|pcs)\b|\b\d+(?:\.\d+)?\s*(?:厘米|英寸|毫米|毫升)"
    )
    masked_neg = mask_camera(neg_part)
    for pat, name in [(hard_price, "价格"), (hard_size, "尺寸")]:
        for m in pat.finditer(masked_neg):
            errors.append(f"[{name}硬违规] 限制清单区出现具体数字 `{m.group(0)}`")

    if market == "us":
        # 剔除标题占位注释后，检查正文是否残留中文
        body_no_bracket = re.sub(r"\[[^\]]+\]", "", text)
        cn_hits = re.findall(r"[\u4e00-\u9fff]+", body_no_bracket)
        if cn_hits:
            errors.append(f"[美区语种隔离违规] 英文提示词正文含中文: {' / '.join(cn_hits[:5])}")

        # 检查正向段否定词（排除 iPhone / zero color grading 等固定白名单短语前先提示）
        pos_clean = re.sub(
            r"\b(?:zero beauty filter|zero studio rim light|zero artificial sharpening|zero color grading|zero exaggerated|zero numeric)\b",
            "",
            pos_part,
            flags=re.IGNORECASE,
        )
        for pat in POSITIVE_NEGATION_WORDS:
            hits = [m.group(0) for m in re.finditer(pat, pos_clean, flags=re.IGNORECASE)]
            if hits:
                warnings.append(f"[正向段否定词提醒] 正向段出现 `{', '.join(hits[:5])}`，建议尽量转入末尾 Restrictions 区")

        if "iPhone 17 Pro Max" not in text:
            warnings.append("[光学底座缺失] 未检测到 `iPhone 17 Pro Max` 实拍引擎锚点")
        if "Listing" not in text and "listing" not in text:
            warnings.append("[合规声明缺失] 建议补充 TikTok Shop Listing 一致性声明")

    elif market == "cn":
        if "iPhone 17 Pro Max" not in text:
            warnings.append("[光学底座缺失] 未检测到 `iPhone 17 Pro Max` 实拍引擎锚点")
        if not neg_part.strip():
            warnings.append("[限制清单缺失] 未检测到 `[硬性限制清单]` 区")

    return errors, warnings


def main():
    p = argparse.ArgumentParser(description="Muse 电商提示词合规与一致性硬检")
    p.add_argument("--market", choices=["us", "cn"], required=True, help="us=TikTok美区, cn=中国抖音")
    p.add_argument("--file", help="UTF-8 提示词文件路径")
    p.add_argument("--text", help="直接传入提示词文本")
    args = p.parse_args()

    if args.file:
        text = Path(args.file).read_text(encoding="utf-8")
    elif args.text:
        text = args.text
    else:
        text = sys.stdin.read()

    errors, warnings = scan(text, args.market)
    print(f"=== Muse 电商提示词校验 ({args.market.upper()}) ===")
    if errors:
        print(f"拦截错误 ({len(errors)}):")
        for e in errors:
            print(f"  ✗ {e}")
    else:
        print("拦截错误: 0 ✓")

    if warnings:
        print(f"提醒 ({len(warnings)}):")
        for w in warnings:
            print(f"  ! {w}")
    else:
        print("提醒: 0 ✓")

    sys.exit(2 if errors else 0)


if __name__ == "__main__":
    main()
