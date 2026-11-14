# 5L 提示词装配结构 · 24 项交付闸门

> 本文件是提示词装配车间。所有电商视频提示词按 **L1→L5 五层** 自上而下装配，每层只解决一类问题，层与层之间不重叠。
> 正向段只写「会发生什么」，禁止项全部集中在 L5，避免语义打架。

---

## 一、5L 五层结构总览

| 层 | 名称 | 解决什么 | 缺了会怎样 |
|---|---|---|---|
| **L1** | 帧基 Frame Base | 画幅、时长、原生色彩基底 | 画幅错、色调假、时长被压缩 |
| **L2** | 主体锁 Subject Lock | 产品不变量 + 人物契约 | 产品变形、人物变脸、配件消失 |
| **L3** | 场域 Set Field | 环境、光源、静态杂物 | 背景被 AI 清空、光位不真实 |
| **L4** | 演进 Beat Flow | 0–10 秒三段动作 + 镜头 + 声音 | 动作僵、穿模、无钩子 |
| **L5** | 闸门 Gate | 限制清单 + 合规声明 | 违规词、乱码文字、平台扣分 |

---

## 二、中文装配模板（抖音 / 中文提示词直用）

```text
【L1 帧基】9:16 竖屏，约 10 秒。Apple iPhone 17 Pro Max 主摄原生直出，bt709 手机色彩，深景深全画面清晰，保留自然自动曝光：窗外日光轻微过曝、室内暗部带细微传感器颗粒，单手举机有轻微呼吸晃动与手腕移动时的动态微糊。

【L2 主体锁 · 产品】全片仅此一件。物理不变量：{材质与透光性}、{几何形状与比例}、{颜色分区}、{部件白名单}、{相对手掌的占比}。{产品自带标识} 全程正面朝向镜头、静止不变形。

【L2 主体锁 · 人物】{年龄性别外貌}、{发型 + 固定发饰}、{固定耳饰}、{上衣下装纹理}、{穿戴物}，以上全程保持原位。神态只做自然松弛的日常微表情，保留真实毛孔与零碎细发。

【L3 场域】{真实家庭/车内场景}，{主光源 + 辅光源及其冷暖关系}，周围有 {4–6 件静止日常杂物}，全程不动。

【L4 演进】
  0–3 秒（钩子）：动作已在进行中——{具体的持握或操作动作}。从 0.0 秒起有真实环境底噪，人物自然开口说第一句大白话（≤10 字）："{个人体验开场白}"
  3–7 秒（实证）：只做一个克制的验证动作——{单一动作}。自然接下一句："{卖点感受}"
  7–10 秒（收束）：{顺手放下的生活化动作}，在动作中间自然结束，不做摆拍或推销手势。

【L5 闸门】
一致性声明：产品比例、颜色、结构、材质严格对应后台商品详情页。
限制清单：不要第三只手、不要多余手指、不要手指遮挡或穿过产品、不要改变产品颜色或结构、不要产品文字乱码、不要夸张表情或磨皮脸、不要单反虚化、不要自动生成字幕或价签、不要出现任何数字尺寸或价格。
```

---

## 三、英文装配模板（TikTok 美区直用）

```text
[L1 Frame Base] Vertical 9:16, ~10s. Shot handheld on an Apple iPhone 17 Pro Max main wide camera, native bt709 color profile, deep focus with natural phone auto-exposure (bright window light clips slightly, indoor shadows carry faint sensor grain), subtle single-arm drift and slight motion softness on wrist movement.

[L2 Subject Lock · Product] Exactly one unit. Physical invariants held for the whole clip: {material and translucency}, {geometry and proportions}, {color zones}, {component whitelist}, {size relative to one hand}. {Product label} faces the camera lens the entire time, upright and legible.

[L2 Subject Lock · Person] {Age, look}, {hair with the same fixed clip}, {fixed earrings}, {top and bottom with fabric texture}, {worn accessory}, all holding their position throughout. Calm conversational micro-expressions only, with real pores and fine flyaway hair.

[L3 Set Field] {Authentic US car / home setting}, {key light plus fill light and their color temperature relationship}, plus {4–6 static everyday props} that stay still the whole clip.

[L4 Beat Flow]
  0–3s (Hook): Action already underway — {specific hold or interaction}. Continuous low room tone from 0.0 seconds. She speaks casually to camera in natural American English after a real breath: "{short hook line}"
  3–7s (Proof): One restrained verification action only — {single action}. She continues smoothly: "{short proof line}"
  7–10s (Landing): {casual put-down gesture} and the clip ends mid-gesture, without a posed smile or call to action.

[L5 Gate]
Listing note: Proportions, color, closures and materials strictly reflect the linked TikTok Shop listing.
Restrictions: extra hands, third hand, mutated or clipped fingers, fingers covering or passing through the product, product morphing or color change, distorted label text, exaggerated or frozen facial expressions, waxy smoothed skin, studio lighting, bokeh, cinematic grading, generated captions or price tags, numeric size labels.
```

