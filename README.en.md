# EasyMultiProfiler Web Plugins

[中文](README.md) · [Open the English plugin store](https://xielab2017.github.io/EasyMultiProfiler-Web-Plugins/en/)

Open a plugin to see its preview, compatibility, installation steps and permissions. In EMP 10.4 or later, install it directly from the Plugins page.

| Plugin | Type | Minimum EMP version |
| --- | --- | --- |
| [Zotero-style research chat](examples/zotero-style-chat/README.en.md) | Research chat | 10.3.0 |
| [Sample quality summary](examples/sample-quality/README.en.md) | Analysis methods | 10.0.0 |
| [Sample quality bars](examples/quality-bars/README.en.md) | Result views | 10.0.0 |
| [Groq model provider](ai-providers/groq/README.en.md) | Model services | 9.4.0 |

## Add a plugin

Place the manifest in its own directory and add both languages to catalog.json. Supply one preview per language in assets/previews. Run python3 build.py to generate the store, detail pages and plugin READMEs. Test the manifest in the supported EMP version before publishing.
