# EasyMultiProfiler Web 插件

[打开插件商店](https://xielab2017.github.io/EasyMultiProfiler-Web-Plugins/)。选择插件后点击「在 EMP 中安装」，或直接在 EMP 10.4+ 的插件页一键安装。兼容版本以各插件页为准。

| 插件 | 类型 | 最低 EMP 版本 |
| --- | --- | --- |
| [Zotero 风格研究助手](examples/zotero-style-chat/) | 研究对话 | 10.3.0 |
| [样本质量概览](examples/sample-quality/) | 分析方法 | 10.0.0 |
| [样本质量条形图](examples/quality-bars/) | 结果展示 | 10.0.0 |
| [Groq 模型接口](ai-providers/groq/) | 模型服务 | 9.4.0 |

## 添加插件

每个插件有自己的文件夹。放入 plugin.json 和 README.md，在 catalog.json 添加用途、安装步骤和兼容版本，运行 python3 build.py 生成商店首页和详情页。使用对应版本的 EMP 验证清单后发布。
