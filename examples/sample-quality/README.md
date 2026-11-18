# 样本质量概览

按样本统计观测值、缺失值、均值、标准差和变异系数。

适用于 EMP Web 10.0.0 及以上版本。插件版本 1.0.0。

[插件详情与下载](https://xielab2017.github.io/EasyMultiProfiler-Web-Plugins/examples/sample-quality/) · [单独下载 plugin.json](https://xielab2017.github.io/EasyMultiProfiler-Web-Plugins/examples/sample-quality/plugin.json)

## 安装与使用

1. 在「插件」上传 plugin.json 并启用。EMP 10.0–10.1 的安装入口在工作台。
2. 导入实验矩阵，在插件面板选择实验、主 assay 和 Sample quality summary。
3. 点击「运行分析」查看指标。10.2 起可在插件设置中选择需要的指标。

适用于特征为行、样本为列的数值矩阵。变异系数使用标准差除以均值，均值为零时结果为空。

## 使用权限

assay.read 读取选定矩阵，job.result.write 写入新任务结果。
