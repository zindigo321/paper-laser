# Markdown 显示质量检查与修复报告

检查日期：2026-10-11（UTC）。仓库：`zindigo321/paper-laser`。

已完成原有 15 个 Markdown 文件的源码检查和 GitHub **Preview 阅读页面**检查，并修复 7 篇笔记中确认的公式显示问题。修复后的 178 个数学表达式已通过本地解析和逐项静态预览；仓库校验脚本通过，4 份原始 PDF 字节未变。

**GitHub 修复后桌面复查已完成。** 用户通过 GitHub Desktop 发布修复分支，首轮提交为 `85d2617bf20afaad5457431dbed0fa99b667b5cd`，补充提交为 `9fb721106c2e6f834a436174bcb1d410d897550a`。本轮以补充提交的实际 Preview 为准：7 篇修改笔记的全部 177 个公式成功渲染，未见数学错误框或正文意外暴露命令；20 个表格列数一致，7 个 Mermaid 的节点文字和连线与基线一致。报告的该版本 Preview 中 13 个表格亦正常。

Cai L62 连乘条件的字面小于号改为等价的 `\lt` 后，GitHub 的括号错误消失，连乘下限、上下标和各项实际可见。两种写法本地严格解析的数学 MathML 相同；未改动数学含义。此前其余页面的 GitHub 临时错误在本轮访问／一次重载后恢复，未据此判为链接失效。

GitHub 窄屏阅读、PDF 网页预览／页码跳转仍为**未验证**；Liu、Cai、Shen 三篇未取得原 PDF 的原文公式核对仍为**待核实**。连接器创建 PR 返回 `403 Resource not accessible by integration`，PR 尚未创建；继续由用户通过 GitHub Desktop 创建。此报告记录本轮检查的固定提交，后续报告记录更新不能替代新版本网页验证。

## 检查基线与范围

- 检查前分支：`main`。
- 检查前提交：`c707a84ce8aa52b78b8e57b36eb91aeba4fc1657`，`docs: update upload verification`。
- 检查前已有修改：无；新克隆工作区的 `git status --porcelain` 为空。
- 本地修复分支：`fix/markdown-display-quality-20261011`，从上述提交创建。
- 检查根目录全部 5 个 Markdown 文件，以及 `papers/` 下全部 7 个 `notes.md`、3 个 `source.md`。新增的本报告不计入原始 15 个文件。
- GitHub 检查使用 Preview 页面及实际数学渲染节点、错误信息、表格单元格和 Mermaid iframe；没有把 Raw 页面或 Code 视图中的合法 LaTeX 判为错误。

GitHub 页面访问记录中的 `main` 在检查时对应上述基线提交。下表列出实际打开的全部 Markdown 阅读页面。