---

## 四、三层变体（按视频形态选一层套用）

### 变体 A：第一人称 POV 生活流
- 在 L1 之后立刻插入强约束，**单独成行**：
  `全程严格第一人称：镜头就是{男友/朋友}的眼睛，本人不入镜，只允许手或前臂偶尔出现在画面边缘。`
- 约束必须写成强约束。弱约束（"尽量不出现"）会被忽略，实测中肩膀大面积入镜。
- L4 的三个节拍改为「手部动作 + 环境反应」，不写人脸。

### 变体 B：口播 talking-head
- L2 人物层额外写：`正对镜头、视线看镜头；非自拍，画面中不出现相机或手机。`
- L4 台词注明语气与口型：`（声音与画面同步，口型与台词对齐，无文字叠加）`
- 单句 ≤12 字；说话时去掉大幅动作，否则口型必崩。

### 变体 C：多段长片（总时长 >10 秒）
- 拆成多条独立提示词，**每条只覆盖自己那一段的 0–10 秒**。
- 每条第一行固定声明：
  `本段为 {N} 秒视频的第 {K} 段（{X}–{Y} 秒），延续同一人物、场景、光线与质感，人物服装发型面容严格一致。`
- L2 主体锁整段**逐字复制**，一个字都不改。
- L5 闸门每条都要重写，不写"同上"。
- 交付附一张拆段表（段号 / 覆盖秒数 / 镜头数 / 本段任务）。

---

## 五、24 项交付闸门（逐项打钩，缺一项不交）

### A 组 · 帧基（L1）
1. 首行有画幅 + 时长
2. 写明 iPhone 17 Pro Max 原生直出与 bt709
3. 写明深景深与自然自动曝光特征
4. 写明手持轻微晃动与动态微糊
5. 没有出现 cinematic / bokeh / 8k / 电影感

### B 组 · 产品锁（L2）
6. 五项物理不变量全部写全
7. 部件白名单逐一点名，没有 "各种配件" 这类概括词
8. 产品自带标识写清朝向，或明确排除主图促销大字
9. 全片只有一件产品的声明
10. 产品大小用人体或家居比例参照，无任何数字尺寸

### C 组 · 人物锁（L2）
11. 发饰、耳饰、衣着、穿戴物逐项点名并声明不动
12. 神态限定为自然微表情，禁夸张表情
13. 保留真实毛孔与零碎细发

### D 组 · 场域（L3）
14. 场景对应目标市场（美区美式 / 抖音中式）
15. 写明主辅光源与冷暖关系
16. 列出 4–6 件静止杂物
17. 声明杂物全程不动

### E 组 · 演进（L4）
18. 0–3 秒动作已在进行中
19. 每段最多一个主要动作
20. 手部接触点 ≤2，单手操作小件
21. 台词词数合规（英文 ≤25 词 / 中文 ≤35 字），单句短促
22. 结尾在动作中间自然结束

### F 组 · 闸门（L5）
23. 价格、尺寸数字、夸大词、医疗功效词全部为零
24. 美区带 Listing 一致性声明；正文无跨市场语言混用

> 机械项交 `bin/validate_ecommerce_prompt.py` 跑一遍，零错误再交付。

---

## 六、现象 → 改法速查

| 你看到的现象 | 改哪一层 | 具体改法 |
|---|---|---|
| 产品形状或花纹变了 | L2 产品锁 | 把物理不变量补到能画出来的粒度；加刚体声明 |
| 产品标签乱码或被转走 | L2 产品锁 | 写死标签朝向与"静止可读" |
| 人物中途换脸 | L2 人物锁 | 人物段整段复制；多段片逐字一致 |
| 配饰（抓夹/耳环）中途消失 | L2 人物锁 | 逐项点名并声明"全程保持原位" |
| 表情夸张、脸发胖、塑料牙 | L2 人物锁 | 限定为自然微表情；把夸张表情写进 L5 |
| 出现第三只手 / 手指粘连 | L4 演进 | 手部接触点降到 ≤2；单手操作；明确哪只手做什么 |
| 产品部件丢失（如瓶盖） | L4 演进 | 拆掉高危连续动作，改成单一静止展示 |
| 动作中间出现半透明残影 | L4 演进 | 每段只留一个运动主体 |
| 背景被清得干干净净 | L3 场域 | 补 4–6 件静止杂物声明 |
| 画面色彩发灰发假 | L1 帧基 | 补 bt709 与自然过曝描述 |
| 画面过度锐利、像渲染 | L1 帧基 | 补"轻微动态微糊" |
| 单条被压成 10 秒 | 结构 | 拆成多段，单条不写长轴 |
| 出现 AI 自造字幕或价签 | L5 闸门 | 限制清单点名禁止 |
