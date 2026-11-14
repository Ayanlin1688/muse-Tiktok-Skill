# 来源与改动说明

本 skill 是个人定制版，原型为 `masonmosen/muse-video-prompt-skill`（MIT License，Copyright (c) 2026 Mason Mosen）。

## v6.2.0-ecommerce-consistency（2026-11-13）：一致性与实拍质感融合版

根据用户提供的「美妆香水（VOYAGE NILLA / QAWAFT）」产品图、真实生成视频（`29e9ef62...mp4`）与两条真机实拍标杆（`7ada9bb1...mp4`、`64fea07f...mp4`）逐帧诊断，并**融合三个 GitHub 开源 Agent Skill 的核心协议**：

### 融合来源
1. **`Emily2040/seedance-2.0`（seedance-characters）** → 吸收「Character Contract 角色契约」与「三层动作分级（持续微动 / 单一受控反应 / 大幅动作默认禁止）」。
2. **`penposs/minimax-h3-video-prompt`** → 吸收「人物与产品一致性锁定必须写可观察特征、不写空泛『保持一致』」与「唯一文字白名单」。
3. **`zhengzhentao86/reverse-video-prompt`** → 吸收「原生手机质感锁（低码率感/轻微软度/不均匀自动曝光）」「0.0 秒音频起声锁」「本地真实感锁」。
4. **本机真实标杆蒸馏** → 提取 Apple iPhone 17 Pro Max bt709 原生色彩、自然自动曝光、轻微手持动态微糊、真实肤质与零碎细发等物理特征。

### 新增与升级内容
1. **重写 `references/ecommerce-universal-engine.md`**：
   - 新增「双锁一致性契约（Character & Product Contract）」：产品 5 项物理不变量 + 唯一文字白名单 + 人物身份/发饰/衣着全程锁定。
   - 新增「三层动作安全分级」：Tier1 微动 / Tier2 单一受控动作 / **Tier3 高危连续拆装默认封杀**（根治穿模与瓶盖丢失）。
   - 新增「真实视频蒸馏光学与色彩模型」：iPhone 17 Pro Max bt709 原生直出、自然过曝、轻微动态微糊。
   - 新增「中美原生实拍场景与语种硬隔离」矩阵。
   - 保留并升级「T1–T5 全类目外观冻结自适应槽位」。
2. **重写 `references/douyin-vs-tiktok-rules.md`**：双轨硬隔离矩阵 + TikTok Shop `-8 分 Mismatch/SNAD` 防扣分红线 + 抖音新广告法红线 + 0–3s 爆款钩子库（H1–H4）。
3. **重写 `references/prompt-template.md`**：美区英文模板 + 抖音中文模板全面重写（含 0.0s 起声锁、三层动作、人物契约、光学底座），22 项硬检清单。
4. **新增 `bin/validate_ecommerce_prompt.py`**：确定性扫描价格/尺寸数字/夸大极限词/抽象 AI 词/中英串台，交付前必跑。
5. **新增案例卡 `cases-2026-11-13-beauty-perfume.md`**：美妆香水逐帧病理复盘。
6. **升级 `SKILL.md` / `personal-defaults.md`** 至 v6.2。

## 历史版本
- **v4.0.0-ecommerce-ultra**：引入 1:1 外观冻结锁、iPhone 17 Pro Max 引擎、双平台规则、22 项硬检。
- **v3.0.0-ecommerce-pro**：全类目电商化（T1–T5 槽位、五大病理根治、双平台合规）。
- **v2.1.0-prompt-only**：职责收窄为「只产提示词」。
- **v2.0.0-personal**：品牌重写与默认项个人化。
