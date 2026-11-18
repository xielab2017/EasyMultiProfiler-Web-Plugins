# Groq 模型接口

把 Groq 接入 EMP 的模型选择器，用自己的 API Key 测试连接。

适用于 EMP Web 9.4.0 及以上版本。插件版本 1.0.0。

[插件详情与下载](https://xielab2017.github.io/EasyMultiProfiler-Web-Plugins/ai-providers/groq/) · [单独下载 plugin.json](https://xielab2017.github.io/EasyMultiProfiler-Web-Plugins/ai-providers/groq/plugin.json)

## 安装与使用

1. 下载 plugin.json，在 EMP 安装目录建立 plugins/ai-providers/groq/ 并把文件放入其中。
2. 刷新「模型与 API」，选择 Groq · Plugin，填写自己的 Groq API Key。
3. 检测模型列表，选择账号可用的模型，保存并加载后进行连接测试。

由本机管理员安装。需要可访问 Groq 的网络和有效凭据，模型供应情况以账号的检测结果为准。

## 使用权限

调用模型会向 api.groq.com 发送本次提交的内容。下载包只包含服务清单。
