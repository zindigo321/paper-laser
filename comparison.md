# 单光子 LiDAR 论文对比

本表依据实际上传的 7 份全文。数值属于各论文自己的数据、系统、参考真值与评价协议；**不按不同实验条件下的误差直接排名**。所有页码为 PDF 文件页码；P3DTT 封面算第 1 页。

## 问题、方法与证据范围

| 论文／笔记 | 要解决的问题 | 方法主线 | 是否训练／优化 | 主要证据 | 主要限制 |
|---|---|---|---|---|---|
| [Liu 2023](papers/2023-liu-dynamic-gm-apd-reconstruction/notes.md) | 多脉冲累计中的高速运动模糊 | 分阶段 Hough → 事件分割 → 末帧补偿 → 参数估计与超分辨率 | 物理模型与统计处理，不需训练数据 | 300 m/s 仿真；真实行人采集后抽帧形成等效高速 | 近匀速直线；弱／晚进入目标可能漏检；形变未校正 |
| [Guo 2026：5D-MR](papers/2026-guo-uav-motion-blur-super-resolution/notes.md) | 超低 SNR 的亚像素 UAV 定位 | 局部窗口与峰统计 → 两阶段 RANSAC+DBSCAN → 驻留／重叠时间 → 终点亚像素定位 | 无可学习权重，但有阈值／聚类参数 | 1 km 仿真；1.8 km 实际 UAV | 需要跨像素运动，不适合悬停；单位和部分表格算术待核实 |
| [Feng 2026：AMAD-Net](papers/2026-feng-four-dimensional-attention/notes.md) | 极低 SBR 的单峰深度恢复 | 小波门控 → 四维注意力 → pixel denoising → CE+NLTV | 有标签监督训练 | NYUv2 模拟训练，Middlebury 光子测试 | 单峰假设；缺少独立远距离实测验证 |
| [Guo 2026：P3DTT](papers/2026-guo-instantaneous-uav-tracking/notes.md) | 光子累计的时间平均偏差与机动跟踪 | 时空一致性 → RANSAC-iTLS 末端 ToF → 像素回溯 → 创新量自适应状态估计 | 模型驱动迭代拟合和跟踪 | 高速仿真；2.5 km 实际 UAV；作者报告 FPGA/RK3588 架构 | 光子预算与相干性边界；全三维真值／完整同步与延时细节不足 |
| [Qiao 2026](papers/2026-qiao-multi-temporal-3d-imaging/notes.md) | 不同像素的回波可信度／展宽不一致 | 1–32 ns 多尺度 → 强度约束 FCM → 分支算法匹配 → FFDNet | 无监督像素聚类，另用去噪网络；非端到端运动网络 | 4／10 km 面阵实际采集；10 km 风机离线视频 | 多时间尺度指 ToF bin；50 fps 不等于运算实时吞吐 |
| [Shen 2026](papers/2026-shen-physics-enhanced-imaging/notes.md) | 数据驱动网络的结构损失与泛化 | AITV 先验+时间分支 → cross-attention → SWNet | 监督训练；AITV 分支含迭代预处理 | 模拟量化；公开实测与室内 TCSPC 定性 | 高分辨率推理 45 s，优化约 16 s；真实数据缺少稠密真值 |
| [Cai 2026：PIDNN](papers/2026-cai-physics-informed-complex-scenarios/notes.md) | 低 SBR、光斑 multiple returns、多层与雾散射 | 每场景网络表示+Poisson forward model；SDF/体渲染；表面–雾双分支 | 每场景无监督优化；雾分支用模拟预训练初始化 | 模拟、室内、公开 21.6／45 km 数据、多层与雾箱 | 迭代体素优化慢；低通量和介质模型仍有假设 |

