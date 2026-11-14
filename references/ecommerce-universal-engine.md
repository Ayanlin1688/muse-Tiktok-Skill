# 全类目电商一致性与实拍质感写死协议（v7.0 真实素材蒸馏版）

> 本协议从真实手机拍摄的带货视频与逐帧病理复盘中反推、验证而成，适用于全部电商品类。

---

## 一、全类目通用写死底层协议（任何品类 100% 强制执行）

### 协议 1：双锁一致性契约（Character & Product Contract）
**禁止空泛写“保持人物和产品一致”（模型会直接忽略）。必须拆成以下 4 个物理不变量锁定：**

1. **产品结构不变量（Product Invariants）**：
   - 必须从参考图提取 5 项写死：`材质与透光性`（如透明琥珀色玻璃 / 哑光毛毡 / 粗针织棉线）+ `容器/本体几何形状`（如圆柱玻璃瓶配金色半球形瓶盖）+ `颜色分区` + `附属组件白名单` + `占比参照`（相对于手掌/人体比例，**严禁写任何 cm/inch/ml/oz 数字**）。
   - **唯一文字白名单锁**：若产品自带不可回避的标签文字（如瓶身棕色矩形标签上的 `VOYAGE NILLA` 与第二行 `QAWAFT`），必须显式声明：`The rectangular label on the bottle stays facing forward toward the lens, keeping the crisp printed lettering "VOYAGE NILLA" over "QAWAFT" legible and undistorted; do not spin the bottle away from the camera.` 若不需要文字或文字易乱码，则锁定角度避免标签翻转。
2. **人物身份与配饰不变量（Character Contract）**：
   - **面部与五官锚点**：保留参考图真人的雀斑/自然毛孔/眼色/肤色均匀度，**严禁写大笑、惊讶睁大眼、闭眼狂笑**（实测 `gen_perfume` f4/f5 证明夸张表情必导致脸型发福变圆与塑料假牙感）。改写为：`calm, conversational micro-expressions—gentle brow lift, natural blinking, soft half-smile while speaking`。
   - **发型与服饰配饰锚点（防中途消失）**：点名参考图里固定穿戴的物品并声明全程不动。例如：`tortoiseshell claw clip holding her messy blonde updo in place, tiny gold hoop earrings, cream cable-knit cardigan unbuttoned over white ribbed tank top, and burgundy seatbelt across her chest—all stay fixed in position throughout.`
3. **三层动作安全分级（防穿模与产品变形核心铁律）**：
   - **Tier 1（持续微动 · 默认层）**：呼吸起伏、自然眨眼、轻微点头、手机自拍臂的 1cm 轻微晃动、发丝微动。
   - **Tier 2（唯一受控主动作 · 限 1 个）**：手指稳稳托住产品向镜头前倾 5–10 厘米、用食指轻敲/轻触产品表面或盖顶、侧头闻一下袖口。
   - **Tier 3（高危禁止动作 · 默认封杀）**：**严禁在单段 10 秒视频内做“拔开瓶盖 + 喷洒 + 换手 + 盖回盖子”的连续复杂拆装！**（实测证明拔盖旋转必导致瓶盖丢失、手指粘连、瓶身变扁、标签乱码）。确需展示开盖状态时，必须拆成独立一段「已开盖首帧」或直接用稳握展示。
4. **单手/双手稳握分工（Zero Third-Hand & Zero Clipping）**：
   - 规定哪只手托底、哪只手指尖贴在瓶身外侧（写清手指在标签上方/下方/两侧，**绝不遮挡文字标签**，指甲与瓶壁接触处清晰分界）。

---

### 协议 2：真实视频蒸馏光学与色彩模型（Apple iPhone 17 Pro Max 实拍感）
从三条真实标杆视频（`IMG_3319.MOV`、`7ada9b`、`64fea0`）蒸馏出的真实物理特征，**彻底替代**假大空的电影感词：

- **色域与曝光特征（bt709 原生直出）**：
  - 真实手机自动曝光（轻微的不均匀自动曝光，车窗/顶灯处有自然高光溢出，脸部暗侧保留真实阴影与颗粒噪点），**严禁 HDR 过度提亮、严禁商业棚拍打光、严禁磨皮美颜**。
  - **动态微糊（Real Motion Slight Softness）**：手部移动或头部轻晃时允许极轻微的手机快门自然模糊感（slight natural smartphone shutter softness on quick hand tilt），这是真人实拍区别于 AI 逐帧锐化塑料感的第一特征。
- **固定光学底座（英文 · TikTok 美区 / Muse 通用）**：
  ```text
  Shot handheld on an Apple iPhone 17 Pro Max (24mm main camera, 9:16 vertical, bt709 native phone color profile), unedited raw social-media video texture. Deep focus with natural smartphone auto-exposure (window daylight slightly overexposed outside, warm-neutral cabin/indoor shadows with faint sensor grain, zero beauty filter, zero studio rim light, zero artificial sharpening). Subtle single-arm handheld breathing drift and slight natural motion softness when shifting the wrist.
  ```
- **固定光学底座（中文 · 抖音电商通用）**：
  ```text
  使用 Apple iPhone 17 Pro Max 原生相机（24mm 主摄，9:16 竖屏，bt709 手机直出自然色彩），零美颜零滤镜无商业调色。深景深全画面清晰，保留真实手机自动曝光特征（窗外或顶灯高光轻微过曝、面部暗部保留真实肤质纹理与细微底噪，拒绝 AI 过度锐化与塑料磨皮）。单手举机自拍/他拍的自然呼吸晃动与轻微手持动态微糊。
  ```

