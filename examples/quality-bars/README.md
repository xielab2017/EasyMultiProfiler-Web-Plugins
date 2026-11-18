# 样本质量条形图

把结果表里的样本均值画成条形图，快速比较样本间的差异。

[在 EMP 中安装](http://127.0.0.1:8080/#plugins/quality-bars) · [插件页面](https://xielab2017.github.io/EasyMultiProfiler-Web-Plugins/examples/quality-bars/)

网页安装需要 EMP 10.4.0 或以上版本。默认连接本机 8080，其他地址可直接在该实例的「插件」页安装。清单兼容 EMP 10.0.0+。

1. 在 EMP 10.4 或更高版本，打开「插件」，点击此插件的「安装并启用」。
2. 选择已完成且含 mean 列的插件任务，例如「样本质量概览」的结果。
3. 选择 Sample quality bars，点击「展示结果」。

默认显示前 30 行。EMP 10.2 起可在设置中切换表格或条形图，并调整行数。

使用权限：job.result.read 读取所选任务的结果表。