方法证据分别见 [Liu pp.2–5](papers/2023-liu-dynamic-gm-apd-reconstruction/source.md#pdf-page-2)、[5D-MR pp.4–7](papers/2026-guo-uav-motion-blur-super-resolution/paper.pdf#page=4)、[AMAD-Net pp.5–12](papers/2026-feng-four-dimensional-attention/paper.pdf#page=5)、[P3DTT pp.8–11](papers/2026-guo-instantaneous-uav-tracking/paper.pdf#page=8)、[Qiao pp.3–5](papers/2026-qiao-multi-temporal-3d-imaging/paper.pdf#page=3)、[Shen pp.3–6](papers/2026-shen-physics-enhanced-imaging/source.md#pdf-page-3)、[PIDNN pp.4–7](papers/2026-cai-physics-informed-complex-scenarios/source.md#pdf-page-4)。

## 探测器、距离、运动与光子条件

| 条件 | 探测器／空间规模 | 距离与速度 | SNR／SBR | 光子数及定义 | 证据 |
|---|---|---|---|---|---|
| Liu 仿真 | 64×64 GM-APD 模型 | 约 1 km，300 m/s | 目标有效像素 SBR≈0.1 | 未给统一 PPP | [p.5](papers/2023-liu-dynamic-gm-apd-reconstruction/source.md#pdf-page-5) |
| Liu 实采后等效处理 | 64×64 GM-APD | 100 m；实际约 1–1.3 m/s，抽帧后等效 100–130 m/s | SBR≈5.86 | 未给统一 PPP | [pp.7–9](papers/2023-liu-dynamic-gm-apd-reconstruction/source.md#pdf-page-7) |
| 5D-MR 仿真 | 64×64 Gm-APD 模型 | 约 1 km；径向 7 m/s，横向的 pixel/m 换算有原文差异 | 最低测试 −9.03 dB | 平均信号 0.5343 photons/pixel | [pp.8–13](papers/2026-guo-uav-motion-blur-super-resolution/paper.pdf#page=8) |
| 5D-MR 外场 | 64×64 Gm-APD，1064 nm | 1.8 km；设置约 12／5 m/s（保留原文方向称谓） | −8.97 dB | 信号 0.3550，背景 2.7977 photons/pixel | [pp.14–16](papers/2026-guo-uav-motion-blur-super-resolution/paper.pdf#page=14) |
| AMAD-Net 模拟 | 64×64×1024 数据，非硬件阵列 | 无独立实际探测距离或目标速度 | 成对信号:背景从 1:100 到 1:500 等 | 1:100 中信号为 1、背景为 100 的计数条件 | [pp.12–16](papers/2026-feng-four-dimensional-attention/paper.pdf#page=12) |
| P3DTT 高速仿真 | 64×64 Gm-APD 模型，1064 nm | 2 km；合速度 188.8 m/s，横向 22.0／径向 187.5 | −8.37 dB | 信号 0.2184，背景 1.5 photons/pixel | [pp.12,15–17](papers/2026-guo-instantaneous-uav-tracking/paper.pdf#page=12) |
| P3DTT 实际外场 | 64×64 Gm-APD，1064 nm | 最远 2.5 km；横向 5–15 m/s | frame 111 −7.6839 dB | 信号 0.2731 photons/pixel | [pp.21–22](papers/2026-guo-instantaneous-uav-tracking/paper.pdf#page=21) |
| Qiao 实际远距离 | 64×64 InGaAs/InP SPAD，1550 nm | 4 km 人／10 km 电塔与风机；风机转速未给 | SBR 0.26／0.28／0.4 | 对应平均 PPP 6.6／2.0／1.7，使用原文定义 | [pp.6–7](papers/2026-qiao-multi-temporal-3d-imaging/paper.pdf#page=6) |
| Shen 室内实测 | 单 SPAD+振镜；128×128 扫描网格 | 绝对距离与目标速度未给 | SBR≈2／≈0.5 | 平均**检测** PPP 3／11，不是信号 PPP | [pp.10–12](papers/2026-shen-physics-enhanced-imaging/source.md#pdf-page-10) |
| PIDNN 本文室内 | 单 SPAD+振镜；128×128×256 | 静态；绝对距离未定量给 | SBR 0.133／0.022 | 单光子图数据；该段未给统一 PPP | [pp.11–13](papers/2026-cai-physics-informed-complex-scenarios/source.md#pdf-page-11) |
| PIDNN 公开长距离数据 | 35 μrad 发散角、22.3 μrad 接收 FoV 的扫描系统；256²／128² 网格 | 21.6／45 km，静态建筑 | SBR 0.11／0.03 | 平均 PPP 1.20／约 2.59 | [pp.11,13](papers/2026-cai-physics-informed-complex-scenarios/source.md#pdf-page-11) |
| PIDNN 多层实测 | 单 SPAD+振镜；128×128 网格 | 磨砂玻璃前后层 | SBR 0.53 | 平均 PPP 4.2；像素间不均匀 | [pp.13–14](papers/2026-cai-physics-informed-complex-scenarios/source.md#pdf-page-13) |

## 时间尺度、输出与误差

| 论文 | 采集／累计时间 | 输出率或处理时间 | 代表结果与范围 |
|---|---|---|---|
| Liu | 仿真 40 ms；实际 4 s 数据按 1/100 抽帧作等效 40 ms | 25 Hz 窗口；未给完整算法耗时 | 仿真普通距离 RMSE 0.44 m；更细栅格下超分辨率 RMSE 0.072 m；等效实测超分辨率 0.053 m。[pp.6–7](papers/2023-liu-dynamic-gm-apd-reconstruction/source.md#pdf-page-6) |
| 5D-MR | 500 脉冲累计，2.5 kHz 下为 0.2 s | 5 Hz 有效重建序列；约 0.09 GFLOPs 是复杂度估算 | 仿真 8 帧平均有符号距离误差 +0.202 m、std 0.211 m；外场角度单位及尺寸误差口径待核实。[pp.12–19](papers/2026-guo-uav-motion-blur-super-resolution/paper.pdf#page=12) |
| AMAD-Net | 模拟数据，没有真实采集时长 | 未给可验证的实际重建 fps | 1:100 八场景平均 RMSE 0.0219 m；1:300 为 0.1131 m；1:500 为 0.5416 m。[pp.14–16](papers/2026-feng-four-dimensional-attention/paper.pdf#page=14) |
| P3DTT | 拟合示例 250 脉冲，在 2.5 kHz 下为 100 ms | 对比 matched filter 输出 10 Hz；部署 P3DTT 状态输出 5 Hz | 普通动态仿真 3D MAE 0.1652 m；真实圆形／边界巡航 3D MAE 0.4003／0.4375 m；depth RMSE 0.4855／0.5209 m。[pp.20–26](papers/2026-guo-instantaneous-uav-tracking/paper.pdf#page=20) |
| Qiao | 实际 20 ms/重建窗；风机共采 0.8 s | **离线**视频 50 fps；未给算法耗时 | 10 km 电塔相对 MLE/Rapp/Li 的 PSNR 增益 15.88／10.48／4.59 dB；参考为长时 MLE，非外部绝对深度真值。[pp.6–7](papers/2026-qiao-multi-temporal-3d-imaging/paper.pdf#page=6) |
| Shen | 实测单点／总采集时长未给；原公开扫描率 5／20 Hz 属采集系统 | 576×704 常规离线推理 45 s，优化约 16 s | 模拟 10:2 RMSE 0.0070±0.0018 m；2:50 为 0.0179±0.0173 m，均非实验室毫米精度实测。[pp.7,9–13](papers/2026-shen-physics-enhanced-imaging/source.md#pdf-page-7) |
| PIDNN | 多层 0.1 ms/pixel；公开 21.6 km 数据为 22 ms/pixel | 每场景迭代优化；原文报平均 257 次和 average iteration time 151.43 s | 室内 Table III 深度 RMSE 原值 0.1127／0.1973（Scene 1）；原表单位未标明。45 km 和雾箱主要定性评价。[pp.7,11–15](papers/2026-cai-physics-informed-complex-scenarios/source.md#pdf-page-7) |

时间 bin 对应的 $c\Delta t/2$ 是距离采样间隔，不等于最终误差或真实可分辨两表面的距离。输出 10×10 子网格也不等于定位误差自动缩小 10 倍。

## 为什么这些数值不能直接排名

1. **观测统计不同。** dB SNR 是对数比，SBR 为线性比；信号 PPP 与全检测 PPP 不同。相同 SBR 的 1:100、3:300 具有不同信号数量，不能只按比值合并。
2. **实验和参考不同。** 模拟真值、长时间 MLE 参考、机载 RTK 纵向参考、照片结构参照不是同等精度的外部三维计量真值。缺少稠密真值的实测只支持定性重建比较。
3. **任务与度量不同。** 深度图 RMSE、强度图 PSNR、终点有符号 range bias、事件 TLS 残差、三维 MAE、角度 pixel/degree 和输出栅格尺寸不可互换。Liu 的 PSNR 定义还与常见峰值图像 PSNR 不同。
4. **学习协议不同。** AMAD-Net 与 Shen 使用不同训练样本、计数混合和损失；PIDNN 是每场景优化，比较监督模型时包含其训练外条件，不能把它当作相同训练后的统一推理竞赛。
5. **硬件与计算不同。** 面阵同时探测、单 SPAD 扫描及借用公开测量的数据具有不同采集预算。离线输出视频节奏与端到端实时闭环是不同证据。

## 复现信息与缺口

| 论文 | 上传全文中的代码／数据状态 | 优先补充内容 |
|---|---|---|
| Liu | 无官方代码；数据保密 | 事件数据或完整仿真、Hough 设置、PSNR 口径 |
| 5D-MR | 无官方代码；数据可合理申请 | 驻留时间表修正、角度误差单位、完整阈值与时延 |
| AMAD-Net | 无官方代码；数据可合理申请 | 生成脚本、split/seed、权重、真实硬件验证 |
| P3DTT | 无官方代码、固件或数据入口 | 外部完整三维真值、同步、协方差与阈值、硬件延时 |
| Qiao | 无官方完整代码／数据入口 | FCM 与 ADMM 参数、FFDNet 配置、实际运行时长 |
| Shen | 原公开数据有出处；本文数据与实现可合理申请 | AITV 求解与投影细节、代码、真实量化真值 |
| PIDNN | 原公开测量有出处；本文未给官方代码／数据 URL | IRF/PSF、skip 与停止准则、初始化、场景优化耗时定义 |

这是“上传全文未提供”的记录，不表示已证明网络上不存在代码。官方补充材料、项目页和作者后续开放内容仍可补充。

## 阅读启发（整理者归纳）

- 高速目标：从 Liu 的轨迹对齐、5D-MR 的驻留／重叠信息和 P3DTT 的末端参考时刻出发，分别评估运动分割、末端测量和状态预测。
- 极稀疏深度：从 AMAD-Net 的多域注意力、Qiao 的尺度可信度和 Shen 的独立物理先验分支出发，保留信号数与背景数，分析细节／去噪取舍。
- 多层／散射：PIDNN 强调先区分回波物理原因，再用场景表示与前向模型统一优化；它提供复杂静态场景思路，尚不替代高速连续跟踪。
- 联合使用这些思路是后续研究设想，不是这 7 篇论文已经共同验证的系统。
