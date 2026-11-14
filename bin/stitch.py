#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Muse Video Studio · 多段拼接（尺寸校验 + 无损拼）

用法:
  python stitch.py --out <成片.mp4> seg1.mp4 seg2.mp4 [seg3.mp4 ...]

规则:
  - 逐段 ffprobe 读宽/高/编码/像素格式；不一致直接报错并指出哪段不同
  - 一致时用 concat demuxer + -c copy 无损拼接
  - 输出成片时长与分段时长之和
依赖:
  ffmpeg / ffprobe 在 PATH 中。
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8", errors="replace")


def die(msg, code=2):
    print(f"[错误] {msg}", file=sys.stderr)
    sys.exit(code)


def probe(path: Path) -> dict:
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-print_format", "json",
         "-show_streams", "-show_format", str(path)],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        die(f"ffprobe 读不了: {path}\n{r.stderr.strip()}")
    data = json.loads(r.stdout)
    v = next((s for s in data.get("streams", []) if s.get("codec_type") == "video"), None)
    if v is None:
        die(f"没有视频流: {path}")
    return {
        "width": v.get("width"),
        "height": v.get("height"),
        "codec": v.get("codec_name"),
        "pix_fmt": v.get("pix_fmt"),
        "duration": float(data.get("format", {}).get("duration", 0) or 0),
    }


def main():
    p = argparse.ArgumentParser(description="Muse 多段无损拼接")
    p.add_argument("--out", required=True, help="成片路径")
    p.add_argument("segments", nargs="+", help="分段视频，按顺序传")
    args = p.parse_args()

    if shutil.which("ffmpeg") is None or shutil.which("ffprobe") is None:
        die("找不到 ffmpeg / ffprobe，请先安装并加入 PATH")

    segs = [Path(s).expanduser().resolve() for s in args.segments]
    for s in segs:
        if not s.is_file():
            die(f"分段不存在: {s}")

    infos = [probe(s) for s in segs]
    first = infos[0]
    bad = []
    for s, info in zip(segs, infos):
        if (info["width"], info["height"]) != (first["width"], first["height"]):
            bad.append(f"{s.name}: {info['width']}x{info['height']} != {first['width']}x{first['height']}")
        elif info["codec"] != first["codec"]:
            bad.append(f"{s.name}: codec {info['codec']} != {first['codec']}")
        elif info["pix_fmt"] != first["pix_fmt"]:
            bad.append(f"{s.name}: pix_fmt {info['pix_fmt']} != {first['pix_fmt']}")
    if bad:
        die("分段参数不一致，先统一转码再拼：\n  " + "\n  ".join(bad))

    out = Path(args.out).expanduser().resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
        for s in segs:
            f.write("file '%s'\n" % s.as_posix())
        list_path = f.name

    print(f"拼接 {len(segs)} 段 -> {out} "
          f"({first['width']}x{first['height']}, {first['codec']}, {first['pix_fmt']})")
    r = subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
         "-i", list_path, "-c", "copy", str(out)],
        capture_output=True, text=True,
    )
    os.unlink(list_path)
    if r.returncode != 0:
        die(f"ffmpeg 拼接失败\n{r.stderr.strip()}")

    total = probe(out)["duration"]
    print(f"完成：{total:.2f}s -> {out}")
    print(f"分段总时长 {sum(i['duration'] for i in infos):.2f}s")


if __name__ == "__main__":
    main()
