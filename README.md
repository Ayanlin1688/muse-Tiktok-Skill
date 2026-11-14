# Muse 提示词工厂 · 个人定制版

**只产提示词，不管生成。** 把需求变成可直接粘贴进 Muse 内置视频（Muse Video）的提示词，生成、拼接、验片由你自己的工具完成。

基于 [masonmosen/muse-video-prompt-skill](https://github.com/masonmosen/muse-video-prompt-skill)（MIT）改写，改动见 [NOTICE.md](NOTICE.md)。

## 它做什么 / 不做什么

| 做 | 不做 |
|---|---|
| 把需求写成六段式提示词 | 生成视频 |
| 超 10 秒拆成多条 | 拼接成片 |
| 14 项自检 | 抽帧验片 |
| 四档对白写法 | 操作你的工具 |
| 按失败现象改提示词 | 承诺锁脸/保证效果 |

## 每次交付长这样

1. **一句话说明**：画幅 / 时长 / 语言 / 有无口播
2. **提示词正文**：代码块，可直接全选复制
3. **参数摘要表**：画幅、时长、参考图张数与用途、对白语言
4. **风险提示**：2–4 条，只写影响这条提示词的

## 我的默认项

| 项 | 默认 |
|---|---|
| 画幅 | 9:16 竖屏 |
| 提示词语言 | 中文；美区投放切英文 |
| 对白 | 标准普通话；可选美式英语 / 美式西班牙语 / 浙江开化话 |
| 时间轴 | 只写 0–10 秒，超时拆段 |
| 沟通 | 简体中文 |

完整清单见 `references/personal-defaults.md`。

## 核心文件

```
muse-video-prompt-skill/
├── SKILL.md                      # 入口：四步流程 + 默认项 + 纪律
├── CONSTITUTION.md               # 六条设计原则
├── NOTICE.md                     # 上游来源与改动说明
├── LICENSE                       # MIT
├── README.md
├── references/
│   ├── prompt-template.md        # ★核心：六段式 + 14 项自检 + 交付格式 + 失败改法
│   ├── personal-defaults.md      # 我的默认项全表
│   ├── dialogue.md               # 四档对白写法
│   ├── model-notes.md            # 能力边界如何影响写法
│   ├── consistency.md            # 人物一致性写法
│   ├── integration.md            # 与上下游的衔接
│   └── cases/                    # 提示词案例（写法参考）
├── bin/                          # 可选脚本（你的工具已覆盖可忽略）
└── scripts/install.ps1           # 同步到 DSH skills 目录
```

## 用法

新对话直接说需求即可：

- 「写一条 Muse 提示词：雨天便利店，POV，10 秒，9:16」
- 「用 muse-video-prompt-skill 把这句改成能用的提示词：……」
- 「这条人物跨段换脸了，帮我改多段提示词」
- 「美区带货，抽真空袋 15 秒，英文提示词」→ 会自动拆成 2 条

## 安装

已装到 `%USERPROFILE%\.dsh\skills\muse-video-prompt-skill\`。
工作区源码 `D:\Skill大全\muse-video-prompt-skill-我的定制版\`，改完跑 `scripts\install.ps1` 同步。

## 许可

MIT，保留上游版权声明（见 `LICENSE` 与 `NOTICE.md`）。
