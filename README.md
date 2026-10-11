# paper-laser

some papers for laser detection

单光子 LiDAR 文献知识库：整理中文阅读笔记、可引用书目信息与实验条件对比。英文原题、方法名和专业术语按原文保留。本次阅读依据 **7 篇用户实际上传的正式发表全文**；公开仓库收录 **4 篇许可允许的原始 PDF**，另 3 篇保留来源、阅读笔记和引用，没有以摘要页或下载列表代替全文。

目录年份使用正式卷期年份；Qiao 等论文在 2025 年首次在线发表、归入 2026 年卷期，因此目录为 `2026-...`。笔记中的页码统一从 PDF 文件第一页开始计数；P3DTT PDF 包含出版商封面，正文第一页是 PDF 第 2 页。

## 导航

- [论文方法与实验条件对比](comparison.md)
- [合并 BibTeX](references.bib)
- [来源、版本、文件大小与 SHA-256 清单](source_manifest.json)
- [PDF 校验值](checksums.sha256)
- [检查结果与待核实信息](verification.md)
- [PDF 许可与署名清单](PDF_LICENSES.md)
- [上传说明](UPLOAD.md)

## 论文索引

| 英文原题 | 完整作者 | 年份 | 发表渠道 | 研究方向 | DOI | PDF | 笔记 | 引用 |
|---|---|---:|---|---|---|---|---|---|
| 3D reconstruction of the dynamic scene with high-speed targets for GM-APD LiDAR | Di Liu; Jianfeng Sun; Wei Lu; Sining Li; Xin Zhou | 2023 | Optics & Laser Technology 161, 109114 | Hough 运动分割、末帧补偿、超分辨重建 | [10.1016/j.optlastec.2023.109114](https://doi.org/10.1016/j.optlastec.2023.109114) | [来源（未收录 PDF）](papers/2023-liu-dynamic-gm-apd-reconstruction/source.md) | [notes](papers/2023-liu-dynamic-gm-apd-reconstruction/notes.md) | [BibTeX](papers/2023-liu-dynamic-gm-apd-reconstruction/citation.bib) |
| Dynamic motion-blur suppression and super-resolution localization of UAV targets using single-photon LiDAR under ultra-low SNR | Dongfang Guo; Xin Zhou; Jianfeng Sun; Sheng Chen; Yinbo Zhang; Sining Li; Yanchen Qu | 2026 | Optica 13(3), 491–510 | 5D-MR、运动模糊抑制、UAV 亚像素定位 | [10.1364/OPTICA.581370](https://doi.org/10.1364/OPTICA.581370) | [PDF](papers/2026-guo-uav-motion-blur-super-resolution/paper.pdf) | [notes](papers/2026-guo-uav-motion-blur-super-resolution/notes.md) | [BibTeX](papers/2026-guo-uav-motion-blur-super-resolution/citation.bib) |
| Single-Photon Depth Reconstruction at Low Signal-Background Ratio Based on Four-Dimensional Attention Mechanism | Senlin Feng; Tong Liu; Jianghua Cheng; Bang Cheng; Yahui Cai; Yunwang Zhang | 2026 | Remote Sensing 18(12), 2006 | AMAD-Net、低 SBR 单峰深度重建 | [10.3390/rs18122006](https://doi.org/10.3390/rs18122006) | [PDF](papers/2026-feng-four-dimensional-attention/paper.pdf) | [notes](papers/2026-feng-four-dimensional-attention/notes.md) | [BibTeX](papers/2026-feng-four-dimensional-attention/citation.bib) |
| Instantaneous UAV tracking using single-photon LiDAR via photon-event-driven suppression of temporal-averaging bias | Dongfang Guo; Jianfeng Sun; Xin Zhou; Chen Shen; Sheng Chen; Sining Li; Yanchen Qu | 2026 | Opto-Electronic Technology 2(2), 260013 | P3DTT、瞬时位置校正、三维轨迹跟踪 | [10.29026/oet.2026.260013](https://doi.org/10.29026/oet.2026.260013) | [PDF](papers/2026-guo-instantaneous-uav-tracking/paper.pdf) | [notes](papers/2026-guo-instantaneous-uav-tracking/notes.md) | [BibTeX](papers/2026-guo-instantaneous-uav-tracking/citation.bib) |
| Multi-Temporal Resolution-Guided 3-D Imaging for Array-Based Single-Photon LiDAR | Kai Qiao; Yu Chang; Zefang Xu; Fei Yin; Chang Su; Liyu Liu; Tianye Liu; Chunliang Liu; Jinshou Tian; Xing Wang | 2026 | IEEE Photonics Journal 18(1), 7800108 | 多时间 bin 尺度、FCM 像素分割、阵列远距离成像 | [10.1109/JPHOT.2025.3645783](https://doi.org/10.1109/JPHOT.2025.3645783) | [PDF](papers/2026-qiao-multi-temporal-3d-imaging/paper.pdf) | [notes](papers/2026-qiao-multi-temporal-3d-imaging/notes.md) | [BibTeX](papers/2026-qiao-multi-temporal-3d-imaging/citation.bib) |
| Physics enhanced single-photon imaging based on deep learning | Haoran Shen; Jian Li; Ruiyi Zheng; Lu Cao; Qin Wang | 2026 | Photonics Research 14(9), 4117–4130 | AITV 显式先验、交叉注意力、SWNet | [10.1364/PRJ.601600](https://doi.org/10.1364/PRJ.601600) | [来源（未收录 PDF）](papers/2026-shen-physics-enhanced-imaging/source.md) | [notes](papers/2026-shen-physics-enhanced-imaging/notes.md) | [BibTeX](papers/2026-shen-physics-enhanced-imaging/citation.bib) |
| Single-Photon Imaging in Complex Scenarios via Physics-Informed Deep Neural Networks | Siao Cai; Zhicheng Yu; Shaobing Gao; Zeyu Chen; Yiguang Liu | 2026 | IEEE Transactions on Pattern Analysis and Machine Intelligence 48(5), 5827–5843 | PIDNN、无监督物理拟合、多深度与雾分离 | [10.1109/TPAMI.2026.3654264](https://doi.org/10.1109/TPAMI.2026.3654264) | [来源（未收录 PDF）](papers/2026-cai-physics-informed-complex-scenarios/source.md) | [notes](papers/2026-cai-physics-informed-complex-scenarios/notes.md) | [BibTeX](papers/2026-cai-physics-informed-complex-scenarios/citation.bib) |

## 目录结构

每篇论文使用 `papers/年份-第一作者-简短英文标题/`，包含：

- `paper.pdf`：仅对许可允许公开再分发的论文保存逐字节副本，内容不改动。
- `source.md`：未收录 PDF 时，说明合法全文来源、原因及原始 PDF 页码定位。
- `notes.md`：文献信息、摘要、背景与贡献、方法与公式、实验与关键参数、消融、局限、复现信息、阅读总结。
- `citation.bib`：该论文的 BibTeX；根目录另有合并版本。

根目录 README 提供索引，`comparison.md` 用不同证据类型对照方法。`tools/verify_repository.py` 可重复检查校验值、引用文件、页码范围、BibTeX 核心字段和文档基本语法。

## 阅读与比较约定

1. 原文报告的结果与整理者的归纳／推断分开写；无法确认的信息保留“待核实”或“原文未提供”。
2. 模拟、实际采集、抽帧等效高速、离线重建及作者报告的部署分开记录。信号 PPP 与全部检测 PPP、SBR 与 dB SNR、时间 bin 与距离误差、输出网格与定位精度分开解释。
3. 实验数据和关键结论附 PDF 页码及本地文件链接。`paper.pdf#page=N` 是阅读定位提示；部分 GitHub PDF 预览器可能忽略页码 fragment，可下载 PDF 后定位。
4. 公式使用 GitHub `$...$`、`$$...$$` 数学格式，方法图使用 Mermaid。不同论文的数据集、训练、参考真值、评价指标与系统条件不统一，表格不作跨论文直接排名。
5. 未取得官方代码／原始数据的论文明确记录缺失；本库是阅读知识库，未宣称完成算法复现。

## 文件归属与可见性

用户于 2026-10-11 明确选择公开仓库。本库仅按原始 PDF 与出版商许可确认后收录全文：3 篇采用 CC BY 4.0，5D-MR 采用 Optica OAPA，供非商业学习与再分发。其他 3 篇不公开 PDF。逐篇依据、署名、许可链接和条件见 [PDF_LICENSES.md](PDF_LICENSES.md)。

论文 PDF 保留原作者／出版商权利，**不纳入整理文档的任何开源许可**。OAPA 的非商业限制仅适用于该论文，不扩展到 CC BY 4.0 论文。本次没有添加覆盖论文全文的根目录开源许可证。

原仓库标题和简介已保留，公开整理版本基于原有 `main` 提交历史新增内容。包含全部 7 篇 PDF 的私人本地整理提交未作为公开版本的父提交；仅公开获准全文。远端交付状态见 [验证报告](verification.md)。
