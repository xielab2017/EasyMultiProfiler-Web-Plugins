"""Build portable static pages from catalog metadata and each installable manifest."""
import hashlib
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = "https://github.com/xielab2017/EasyMultiProfiler-Web-Plugins"
kinds = ["研究对话", "分析方法", "结果展示", "模型服务"]
def link(url, label, cls=""):
    return f'<a href="{escape(url,quote=True)}" class="{cls}">{escape(label)}</a>'

def frame(title, prefix, body, description):
    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="{escape(description,quote=True)}"><title>{escape(title)} · EMP Web</title><link rel="stylesheet" href="{prefix}store.css"></head>
<body><header><nav aria-label="主导航"><a class="brand" href="{prefix}index.html"><b>emp<span>·</span></b><span>EasyMultiProfiler Web</span></a><a class="repo" href="{REPO}">GitHub ↗</a></nav></header><main>{body}</main><footer><span>EasyMultiProfiler Web</span>{link(REPO+'/issues','反馈与建议 ↗')}</footer></body></html>'''

records = json.loads((ROOT / 'catalog.json').read_text())
cards = []
install_index = []
for record in records:
    p = Path(record["path"])
    folder = (ROOT / p).resolve()
    if not folder.is_relative_to(ROOT) or p.is_absolute():
        raise ValueError("Plugin path outside the catalog")
    manifest = json.loads((folder/'plugin.json').read_text())
    title,summary,kind,minimum,mark = (escape(record[k]) for k in ("title","summary","kind","minimum","mark"))
    version = escape(manifest["version"])
    install_index.append({key: record[key] for key in ('path','title','kind','summary','minimum')} |
        dict(id=manifest['id'], version=manifest['version'], sha256=hashlib.sha256((folder/'plugin.json').read_bytes()).hexdigest(),
             permissions=manifest.get('permissions',[manifest.get('base_url','')])))
    readme = f"# {record['title']}\n\n{record['summary']}\n\n[在 EMP 中安装](http://127.0.0.1:8080/#plugins/{manifest['id']}) · [插件页面](https://xielab2017.github.io/EasyMultiProfiler-Web-Plugins/{p}/)\n\n网页安装需要 EMP 10.4.0 或以上版本。默认连接本机 8080，其他地址可直接在该实例的「插件」页安装。清单兼容 EMP {minimum}+。\n\n" + '\n'.join(f"{i}. {step}" for i,step in enumerate(record['steps'],1)) + f"\n\n{record['note']}\n\n使用权限：{record['permission']}\n"
    (folder/'README.md').write_text(readme)
    icon = f'<span class="icon icon-{kinds.index(kind)}" aria-hidden="true">{mark}</span>'
    cards.append(f'''<article class="card" data-kind="{kind}" data-search="{escape(manifest['id'],quote=True)} {escape(manifest['name'],quote=True)}"><div class="meta">{icon}<span>{kind}</span></div><h2><a href="{p}/">{title}</a></h2><p>{summary}</p><div class="cardfoot"><span>EMP {minimum}+</span><span aria-hidden="true">↗</span></div></article>''')
    steps = ''.join(f'<li>{escape(step)}</li>' for step in record['steps'])
    prefix='../'*len(p.parts)
    body=f'''<div class="back">{link(prefix+'index.html','← 全部插件')}</div><section class="detail"><div class="detailhead">{icon}<div><span class="eyebrow">{kind}</span><h1>{title}</h1></div></div><p class="lead">{summary}</p><div class="facts"><span>插件 v{version}</span><span>EMP {minimum}+</span></div><a class="primary" href="http://127.0.0.1:8080/#plugins/{manifest['id']}">在 EMP 中安装 ↗</a> <a class="source" href="plugin.json" download="plugin.json">下载 plugin.json</a> {link(REPO+'/tree/main/'+str(p),'查看源码 ↗','source')}</section><section class="guide"><p>在线安装适用 EMP 10.4.0 及以上版本。按钮打开本机 8080 的插件页，使用其他地址时可直接在该实例的「插件」页安装。</p><h2>安装与使用</h2><ol>{steps}</ol><p>{escape(record['note'])}</p><h2>使用权限</h2><p>{escape(record['permission'])}</p></section>'''
    (folder/'index.html').write_text(frame(title,prefix,body,summary))

filters=''.join(f'<button type="button" aria-pressed="{str(i==0).lower()}" data-filter="{k}">{k}</button>' for i,k in enumerate(['全部']+kinds))
home=f'''<section class="intro"><div class="eyebrow">EasyMultiProfiler Web 插件</div><h1>插件商店<span>.</span></h1><p>为你的分析工作台添加研究助手、分析方法与结果视图。</p><form role="search" onsubmit="return false"><span aria-hidden="true" class="magnifier"></span><input type="search" id="search" aria-label="搜索插件" placeholder="搜索插件、功能或模型"></form></section><section class="list" aria-label="插件目录"><div class="toolbar"><div class="filters" aria-label="插件类型">{filters}</div><span id="count" role="status">{len(cards)} 个插件</span></div><div class="grid">{''.join(cards)}</div><p id="empty" hidden>没有匹配的插件。请尝试其他关键词或类型。</p></section><script src="store.js" defer></script>'''
(ROOT/'index.html').write_text(frame("EasyMultiProfiler Web 插件","./",home,"浏览、筛选和下载 EasyMultiProfiler Web 插件。"))

(ROOT/'store-index.json').write_text(json.dumps(install_index,ensure_ascii=False,indent=2)+'\n')
