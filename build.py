"""Build the Chinese and English plugin stores from one versioned manifest per plugin."""
import hashlib
import json
import os
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = "https://github.com/xielab2017/EasyMultiProfiler-Web-Plugins"
SITE = "https://xielab2017.github.io/EasyMultiProfiler-Web-Plugins/"
records = json.loads((ROOT / "catalog.json").read_text())
kinds = ["研究对话", "分析方法", "结果展示", "模型服务"]
en_kinds = ["Research chat", "Analysis methods", "Result views", "Model services"]

def relative(file, target):
    return os.path.relpath(target, file.parent)

def page_file(lang, path=""):
    return ROOT / ("en" if lang == "en" else "") / path / "index.html"

def link(url, label, cls=""):
    return f'<a href="{escape(str(url),quote=True)}" class="{cls}">{escape(label)}</a>'

def page(lang, path, title, description, body):
    file = page_file(lang, path)
    en = lang == "en"
    alternate = relative(file, page_file("zh" if en else "en",path))
    home = relative(file, page_file(lang))
    language = f'<a class="language" hreflang="{"zh-CN" if en else "en"}" href="{alternate}" lang="{"zh-CN" if en else "en"}">{"中文" if en else "English"}</a>'
    brand = f'<a class="brand" href="{home}"><b>emp<span>·</span></b><span>EasyMultiProfiler Web</span></a>'
    file.parent.mkdir(parents=True,exist_ok=True)
    file.write_text(f'''<!doctype html>
<html lang="{"en" if en else "zh-CN"}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="{escape(description,quote=True)}"><title>{escape(title)} · EMP Web</title><link rel="stylesheet" href="{relative(file,ROOT/'store.css')}"></head>
<body><header><nav aria-label="{'Main navigation' if en else '主导航'}">{brand}<div class="navlinks">{language} {link(REPO,'GitHub ↗','repo')}</div></nav></header><main>{body}</main><footer><span>EasyMultiProfiler Web</span>{link(REPO+'/issues','Send feedback ↗' if en else '反馈与建议 ↗')}</footer></body></html>''')

def preview(record, lang, file):
    plugin_id = Path(record['path']).name
    src = relative(file,ROOT/'assets'/'previews'/f'{plugin_id}-{lang}.svg')
    alt = (record['en'] if lang == 'en' else record)['preview_alt']
    return f'<img class="plugin-preview" loading="lazy" src="{src}" alt="{escape(alt,quote=True)}">'

def plugin_page(record, manifest, lang):
    en = lang == 'en'
    t = record['en'] if en else record
    path = record['path']
    file = page_file(lang,path)
    folder = ROOT / path
    minimum, version = record['minimum'], manifest['version']
    install = 'http://127.0.0.1:8080/#plugins/'+manifest['id']
    usage = ('Online installation requires EMP 10.4 or later. The install button opens port 8080 on this computer. For another address, open Plugins in that EMP instance.' if en else '在线安装需要 EMP 10.4 或更高版本。安装按钮打开本机 8080 端口。使用其他地址时，直接从该实例的「插件」页安装。')
    primary = link(install,'Install in EMP ↗' if en else '在 EMP 中安装 ↗','primary')
    download = relative(file,folder/'plugin.json')
    actions = f'{primary} <a class="source" href="{download}" download="plugin.json">{"Download" if en else "下载"} plugin.json</a> ' + link(REPO+'/tree/main/'+path,'Source on GitHub ↗' if en else 'GitHub 源码 ↗','source')
    preview_file = relative(file,ROOT/'assets'/'previews'/f"{manifest['id']}-{lang}.svg")
    steps = ''.join(f'<li>{escape(step)}</li>' for step in t['steps'])
    body = f'''<div class="back">{link(relative(file,page_file(lang)),'← All plugins' if en else '← 全部插件')}</div>
<section class="detail"><div class="eyebrow">{escape(t['kind'])}</div><h1>{escape(t['title'])}</h1><p class="lead">{escape(t['summary'])}</p><div class="facts"><span>{"Plugin" if en else "插件"} v{version}</span><span>EMP {minimum}+</span></div>{actions}</section>
<section class="guide"><h2>{"Plugin preview" if en else "效果预览"}</h2><figure><a href="{preview_file}">{preview(record,lang,file)}</a><figcaption>{escape(t['preview_alt'])} {link(preview_file,'View full size' if en else '查看大图')}</figcaption></figure><h2>{"Install and use" if en else "安装与使用"}</h2><p>{usage}</p><ol>{steps}</ol><p>{escape(t['note'])}</p><h2>{"Permissions" if en else "使用权限"}</h2><p>{escape(t['permission'])}</p></section>'''
    page(lang,path,t['title'],t['summary'],body)
    readme = folder / ('README.en.md' if en else 'README.md')
    switch = '[中文](README.md)' if en else '[English](README.en.md)'
    image = relative(readme, ROOT/'assets'/'previews'/f"{manifest['id']}-{lang}.svg")
    url = SITE+('en/' if en else '')+path+'/'
    steps_md = '\n'.join(f'{i}. {step}' for i, step in enumerate(t['steps'],1))
    readme.write_text(f"# {t['title']}\n\n{switch}\n\n{t['summary']}\n\n![{t['preview_alt']}]({image})\n\n[{'Install in EMP' if en else '在 EMP 中安装'}]({install}) · [{'Plugin page' if en else '插件页面'}]({url})\n\nEMP {minimum}+ · v{version}\n\n{usage}\n\n{steps_md}\n\n{t['note']}\n\n{t['permission']}\n")

