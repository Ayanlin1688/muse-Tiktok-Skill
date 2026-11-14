# 抖音电商 vs TikTok Shop 美区 · 双轨硬隔离与合规红线（v7.0）

> 核心原则：**两个市场物理级硬隔离，绝不混用人设、语言、场景或话术习惯。**

---

## 一、双轨硬隔离矩阵（严禁串台）

| 隔离维度 | TikTok Shop 美区（US Market） | 中国抖音电商（Douyin CN Market） |
|---|---|---|
| **提示词书写语言** | **100% 纯英文**（含动作、光学、对话、限制词，严禁夹杂中文字样） | **100% 纯中文**（仅保留通用设备型号 `Apple iPhone 17 Pro Max` 与色彩标准 `bt709`） |
| **人物与族裔语境** | 美区本地真人 UGC 创作者（或明确要求拉美/西语裔），穿美式日常居家/通勤休闲服 | 中国本土真人穿搭与居家/通勤面貌 |
| **口播语种** | **地道美式英语口语（支持北美各地方言语气）或美式西班牙语（US Spanish）**；严禁中文口播 | **标准普通话或指定中国地方方言（如浙江开化话，标注后期配音提示）**；严禁英文口播 |
| **拍摄环境** | 美式私家车（左舵/安全带/中控咖啡杯）、美式带百叶窗与地毯客厅/梳妆台 | 中国家庭客厅餐桌、阳台自然光、国产/国内常见内饰车厢 |
| **信任基调** | **去广告感的真实生活切片（Slice-of-Life Confession）**：像给闺蜜/同事安利，允许小瑕疵和卡壳 | **痛点直击 + 细节特写实证**：前 3 秒讲清解决什么问题、材质怎么真实 |

---

## 二、TikTok Shop 美区防扣分红线（重点防 -8 分 Mismatch 违规）

> 依据 TikTok Shop US Content Policy & AIGC Visual Guidelines（2026 最新规则）：

1. **尺寸与比例不一致（Product Details Mismatch / Oversized 违规，单次扣 8 分）**：
   - **违规诱因**：视频把小毯子/墙贴树拍得过大，或在脚本/字幕里提及与后台 SKU 不符的尺寸数字。
   - **硬规则**：**提示词与台词里绝对禁止出现任何具体尺寸数字与单位**（`inch, cm, ft, mm, ml, oz, pcs` 全部清零）。改为**人体手掌/常见家居比例锚点**（例如：`held comfortably in one hand`, `draped naturally across a single armchair`）。
   - **强制声明**：每条美区脚本必须附带 Listing 合规声明：`Product proportions, colors, and physical details strictly reflect the linked TikTok Shop listing.`
2. **外观与配件不符（SNAD 货不对板）**：
   - 严禁 AI 擅自改变产品颜色、花纹、瓶盖形状、数量或脑补不存在的挂件。
   - 严格使用**外观冻结锁 + 组件白名单**。
3. **绝对化与误导性效果宣称（Exaggerated Claims）**：
   - 禁止 `100%`, `best`, `guaranteed`, `never fades`, `cures`, `prevents`, `cheapest`, `$xx`。
   - 必须改用**主观个人感受句式**：`"I was honestly surprised how long this vanilla scent stayed on my sweater."`
4. **AIGC 画面禁忌**：
   - 禁止画面内由 AI 自己生成假字幕、价格标签、倒计时贴纸、假评论弹窗。

---

## 三、中国抖音电商防违规红线

1. **新广告法极限词清零**：严禁“第一、最好、最便宜、全网销冠、100%有效、绝对不掉、国家级、顶级、根治、修复细胞”。
2. **禁止价格与虚构优惠**：提示词与口播不写具体价格数字（“9.9”、“原价XX”），不写“限时秒杀/免费送”等易触发价格欺诈判定的词。
3. **材质与功效真实性**：严禁把人造毛毡写成“纯羊毛”、把普通香氛写成“助眠治疗”。

---

## 四、全网爆款 0–3s 黄金开头库（直接套入第 1 节拍）

| 代号 | 爆款开头类型 | TikTok 美区英文话术范例 | 抖音中文话术范例 |
|---|---|---|---|
| **H1** | **动作半途入画（最稳，推荐首选）** | 0.0s 已举起产品刚嗅完或刚捏住边缘：`"Wait—I didn't think this would actually last till evening..."` | 0.0s 手已托着产品/按压纹理：`"刚拿到手我以为很普通，结果上身一试真香。"` |
| **H2** | **反常识质疑开局** | `"Look, I'm super picky about vanilla scents in the car, okay?"` | `"说实话，平时这种贴墙的东西我都怕掉，但这块还真稳。"` |
| **H3** | **细节特写实证** | 镜头略微前倾展示瓶身标签与手部接触纹理：`"See this thick amber glass? Not cheap plastic."` | 手指轻弹产品边缘看回弹：`"你们近看这个针织纹路，厚实得很。"` |
| **H4** | **真实痛点对比** | `"If you hate perfumes that smell like synthetic sugar..."` | `"家里客厅没地儿放东西的，看这一面墙就够了。"` |