---

### 协议 3：中美原生实拍场景与语种硬隔离（严禁串台）

| 市场 | 人物与口音锁 | 真实生活场景库（严禁空旷摄影棚） | 0.0s 起声与底噪锁 |
|---|---|---|---|
| **TikTok Shop 美区** | **Native US UGC Creator**（北美本地人设，地道美式口语含卡壳/换气，或明确指定 **US Spanish / 拉美西语**；**严禁出现任何中文或中式播音腔**） | ① **美式车内前排自拍**（安全带、中控台咖啡杯、窗外停车场树影阳光）；② **美式客厅/卧室杂乱梳妆台**（带百叶窗光影、身后架子摆满日常瓶罐/杂物）；③ **美式车库/厨房台面** | 从 `0.0s` 立即开口第一句真实感受（含自然换气声 `"Okay wait—"`, `"Honestly..."`），全程保持低电平环境底噪（车内空调微声/室内空气底噪），停顿处**绝不变成数字静音** |
| **中国抖音电商** | **中国本土真人穿搭与普通话/指定地方方言**（生活化短句、接地气语气；**严禁英文口播混入**） | ① **中国居家客厅/卧室窗边自然光**（实木餐桌、沙发抱枕、日常水杯纸巾杂物）；② **私家车副驾/梳妆台实拍** | 开场 0 秒直接切入动作+真实环境声（撕拉声/玻璃轻碰声）+ 接地气普通话短句（单句 ≤10 字），全程自然环境底噪不断 |

---

### 协议 4：T1–T5 全类目外观冻结自适应槽位

无论用户传入什么品类（美妆香水、家居纺织、3C 车载、服饰鞋包、日用百货），按以下 5 档自动套入防变形语法：

| 档位 | 适用类目 | 必须锁死的外观与交互规则 |
|---|---|---|
| **T1 微型/精巧件** | 口红、眼影、耳机、饰品、挂饰片 | 单手拇指+食指捏外缘；禁止双手叠抓同一小件；薄片件加“刚体不融化锁” |
| **T2 瓶罐/手持美妆与日化** | **香水、精华液、水杯、防晒、吹风机** | **单手五指稳握瓶身中下段（绝不遮挡正面标签）**；**单段 10s 内禁止拔盖喷洒旋转**；正面标签始终朝镜头 |
| **T3 柔软/织物/折叠件** | **针织玫瑰毯、四件套、毛衣、收纳袋** | **展开比例参照家居物体（床沿/沙发靠背），绝不写尺寸数字**；禁止边缘花朵/流苏数量变化；手部指尖落点贴合织物起伏 |
| **T4 墙贴/悬挂/长条件** | **毛毡圣诞树、拖把、落地灯、晾衣架** | 本体先行固定于墙面/地面；**单手操作单一局部配件**；全貌留白构图锁 |
| **T5 车载/家电/桌面固定件** | **车载水杯架、空气炸锅、咖啡机、显示器** | **产品本体 100% 固定卡紧在底座/出风口/台面上**，只演示手部放入水杯/按单颗按键的物理反馈 |

---

## 二、全类目爆款前 3 秒黄金钩子矩阵（0–3s 硬注入）

1. **H1 动作半途入画（Action Mid-Way）**：0.0s 时手已经稳稳举着产品或刚完成核心动作（如刚喷完凑近手腕轻嗅一口后抬眼看镜头说话），绝不从空手挥手说“Hey guys”开始。
2. **H2 阻力与真实验证（Tactile Proof）**：用单指轻弹/轻按/轻揉产品材质边缘（如毛毡硬挺不塌、玫瑰花球饱满回弹、玻璃厚实反光），用物理反馈证明品质。
3. **H3 反常识痛点直击（Anti-Hype Confessional）**：口播一上来用自嘲/怀疑口吻切入（如 `"I genuinely thought this was just TikTok hype until I smelled it in my car..."`）。
4. **H4 对比参照入画（Real-Context Contrast）**：产品与真实日常物品（车内咖啡杯、原装礼盒、旧工具）同框出现，一眼看清用途与真实比例。

---

## 三、严禁改变与严禁出现的红线（Zero-Violation Firewall）

1. **严禁数字与尺寸单位**：禁止 `cm`、`inch`、`"`、`ft`、`mm`、`ml`、`oz`、`32PCS`、`59.06`、`39"`（防 TikTok Shop 判 `Product Details Mismatch` 扣 8 分）。
2. **严禁价格与虚假促销**：禁止 `$`、`元`、`折`、`off`、`cheapest`、`lowest price`、`limited time`。
3. **严禁夸大与医疗违禁词**：禁止 `best`、`#1`、`perfect`、`guaranteed`、`forever`、`magic`、`cures`、`zero formaldehyde`、`100%`、`绝对`、`最好`、`第一`。
4. **严禁新增视觉文字/字幕**：限制清单写明禁止 AI 自行生成屏幕悬浮字幕、价签、角标、促销贴纸（产品本体自带且参考图可见的物理标签文字除外）。
5. **严禁正反向语意冲突**：正向段只写要发生的物理画面事实（不写 `no third hand` 这种正向否定词，所有禁止项统一放在末尾 `Restrictions / Negative Lock` 区）。