def home_page(lang, manifests):
    en = lang == 'en'
    file = page_file(lang)
    cards = []
    for record,m in zip(records,manifests):
        t = record['en'] if en else record
        category = kinds.index(record['kind'])
        search = escape(' '.join([m['id'],record['title'],record['en']['title'],record['summary'],record['en']['summary']]),quote=True)
        target = relative(file,page_file(lang,record['path']))
        cards.append(f'''<article class="card" data-kind="{category}" data-search="{search}">{preview(record,lang,file)}<div class="meta"><span>{escape(t['kind'])}</span><span>EMP {record['minimum']}+</span></div><h2>{link(target,t['title'])}</h2><p>{escape(t['summary'])}</p></article>''')
    labels = ['All']+en_kinds if en else ['全部']+kinds
    filters = ''.join(f'<button type="button" aria-pressed="{str(i==0).lower()}" data-filter="{i-1}">{label}</button>' for i,label in enumerate(labels))
    lead = 'Add research chat, analysis methods and result views to your workspace.' if en else '为你的分析工作台添加研究助手、分析方法与结果视图。'
    body = f'''<section class="intro"><div class="eyebrow">{'EasyMultiProfiler Web Plugins' if en else 'EasyMultiProfiler Web 插件'}</div><h1>{'Plugin store' if en else '插件商店'}<span>.</span></h1><p>{lead}</p><form role="search" onsubmit="return false"><span aria-hidden="true" class="magnifier"></span><input type="search" id="search" aria-label="{'Search plugins' if en else '搜索插件'}" placeholder="{'Search plugins, features or models' if en else '搜索插件、功能或模型'}"></form></section>
<section class="list" aria-label="{'Plugin catalog' if en else '插件目录'}"><div class="toolbar"><div class="filters" aria-label="{'Plugin categories' if en else '插件类型'}">{filters}</div><span id="count" role="status">{len(cards)} {'plugins' if en else '个插件'}</span></div><div class="grid">{''.join(cards)}</div><p id="empty" hidden>{'No matching plugins. Try another keyword or category.' if en else '没有匹配的插件。请尝试其他关键词或类型。'}</p></section><script src="{relative(file,ROOT/'store.js')}" defer></script>'''
    page(lang,'','EasyMultiProfiler Web Plugins' if en else 'EasyMultiProfiler Web 插件',lead,body)

index = []
manifests = []
for record in records:
    folder = (ROOT/record['path']).resolve()
    if not folder.is_relative_to(ROOT) or Path(record['path']).is_absolute():
        raise ValueError('Plugin path outside the catalog')
    data = (folder/'plugin.json').read_bytes()
    manifest = json.loads(data)
    manifests.append(manifest)
    index.append({k:record[k] for k in ('path','title','kind','summary','minimum','preview_alt')} |
        dict(id=manifest['id'],version=manifest['version'],sha256=hashlib.sha256(data).hexdigest(),
             en={k:record['en'][k] for k in ('title','kind','summary','preview_alt')},
             permissions=manifest.get('permissions',[manifest.get('base_url','')])))
    for lang in ('zh','en'):
        plugin_page(record,manifest,lang)
for lang in ('zh','en'):
    home_page(lang,manifests)
(ROOT/'store-index.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')