| 文件路径 | GitHub 阅读页面 | 检查结果与修改情况 |
|---|---|---|
| [README.md](README.md) | [Preview](https://github.com/zindigo321/paper-laser/blob/main/README.md) | 中文、标题、列表、目录及表格未发现确认的显示问题；未修改 |
| [comparison.md](comparison.md) | [Preview](https://github.com/zindigo321/paper-laser/blob/main/comparison.md) | 4 个表格列数一致；唯一行内公式实际渲染；未修改 |
| [PDF_LICENSES.md](PDF_LICENSES.md) | [Preview](https://github.com/zindigo321/paper-laser/blob/main/PDF_LICENSES.md) | 中文、授权说明、链接和表格结构未发现确认的显示问题；未修改 |
| [UPLOAD.md](UPLOAD.md) | [Preview](https://github.com/zindigo321/paper-laser/blob/main/UPLOAD.md) | 正文及明确标注的代码示例未发现确认的显示问题；未修改 |
| [verification.md](verification.md) | [Preview](https://github.com/zindigo321/paper-laser/blob/main/verification.md) | 历史验证记录正常排版；保留原记录及其历史计数，未修改 |
| [papers/2023-liu-dynamic-gm-apd-reconstruction/notes.md](papers/2023-liu-dynamic-gm-apd-reconstruction/notes.md) | [Preview](https://github.com/zindigo321/paper-laser/blob/main/papers/2023-liu-dynamic-gm-apd-reconstruction/notes.md) | 已修复公式格式；原 PDF 不在仓库，本次未取得 |
| [papers/2023-liu-dynamic-gm-apd-reconstruction/source.md](papers/2023-liu-dynamic-gm-apd-reconstruction/source.md) | [Preview](https://github.com/zindigo321/paper-laser/blob/main/papers/2023-liu-dynamic-gm-apd-reconstruction/source.md) | 10 个页码锚点存在；第 3 页锚点点击可定位；未修改 |
| [papers/2026-cai-physics-informed-complex-scenarios/notes.md](papers/2026-cai-physics-informed-complex-scenarios/notes.md) | [Preview](https://github.com/zindigo321/paper-laser/blob/main/papers/2026-cai-physics-informed-complex-scenarios/notes.md) | 已修复公式格式；原 PDF 不在仓库，本次未取得 |
| [papers/2026-cai-physics-informed-complex-scenarios/source.md](papers/2026-cai-physics-informed-complex-scenarios/source.md) | [Preview](https://github.com/zindigo321/paper-laser/blob/main/papers/2026-cai-physics-informed-complex-scenarios/source.md) | 17 个页码锚点存在；第 3 页锚点点击可定位；未修改 |
| [papers/2026-feng-four-dimensional-attention/notes.md](papers/2026-feng-four-dimensional-attention/notes.md) | [Preview](https://github.com/zindigo321/paper-laser/blob/main/papers/2026-feng-four-dimensional-attention/notes.md) | 已修复公式格式；相关原 PDF 页已核对 |
| [papers/2026-guo-instantaneous-uav-tracking/notes.md](papers/2026-guo-instantaneous-uav-tracking/notes.md) | [Preview](https://github.com/zindigo321/paper-laser/blob/main/papers/2026-guo-instantaneous-uav-tracking/notes.md) | 已修复公式格式；相关原 PDF 页已核对 |
| [papers/2026-guo-uav-motion-blur-super-resolution/notes.md](papers/2026-guo-uav-motion-blur-super-resolution/notes.md) | [Preview](https://github.com/zindigo321/paper-laser/blob/main/papers/2026-guo-uav-motion-blur-super-resolution/notes.md) | 已修复公式格式；相关原 PDF 页已核对 |
| [papers/2026-qiao-multi-temporal-3d-imaging/notes.md](papers/2026-qiao-multi-temporal-3d-imaging/notes.md) | [Preview](https://github.com/zindigo321/paper-laser/blob/main/papers/2026-qiao-multi-temporal-3d-imaging/notes.md) | 已修复公式格式；保留 ToF 换算为“整理者的单位说明” |
| [papers/2026-shen-physics-enhanced-imaging/notes.md](papers/2026-shen-physics-enhanced-imaging/notes.md) | [Preview](https://github.com/zindigo321/paper-laser/blob/main/papers/2026-shen-physics-enhanced-imaging/notes.md) | 已修复公式格式；原 PDF 不在仓库，本次未取得 |

## GitHub Desktop 发布后的网页复查

本轮复查对象：`fix/markdown-display-quality-20261011` 的 `9fb721106c2e6f834a436174bcb1d410d897550a`；桌面视口 1363×936。逐页打开实际 Preview，等待每个数学组件出现 MathML 或错误框后判定，检查全部组件、正文裸露命令、表格和 Mermaid SVG。表中的链接为实际访问的固定提交页面。

| 修改页面 | 本轮实际结果 | 状态 |
|---|---|---|
| [papers/2026-cai-physics-informed-complex-scenarios/notes.md](https://github.com/zindigo321/paper-laser/blob/9fb721106c2e6f834a436174bcb1d410d897550a/papers/2026-cai-physics-informed-complex-scenarios/notes.md) | 全部 35 个公式生成 MathML，无公式错误或正文裸露命令；4 表列数一致；Mermaid 5 节点／4 连线；L62 连乘式补充修复实际通过 | 已修复并验证（GitHub 桌面） |
| [papers/2026-guo-instantaneous-uav-tracking/notes.md](https://github.com/zindigo321/paper-laser/blob/9fb721106c2e6f834a436174bcb1d410d897550a/papers/2026-guo-instantaneous-uav-tracking/notes.md) | 全部 29 个公式生成 MathML，无公式错误或正文裸露命令；3 表列数一致；Mermaid 5 节点／4 连线 | 已修复并验证（GitHub 桌面） |
| [papers/2026-guo-uav-motion-blur-super-resolution/notes.md](https://github.com/zindigo321/paper-laser/blob/9fb721106c2e6f834a436174bcb1d410d897550a/papers/2026-guo-uav-motion-blur-super-resolution/notes.md) | 全部 30 个公式生成 MathML，无公式错误或正文裸露命令；1 表列数一致；Mermaid 5 节点／4 连线 | 已修复并验证（GitHub 桌面） |
| [papers/2026-qiao-multi-temporal-3d-imaging/notes.md](https://github.com/zindigo321/paper-laser/blob/9fb721106c2e6f834a436174bcb1d410d897550a/papers/2026-qiao-multi-temporal-3d-imaging/notes.md) | 全部 14 个公式生成 MathML，无公式错误或正文裸露命令；4 表列数一致；Mermaid 8 节点／8 连线 | 已修复并验证（GitHub 桌面） |
| [papers/2026-shen-physics-enhanced-imaging/notes.md](https://github.com/zindigo321/paper-laser/blob/9fb721106c2e6f834a436174bcb1d410d897550a/papers/2026-shen-physics-enhanced-imaging/notes.md) | 全部 31 个公式生成 MathML，无公式错误或正文裸露命令；3 表列数一致；Mermaid 5 节点／5 连线 | 已修复并验证（GitHub 桌面） |
| [papers/2023-liu-dynamic-gm-apd-reconstruction/notes.md](https://github.com/zindigo321/paper-laser/blob/9fb721106c2e6f834a436174bcb1d410d897550a/papers/2023-liu-dynamic-gm-apd-reconstruction/notes.md) | 全部 19 个公式生成 MathML，无公式错误或正文裸露命令；3 表列数一致；Mermaid 9 节点／9 连线 | 已修复并验证（GitHub 桌面） |
| [papers/2026-feng-four-dimensional-attention/notes.md](https://github.com/zindigo321/paper-laser/blob/9fb721106c2e6f834a436174bcb1d410d897550a/papers/2026-feng-four-dimensional-attention/notes.md) | 全部 19 个公式生成 MathML，无公式错误或正文裸露命令；2 表列数一致；Mermaid 5 节点／4 连线 | 已修复并验证（GitHub 桌面） |
| [DISPLAY_QUALITY_REPORT.md](https://github.com/zindigo321/paper-laser/blob/9fb721106c2e6f834a436174bcb1d410d897550a/DISPLAY_QUALITY_REPORT.md) | 该检查版本的 13 表列数一致，正文、标题和代码示例正常排版；本次随后更新复查记录 | 已修复并验证（该版本 GitHub 桌面） |

本轮实际读取 177 个数学组件，全部成功，无数学错误。另一个 `comparison.md` 行内公式未修改，已在基线网页验证；因此不能把本轮 177 个组件写成在该新提交重新检查了 178 个组件。全部 178 项的本地严格解析和可视复查记录继续保留。

首轮发布的 `85d2617` 中 Liu／Feng 的 38 项成功，Cai 的 35 项中 34 项成功、1 项报错；随后补充修复 Cai L62 的小于号。首轮和本轮的记录、错误截图、修复截图分开保存，便于追溯。临时错误页不作为文件损坏或内部链接失效的证据。

用户 Windows 的 `python tools/verify_repository.py` 返回 `ok: true`、零错误；唯一警告是未安装 `pypdf`，该次 PDF 总页数按原始清单检查，全部 PDF SHA-256 已校验。本检查环境包含 PDF 页数解析，补充修复后实际运行脚本，零错误、零警告。单纯 LF／CRLF 转换提示未作为乱码或检查失败的证据。

## 确认问题与修复清单

下列行号均基于检查前提交；本次笔记修改未增删行，因此修复后对应行号不变。每组标题给出完整文件路径，表格中的每条问题均归属于该文件。“已修复并验证（GitHub 桌面）”仅指该固定提交的桌面阅读页面实际通过；不包含窄屏或未取得原 PDF 的原文核对。未完成项目单独保持未验证或待核实。

验证方式缩写：G＝修复前 GitHub Preview 的实际显示／渲染错误；W＝发布后 GitHub 桌面 Preview 的实际 MathML／截图复查；L＝修复后 KaTeX 解析和逐项静态预览；D＝修复前后源码归一化比较；P＝可访问原 PDF 核对。W 不包含窄屏验证。

### papers/2023-liu-dynamic-gm-apd-reconstruction/notes.md

| 位置／所在标题 | 问题现象 | 原因 | 修复方式 | 验证方式 | 状态 |
|---|---|---|---|---|---|
| L38–45，首次触发观测模型 | 指数函数旁出现额外感叹号，乘积与积分微分旁出现逗号 | 普通数学段先经 Markdown 处理，标点转义 `\!`、`\,` 被消耗 | 两个独立公式改用 `math` 围栏，完整保留公式源码 | G、W、L、D；P 未完成 | 已修复并验证（GitHub 桌面） |
| L47，变量定义 | 5 个行内表达式连同美元定界符作为普通文字显示 | 中文标点紧接行内公式开头，未被 GitHub 识别 | 开头补空格，保留原变量与定义 | G、W、L、D | 已修复并验证（GitHub 桌面） |
| L57，分阶段运动估计和数据分离 | 两个 bin 表达式下标被破坏并暴露源码 | 同一段中的下划线参与 Markdown 强调解析 | 两个行内公式使用 GitHub 支持的美元加反引号定界形式 | G、W、L、D；P 未完成 | 已修复并验证（GitHub 桌面） |

### papers/2026-feng-four-dimensional-attention/notes.md

| 位置／所在标题 | 问题现象 | 原因 | 修复方式 | 验证方式 | 状态 |
|---|---|---|---|---|---|
| L42–46，时间分类与连续估计 | 求和项中时间 bin 与概率之间出现逗号 | `\,` 被 Markdown 当作标点转义处理 | 改用 `math` 围栏，保留概率、求和、距离换算各项 | G、W、L、D、P（PDF pp.5–6；整理符号说明保留） | 已修复并验证（GitHub 桌面） |
| L48、L62，变量定义 | 共 7 个行内变量或表达式暴露源码 | 中文标点与开头定界符相邻 | 补开头空格 | G、W、L、D | 已修复并验证（GitHub 桌面） |
| L57–60，训练目标 | NLTV 权重公式报宏不允许，且指数旁出现感叹号 | 当前 GitHub 渲染器拒绝 `\operatorname`；Markdown 消耗 `\!` | MSE 改用同名字的直立字体命令；整个公式改用 `math` 围栏 | G、W、L、D、P（PDF pp.11–12） | 已修复并验证（GitHub 桌面） |

### papers/2026-guo-instantaneous-uav-tracking/notes.md

| 位置／所在标题 | 问题现象 | 原因 | 修复方式 | 验证方式 | 状态 |
|---|---|---|---|---|---|
| L33、48、58、68、113，方法／参数／局限 | 共 6 个行内表达式暴露源码，含表格阵列维度 | 开头定界符与中文标点相邻 | 补开头空格；内点集使用保护定界形式 | G、W、L、D；相关变量参照 PDF pp.9–11 | 已修复并验证（GitHub 桌面） |
| L44–46，阶段 I | 指示函数显示成带感叹号的表达式，容易被误读为阶乘 | `\!` 被 Markdown 消耗 | 改用 `math` 围栏，保留计数、绝对值、下标和阈值 | G、W、L、D、P（PDF p.9） | 已修复并验证（GitHub 桌面） |
| L50，阶段 II | 候选集合的花括号消失 | Markdown 消耗括号的反斜杠转义 | 行内公式使用保护定界形式，恢复集合括号 | G、W、L、D、P（PDF p.10） | 已修复并验证（GitHub 桌面） |
| L62，阶段 III | std 置信界公式报宏不允许 | 当前 GitHub 渲染器拒绝 `\operatorname` | std 改用同名字的直立字体命令，不改加号、参数或系数 | G、W、L、D、P（PDF p.11） | 已修复并验证（GitHub 桌面） |

### papers/2026-guo-uav-motion-blur-super-resolution/notes.md

| 位置／所在标题 | 问题现象 | 原因 | 修复方式 | 验证方式 | 状态 |
|---|---|---|---|---|---|
| L35–37，光子模型与 SNR | 对数函数后出现感叹号 | `\!` 被 Markdown 消耗 | 改用 `math` 围栏，保留信号／背景分数和对数底数 | G、W、L、D、P（PDF p.2，Eq.4） | 已修复并验证（GitHub 桌面） |
| L39、49、66、68、74、104，定义／参数／局限 | 共 15 个行内表达式暴露源码，含表格维度 | 中文标点与开头定界符相邻 | 补开头空格 | G、W、L、D | 已修复并验证（GitHub 桌面） |
| L68，终像素内位移 | 两个星号上标被强调解析干扰，位移式暴露源码 | 同一段中的星号参与 Markdown 解析 | 两个行内公式使用保护定界形式，保留时间星号与两个速度方向 | G、W、L、D、P（PDF p.7，Eqs.24–25） | 已修复并验证（GitHub 桌面） |

### papers/2026-qiao-multi-temporal-3d-imaging/notes.md

| 位置／所在标题 | 问题现象 | 原因 | 修复方式 | 验证方式 | 状态 |
|---|---|---|---|---|---|
| L39、60，多尺度直方图／FCM 定义 | 共 4 个行内表达式暴露源码 | 中文标点与开头定界符相邻 | 补开头空格 | G、W、L、D | 已修复并验证（GitHub 桌面） |
| L41，ToF 单位说明 | 光速与 ToF 之间出现逗号，影响乘积阅读 | `\,` 被 Markdown 消耗 | 使用保护定界形式，保留完整换算及“整理者的单位说明”标注 | G、W、L、D、P（PDF p.3，Eqs.3–4 的 bin／时间定义；并非逐字原文公式） | 已修复并验证（GitHub 桌面） |

### papers/2026-shen-physics-enhanced-imaging/notes.md

| 位置／所在标题 | 问题现象 | 原因 | 修复方式 | 验证方式 | 状态 |
|---|---|---|---|---|---|
| L37、60、69，Poisson／注意力／训练目标 | 3 个独立公式因 4 处函数宏被拒绝而报错 | 当前 GitHub 渲染器拒绝 `\operatorname` | Poisson、Attention、softmax、TV 改用同名字的直立字体命令 | G、W、L、D；P 未完成 | 已修复并验证（GitHub 桌面） |
| L40、53、63、78–80，定义／实验条件 | 共 14 个行内表达式暴露源码，含数据体与阵列维度 | 中文标点与开头定界符相邻 | 补开头空格，保留扫描网格与硬件阵列的区别 | G、W、L、D | 已修复并验证（GitHub 桌面） |

### papers/2026-cai-physics-informed-complex-scenarios/notes.md

| 位置／所在标题 | 问题现象 | 原因 | 修复方式 | 验证方式 | 状态 |
|---|---|---|---|---|---|
| L35–38，每场景拟合 | 星号上标被破坏，实际渲染报 `Missing open brace for superscript` | 多个星号参与 Markdown 强调解析 | 改用 `math` 围栏，保留优化变量和两个星号结果 | G、W、L、D；P 未完成 | 已修复并验证（GitHub 桌面） |
| L53–56，透过率与表面表示 | 积分变量前出现逗号 | `\,` 被 Markdown 消耗 | 改用 `math` 围栏，保留积分范围、平方和分母 | G、W、L、D；P 未完成 | 已修复并验证（GitHub 桌面） |
| L62–64，表面透过率 | 发布后的连乘式仍报 `Extra open brace or missing close brace` 并暴露源码 | 字面 `l<k` 在 GitHub 触发解析异常；本地括号平衡且解析成功 | 保留 `math` 围栏，把 `<` 改成 `\lt`；完整保留连乘条件和所有项 | G 确认原错误；W、L、D 通过；P 未完成 | 已修复并验证（GitHub 桌面） |
| L45、80，测量模型／显式 TV | 2 个独立公式因 3 处函数宏被拒绝而报错 | 当前 GitHub 渲染器拒绝 `\operatorname` | Poisson 和两个 TV 改用同名字的直立字体命令 | G、W、L、D；P 未完成 | 已修复并验证（GitHub 桌面） |
| L40、49、58、83、97–98、132–133，定义／实验表格 | 共 14 个行内表达式暴露源码，含室内和长距离扫描维度 | 中文标点与开头定界符相邻 | 补开头空格，保留数据、单位和证据页码 | G、W、L、D | 已修复并验证（GitHub 桌面） |

### tools/verify_repository.py

| 位置／所在功能 | 问题现象 | 原因 | 修复方式 | 验证方式 | 状态 |
|---|---|---|---|---|---|
| Markdown 围栏与数学块检查（修复前 L87 起附近） | `math` 围栏按普通代码跳过，不能计数或检查其数学括号 | 原脚本只收集双美元独立公式 | 增加 9 行，收集并检查 `math` 围栏；原有检查继续运行 | 实际运行脚本；28 个独立公式均计入；零错误、零警告 | 已修复并验证（本地脚本） |

合计：65 处行内公式开头补空格；7 个行内表达式使用保护定界形式；9 个独立数学块改为 `math` 围栏；9 处函数宏改为同名字的直立字体命令；补充修复 1 处小于号的等价写法。问题项之间有重叠，不将这些数字相加当作独立公式数量。

所用行内保护定界形式及 `math` 围栏在 [GitHub 官方数学表达式文档](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)中有说明。该文档支持语法选择，但不能替代修改页面的实际复查。

## 文字、表格、图示与链接结果

- 原有 15 个文件均能严格按 UTF-8 解码；未发现替换字符、异常控制字符、零宽字符或 BOM。结合上下文检查后，未确认中文乱码、缺字、标题粘连、错误代码块、异常列表缩进、PDF 提取错序／重复、意外显示的换行转义或 JSON 双重转义。没有进行全局反斜杠删除。
- 原有 26 个表格的源码列数和 GitHub DOM 单元格列数一致；未发现未转义竖线导致串列。表格中的公式识别问题按上表修复。宽表允许横向滚动；没有删减实验数据或移动数据到错误列。
- 原有 7 个 Mermaid 在 GitHub 桌面页面均实际生成 SVG，无 `.error-text`。节点文字、分支和连线与源码核对：Liu 9 节点／9 连线，Cai 5／4，Feng 5／4，P3DTT 5／4，5D-MR 5／4，Qiao 8／8，Shen 5／5。修复前后 7 个 Mermaid 源码逐字相同。未确认需要修改的流程或节点截断。
- 原有 Markdown 无静态图片嵌入；因此没有可供判定的缺失嵌入图片。PDF 内部图像能在本地原 PDF 中查看；未改动 PDF 图像。
- 原有 307 个内部链接路径和 211 个 PDF 页码／来源页码引用通过结构检查；页码范围按 4 份 PDF 的实际页数及 3 份来源说明核对。三份 `source.md` 的全部 41 个页码锚点在 GitHub DOM 中存在，各自第 3 页锚点实际点击后可见。未发现本机绝对路径链接。
- `source.md` 是未再分发 PDF 的来源与页码说明，不是原 PDF 全文。锚点存在不等于已核实对应原 PDF 内容。
- GitHub 的 Qiao PDF 预览器已打开，但当前显示空白画布；未据此判定 PDF 文件或链接损坏。原 PDF 可在本地读取，**GitHub PDF 可视预览与 `#page=` 跳转未验证**。

## 外部链接检查

所有原有 19 个不同外部 URL 均纳入检查。未确认外部死链接；不能把访问限制或当前网络／工具失败写成链接错误。

| 链接组 | 本次访问结果 | 判定 |
|---|---|---|
| GitHub 仓库 | 实际网页可访问 | 基线仓库可访问 |
| 历史提交 `d4b6e9bab84e63e47a58c4eb26972160d1781fb4` | 本地完整提交历史中存在 | 对象存在；独立历史提交网页未验证 |
| CC BY 4.0、GitHub Desktop 下载、Optica 版权政策 | 可取得官方页面正文 | 本次可访问 |
| 7 个 DOI 地址 | 当前检索服务无法访问 DOI 重定向 | 网络／工具可达性未验证；DOI 未改动 |
| Liu 的 ScienceDirect 页面 | HTTP 403 Forbidden | 访问受限，不能判为失效；未取得原 PDF |
| Shen 的 Optica PRJ 页面 | 重定向后停在等待页面 | 未取得全文，原因未充分确认 |
| Cai、Qiao 的 IEEE 页面 | JavaScript／机器人验证提示 | 当前访问受限，未绕过验证 |
| Guo 5D-MR 的 Optica 页面 | 重定向后的正文内容不可确认 | 待核实 |
| Feng 的 MDPI、Guo P3DTT 的 OET 页面 | 当前检索返回 Internal Error | 原因未明确，不能判为死链接 |

## 原文内容与 PDF 完整性

以下 PDF 检查前后 SHA-256 完全一致，文件大小、页数及 Git blob 也未改变。没有新增 PDF，也没有修改原 PDF 或其授权文件。

| PDF 路径 | 字节数／页数 | 检查前后相同的 SHA-256 |
|---|---|---|
| `papers/2026-feng-four-dimensional-attention/paper.pdf` | 9,955,541／20 | `86b6bc50d98479e8a23664bf1f1d2defc3fa63d41f8e070ba2e7846826310809` |
| `papers/2026-guo-instantaneous-uav-tracking/paper.pdf` | 27,955,232／28 | `14921928fde7111bd22c80c83a3b11a21488f29c81cef85fdcfd25c1709c43aa` |
| `papers/2026-guo-uav-motion-blur-super-resolution/paper.pdf` | 10,501,050／20 | `3a2f8a7f3625fe21d8dd2a7560a176cb1725f5fb65e721609a5062ce599db457` |
| `papers/2026-qiao-multi-temporal-3d-imaging/paper.pdf` | 1,820,587／8 | `1294af228194599a609310ba70dbc5068cd0a0849cfe5de1fc63c6591c5c1fd4` |

原 PDF 核对限于本次格式修改所涉及的公式和必要上下文：Feng PDF pp.5–6、11–12；P3DTT pp.9–11；5D-MR pp.2–3、6–7；Qiao p.3。核对了相关符号、正负号、上下标、括号、变量含义及页码。整理表达继续保持其整理说明，不声称逐字复制原文。

Liu、Shen、Cai 的原始 PDF 不在公开仓库，官方页面本次未提供可访问全文。其格式修复保留原有表达式，未推测新的公式内容；原文核对状态为 **待核实**。

7 篇笔记修复前后比较：只归一化新增空格、数学围栏／保护定界形式、函数字体命令，以及 Cai 唯一一处 `<`／`\lt` 的等价写法后，文本完全相同。原英文题名、作者姓名、数据、单位、DOI、引用、公式出处及“原文结论／整理者归纳／推断”的区别均保留。原有 BibTeX、清单、校验值、授权说明和历史验证文件未改动。论文中原已标注的数值或单位不一致未擅自修正。

## 修复后复查与验证边界

| 验证层次 | 实际完成的内容 | 结果／限制 |
|---|---|---|
| 源码 | 全部原有 15 个 Markdown；UTF-8、代码围栏、数学定界符、普通正文裸露命令、表格、内部链接和 Mermaid 源码 | 通过；合法数学源码、BibTeX 和标注代码示例保留 |
| 仓库脚本 | 修复前后实际运行 `python tools/verify_repository.py` | 原始语料均为 15 文档、307 内部链接、211 页码引用、26 表格、28 独立数学块、7 Mermaid；零错误、零警告 |
| 本地数学解析 | KaTeX 0.19.0，严格解析全部 178 项（150 行内＋28 独立） | 全部成功；KaTeX 与 GitHub MathJax 不同 |
| 本地可视复查 | 全部 178 项公式逐项静态渲染；7 篇笔记分别生成 1000 px 和 390 px 宽的离线静态预览 | 数学符号可见；窄版长公式／表格在打印引擎中可能溢出，不能据此宣称网页横向滚动已验证 |
| 本地交互预览 | 提供包含原有 15 个文件的 HTML，可切换桌面与 390 px 内容宽度 | 已生成；本会话浏览器不允许打开本地文件，交互操作及本地 Mermaid JavaScript 渲染未验证 |
| GitHub 修复前 | 实际打开全部 15 个 Preview 页面；检查公式错误、26 表格、7 Mermaid 及来源锚点 | 已确认上列问题；桌面视口 1363×936 |
| GitHub 修复后 | 在 `9fb7211` 重新打开全部 7 篇修改笔记与报告；177 个笔记公式、20 个笔记表格及 7 个 Mermaid 通过，报告该版本 13 表通过 | **桌面验证通过**；窄屏、PDF 网页预览／跳转未验证 |
| GitHub 窄屏 | 当前浏览器不提供视口调整，尝试浏览器缩放未改变视口尺寸 | **未验证** |
| GitHub PDF 预览和页码跳转 | 打开 Qiao 的 PDF 阅读页，预览出现空白画布 | **未验证**；本地 PDF 和页码范围检查通过 |

新增本报告后，最终仓库脚本实际检查 16 个 Markdown、321 个内部链接、211 个页码引用、39 个表格、28 个独立数学块和 7 个 Mermaid，零错误、零警告；完整输出随交付包提供。原有 `verification.md` 是历史记录，没有把它的旧计数改写为本次结果。

## 修改文件与交付

修改：上述 7 个 `notes.md`、`tools/verify_repository.py`。新增：本报告 `DISPLAY_QUALITY_REPORT.md`。其余仓库文件保持不变。

交付包包含补丁、本报告、完整修改文件、GitHub 基线截图及渲染记录、全部公式的本地可视复查图和本地 HTML 预览。证据文件在交付包的 `evidence/` 中，未将临时预览依赖、原始 PDF 或凭据加入仓库。

每张 GitHub 截图保留文件路径的页面上下文；`*-before-desktop.jpg` 为基线页面错误证据，不能作为修复后验证截图。本地复查图明确标为本地渲染。结构化记录提供文件路径、公式原行号、实际渲染错误和逐项公式清单，便于定位。

远端操作状态：用户通过 GitHub Desktop 普通推送专用修复分支，首轮提交 `85d2617bf20afaad5457431dbed0fa99b667b5cd`，补充提交 `9fb721106c2e6f834a436174bcb1d410d897550a`；两次推送的文件与已检查修复文件一致。当前 `main` 为 `bb1af895c9f09ab96c7696abfbead4f67570c23d`，在原基线之后只新增 README 英文复数修正。该修改不属于修复分支改动，PR 使用共同基线比较，合并时保留它；未覆盖无关修改。原有提交及父链保留，没有强制推送或合并。

通过 GitHub 连接器创建草稿 PR 的请求返回 `403 Resource not accessible by integration`；不是补丁或公式校验失败。PR 尚未创建，需要用户通过 GitHub Desktop 的 Preview Pull Request／Create Pull Request 创建。本轮最终报告包只需替换本报告一个文件，笔记公式已在上述补充提交实际验证，无新增论文内容修改。

最终报告包包含本报告、报告更新补丁、PR 标题与正文、8 个页面的实际渲染记录、7 个 Mermaid 节点／连线比较、PDF 完整性记录、实际截图及校验输出。不含原 PDF、Git 元数据或凭据。初次修复包和两文件补充包保留为历史交付。

验收仍未完成的项目：GitHub 窄屏阅读、PDF 网页预览／页码跳转、三篇未取得全文的原文公式核对，以及上述受限外部链接的实际可达性。状态保持未验证或待核实。PR 的创建结果及随后报告记录更新的网页验证，以最终交付中的链接和提交 SHA 为准，不提前宣称完成。
