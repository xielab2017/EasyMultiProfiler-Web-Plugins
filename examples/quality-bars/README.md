# 样本质量条形图

把结果表里的样本均值画成条形图，快速比较样本间的差异。

适用于 EMP Web 10.0.0 及以上版本。插件版本 1.0.0。

[插件详情与下载](https://xielab2017.github.io/EasyMultiProfiler-Web-Plugins/examples/quality-bars/) · [单独下载 plugin.json](https://xielab2017.github.io/EasyMultiProfiler-Web-Plugins/examples/quality-bars/plugin.json)

## 安装与使用

1. 在「插件」上传 plugin.json 并启用。EMP 10.0–10.1 的安装入口在工作台。
2. 选择已完成且含 mean 列的插件任务，例如「样本质量概览」的结果。
3. 选择 Sample quality bars，点击「展示结果」。

默认显示前 30 行。EMP 10.2 起可在设置中切换表格或条形图，并调整行数。

## 使用权限

job.result.read 读取所选任务的结果表。
