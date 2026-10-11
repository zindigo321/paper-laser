# 核对与交付状态

整理及公开许可核对日期：2026-10-11。全部 7 篇笔记依据用户实际上传的正式期刊全文整理；未把摘要页、下载列表或来源说明当成全文。[来源清单](source_manifest.json)

## 公开范围与本地检查

- 用户已明确选择公开仓库。公开版收录 4 份 PDF：3 份 CC BY 4.0，5D-MR 按 Optica OAPA 用于非商业学习与再分发；许可及署名见 [PDF_LICENSES.md](PDF_LICENSES.md)。
- 4 份公开 PDF 共 50,232,410 bytes，与上传原文件的 SHA-256 一致，内容未修改；PDF 按二进制保存。
- Liu 2023、Shen SWNet、Cai PIDNN 不公开原始 PDF；其 notes、citation 和 source 说明均保留，页码引用沿用实际上传文件。
- [检查脚本](tools/verify_repository.py) 验证公开范围、PDF 文件头／哈希／大小／页数、内部文件与页码锚点、BibTeX 字段、公式定界符、表格列数及代码 fence。
- 检查通过：15 个 Markdown 文档、306 个内部文件链接、211 个 PDF 页码引用／来源定位、26 张表格、28 个展示公式块、7 个 Mermaid 图；4 份 PDF 的文件头、大小、SHA-256 和页数均一致。静态结构检查不能代替 GitHub 上的数学公式、Mermaid 和 PDF 预览验证。
- 未在仓库文件或提交内容中写入访问令牌。

## 外部来源

7 个 DOI、作者和发表信息已与实际 PDF 核对。Optica 官方版权与再使用页面可访问并确认 OAPA 非商业再分发条件；CC BY 4.0 官方许可页面可访问。各论文的在线全文页面可能受到出版商验证码、403 或 429 限制，不能把访问限制误判为 DOI 错误。非公开 PDF 的 source.md 只提供获取说明，不代表可下载全文。

## 需要补充或向作者核实

- 5D-MR：摘要与结论的角度误差 degree/pixel、1 km 像素覆盖大小、Eq.27 单位、Table 7 起止帧／Frame Span、尺寸误差评估口径。
- AMAD-Net：Table 10 分组与正文描述不一致；完整训练代码、权重、真实系统外场验证未提供。
- P3DTT：摘要 0.43 m 与 Table 4 的 0.4375 m、KF 改善比例、角分辨率小数位、383.82/383.92 m/s、某拟合预测的 5633.30 ns 算术；完整三维真值与同步／时延细节。
- Qiao：摘要“超过 50 fps”与正文“最高 50 fps”、4 km 的几何分辨率描述、FFDNet 与分支完整配置、端到端运行时间。
- Shen：AITV 的实际投影／求解细节；实测稠密深度真值、完整代码／权重与测量数据。
- PIDNN：表中深度／强度 RMSE 的明确单位／归一化口径、平均迭代时间统计含义、官方代码与测量数据入口。
- 各论文上传全文中未提供的官方代码／数据链接已分别注明；“未在全文提供”不等于断言互联网不存在。

上述问题均在 [逐篇笔记](README.md) 保留 PDF 页码。该知识库没有完成算法重现，也没有新增实验数据。

## GitHub 状态

- 目标：[zindigo321/paper-laser](https://github.com/zindigo321/paper-laser)，`main`，保持公开。
- 已核对远端 main 仍是原始提交 `12559b2945883785a203b3472ecae03f9233cfdb`。公开版直接在原始历史上新增，保留原 README 标题与简介；含全部 PDF 的私人本地整理提交不进入公开历史。
- 当前连接创建 PDF blob 和 Markdown 文件均返回 HTTP 403 `Resource not accessible by integration`；GitHub App 安装列表为空。当前连接没有成功写入本仓库。
- 写入尝试后重新读取远端 main，仍为原始提交；远端新增文件数为 0。远端上传／推送和在线渲染验证尚未执行，待连接具备仓库写入授权后继续。

## 文件清单

- 7 个论文目录：7 份 notes.md、7 份 citation.bib、4 份 paper.pdf、3 份 source.md，共 21 个文件。
- 根目录：README.md、comparison.md、references.bib、source_manifest.json、checksums.sha256、verification.md、UPLOAD.md、PDF_LICENSES.md、.gitattributes，共 9 个文件。
- tools/verify_repository.py：1 个文件。
- 合计 31 个仓库文件。公开版压缩包不含 .git、私人 PDF、辅助分析目录或凭据。
