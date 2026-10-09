r"""
认知蒸馏自动化管线引擎 v2.1
D:\1052-OS\brain\pipeline.py

v2.1: +WechatSogou微信公众号收割（解决微信文章JS渲染问题）
v2.0: +requests实际抓取 + MiniMax API蒸馏 + Obsidian同步

用法:
  python pipeline.py --mode harvest --urls "url1,url2"   # 抓取指定URL
  python pipeline.py --mode harvest                       # 从RSS源收割
  python pipeline.py --mode wechat                        # 微信公众号收割(默认关键词)
  python pipeline.py --mode wechat --keywords "AI,Agent" # 指定关键词搜索微信
  python pipeline.py --mode distill                       # LLM蒸馏
  python pipeline.py --mode merge                         # 合并到SKILL.md
  python pipeline.py --mode full                          # 全流程(含wechat+Rss)
  python pipeline.py --mode status                        # 查看状态
  python pipeline.py --mode sync                          # 同步Obsidian
"""
import sys
import json
import os
import re
import csv
import time
import html as html_lib
from datetime import datetime
from pathlib import Path

# ============ 配置 ============
BASE_DIR = Path(r'D:\1052-OS\brain')
SKILL_FILE = BASE_DIR / 'SKILL.md'
RAW_DIR = BASE_DIR / 'raw_harvest'
DISTILLED_DIR = BASE_DIR / 'distilled'
CONFIG_FILE = BASE_DIR / 'pipeline_config.json'
HARVEST_LOG = BASE_DIR / 'harvest_log.csv'
MERGE_LOG = BASE_DIR / 'MERGE_LOG.md'

# Obsidian Vault
OBSIDIAN_VAULT = Path(r'C:\Users\19586\Documents\Obsidian Vault')
OBSIDIAN_RAW_DIR = OBSIDIAN_VAULT / 'raw'

# 混元（Hunyuan）LLM配置 — 2026-08-22 由 MiniMax-M2.7 切换为 hunyuan-turbo
# OpenAI 兼容端点；蒸馏前需将 api_key 替换为腾讯混元 API Key（Hunyuan SecretId/Key 走 TC3 签名，非 Bearer）
LLM_CONFIG = {
    "base_url": "https://api.hunyuan.cloud.tencent.com/v1",
    "model": "hunyuan-turbo",
    "api_key": "REPLACE_WITH_HUNYUAN_API_KEY",  # TODO: 配置混元 API Key 后方可运行 distill 阶段
    "max_tokens": 4096,
    "temperature": 0.3
}

TARGET_KEYWORDS = [
    'AI工具', 'Agent', 'Skill', 'GPT', 'Claude', 'LLM',
    '开源', '视频生成', 'Seedance', 'Obsidian', '知识管理',
    '工作流', '自动化', 'Prompt', '蒸馏', '认知框架',
    'Coze', '成本优化', '平替', '教程', '方法论',
    '内容创作', 'AI视频', '短剧', '故事板', 'OneDrive',
    '教育场景', '游戏化学习', '大模型', 'RAG', 'Function Calling',
    '多Agent', '提示词工程', 'AI产品', '效率工具', '工作流编排',
    '数字生命', '认知升级', '第二大脑', '知识图谱', '自动化办公'
]

HTTP_TIMEOUT = 30
HTTP_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

for d in [RAW_DIR, DISTILLED_DIR]:
    d.mkdir(exist_ok=True)


def load_config():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    default = {
        "harvested_urls": {},
        "module_index": {"current_max": 152, "last_merge": None, "version": "v11.0"},
        "target_feeds": [
            {"name": "数字生命卡兹克", "type": "wechat_rss", "url": "", "keywords": ["AI","Skill","Agent"]},
            {"name": "林小卫很行", "type": "wechat_rss", "url": "", "keywords": ["效率","AI工具","工作流"]},
            {"name": "工程人的智库", "type": "wechat_rss", "url": "", "keywords": ["工程","数字化"]},
        ],
        "llm_settings": {"provider": "minimax", "model": "MiniMax-M2.7"},
        "obsidian_sync": {"enabled": True, "vault_path": str(OBSIDIAN_VAULT)},
        "created_at": datetime.now().isoformat()
    }
    save_config(default)
    return default


def save_config(cfg):
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)


def url_hash(url):
    import hashlib
    return hashlib.md5(url.encode()).hexdigest()[:12]


def log_harvest(url, title, status, note=""):
    file_exists = HARVEST_LOG.exists()
    with open(HARVEST_LOG, 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['timestamp', 'url_hash', 'url', 'title', 'status', 'note'])
        writer.writerow([
            datetime.now().isoformat(),
            url_hash(url), url, title, status, note
        ])


# ============ Layer 1: HTML工具 ============

def html_to_markdown(html):
    """将HTML转为简化Markdown（不依赖BeautifulSoup）"""
    # 移除script/style/head
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.S | re.I)
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.S | re.I)
    html = re.sub(r'<head[^>]*>.*?</head>', '', html, flags=re.S | re.I)
    # 标题
    for i in range(6, 0, -1):
        hashes = '#' * i
        replacement = f'\n{hashes} \\1\n'
        html = re.sub(rf'<h{i}[^>]*>(.*?)</h{i}>', replacement, html, flags=re.S | re.I)
    # 段落/换行
    html = re.sub(r'<br\s*/?>', '\n', html, flags=re.I)
    html = re.sub(r'<p[^>]*>', '\n', html, flags=re.I)
    html = re.sub(r'</p>', '\n', html, flags=re.I)
    # 加粗/斜体
    html = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', html, flags=re.S | re.I)
    html = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', html, flags=re.S | re.I)
    # 链接
    html = re.sub(r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', r'[\2](\1)', html, flags=re.S | re.I)
    # 移除所有剩余标签
    html = re.sub(r'<[^>]+>', '', html)
    # HTML实体解码
    html = html_lib.unescape(html)
    # 清理多余空行
    html = re.sub(r'\n{3,}', '\n\n', html)
    return html.strip()


# ============ Layer 2: 普通URL抓取 ============

def fetch_url_content(url):
    """普通HTTP抓取URL，返回(title, content_md, error)"""
    try:
        import requests
        resp = requests.get(url, headers=HTTP_HEADERS, timeout=HTTP_TIMEOUT, allow_redirects=True)
        resp.raise_for_status()
        html = resp.text
        title_match = re.search(r'<title[^>]*>(.*?)</title>', html, re.S | re.I)
        title = title_match.group(1).strip() if title_match else Path(url).stem
        title = re.sub(r'[\\/:*?"<>|]', '_', title)[:100]
        content_md = html_to_markdown(html)
        return title, content_md, None
    except Exception as e:
        return None, None, str(e)[:120]


def harvest_urls(urls):
    """普通URL列表 → 抓取 → 保存MD"""
    cfg = load_config()
    success = fail = new_count = 0
    for url in urls:
        url = url.strip()
        if not url: continue
        uh = url_hash(url)
        if uh in cfg.get("harvested_urls", {}):
            print(f"[SKIP] Already: {url[:60]}...")
            continue
        print(f"[FETCH] {url[:70]}...")
        title, content_md, error = fetch_url_content(url)
        if error or not content_md or len(content_md) < 100:
            fail += 1
            print(f"  [FAIL] {error or 'too short'}")
            log_harvest(url, title or "error", "failed", error or "too short")
            continue
        timestamp = datetime.now().strftime('%Y%m%d%H%M')
        safe_title = re.sub(r'[\\/:*?"<>|]', '_', title)[:60]
        filename = f"[{timestamp}]{safe_title}.md"
        filepath = RAW_DIR / filename
        filepath.write_text(content_md, encoding='utf-8')
        cfg.setdefault("harvested_urls", {})[uh] = {
            "url": url, "title": title, "file": str(filepath),
            "harvested_at": datetime.now().isoformat(), "distilled": False
        }
        success += 1
        new_count += 1
        log_harvest(url, title, "ok", f"{filename} ({len(content_md)} chars)")
        print(f"  [OK] {filename} ({len(content_md)} chars)")
    save_config(cfg)
    print(f"\n[HARVEST] {success} ok, {fail} fail, {new_count} new")
    return success, fail, new_count


# ============ Layer 2.5: WeChatSogou 微信收割 ============

def init_wechat_sogou():
    """初始化 WechatSogouAPI，返回实例或None"""
    try:
        from wechatsogou.api import WechatSogouAPI
        ws = WechatSogouAPI(captcha_break_time=3)
        print("[WECHAT] WechatSogouAPI inited")
        return ws
    except ImportError:
        print("[WECHAT] wechatsogou not installed. pip install wechatsogou")
        return None
    except Exception as e:
        print(f"[WECHAT] Init error: {e}")
        return None


def wechat_search_articles(keyword, max_results=10):
    """微信搜索文章，返回 [{'title','url','author','abstract'}, ...]"""
    ws = init_wechat_sogou()
    if not ws: return []
    try:
        results = ws.search_article(keyword)
        articles = []
        for item in results[:max_results]:
            try:
                art = item.get('article', {})
                gzh = item.get('gzh', {})
                entry = {
                    'title': art.get('title', ''),
                    'url': art.get('url', ''),
                    'author': gzh.get('wechat_name', ''),
                    'abstract': art.get('abstract', ''),
                    'time': art.get('time', ''),
                }
                if entry['url'] and entry['title']:
                    articles.append(entry)
            except Exception:
                continue
        print(f"[WECHAT SEARCH] '{keyword}' -> {len(articles)} articles")
        return articles
    except Exception as e:
        print(f"[WECHAT SEARCH ERROR] {keyword}: {e}")
        return []


def wechat_fetch_content(article_url):
    """用WechatSogou获取文章完整HTML，返回 (title, content_html, error)"""
    ws = init_wechat_sogou()
    if not ws: return None, None, "not available"
    try:
        result = ws.get_article_content(article_url)
        if isinstance(result, dict):
            return result.get('title',''), result.get('content',''), None
        else:
            return getattr(result,'title',''), getattr(result,'content',''), None
    except Exception as e:
        err = str(e)
        if '验证' in err or 'captcha' in err.lower(): return None,None,"Captcha required"
        if '过期' in err or 'expire' in err.lower(): return None,None,"Link expired"
        if '限制' in err or 'rate' in err.lower(): return None,None,"Rate limited"
        return None, None, err[:120]


def harvest_wechat(keywords=None, max_per_keyword=5):
    """
    微信收割主入口:
    关键词→搜索→WechatSogou抓取完整HTML→保存MD
    返回 (success, fail, new_count)
    """
    cfg = load_config()
    if keywords is None:
        keywords = TARGET_KEYWORDS[:10]

    all_articles = []
    for kw in keywords:
        print(f"\n[WECHAT] Searching: {kw}...")
        try:
            all_articles.extend(wechat_search_articles(kw, max_results=max_per_keyword))
            time.sleep(1)
        except Exception as e:
            print(f"  [ERR] {e}")

    if not all_articles:
        print("\n[WECHAT] No articles found")
        return 0, 0, 0

    print(f"\n[WECHAT] Got {len(all_articles)} URLs, fetching...")
    success = fail = new_count = 0

    for idx, article in enumerate(all_articles, 1):
        url = article.get('url','')
        search_title = article.get('title','')
        author = article.get('author','')
        if not url: continue
        uh = url_hash(url)
        if uh in cfg.get("harvested_urls", {}):
            print(f"  [{idx}] SKIP: {search_title[:40]}...")
            continue
        print(f"  [{idx}] FETCH: {search_title[:50]}...")
        title, content_html, error = wechat_fetch_content(url)
        if error:
            fail += 1
            print(f"    [FAIL] {error}, trying requests fallback...")
            fb_title, fb_content, fb_error = fetch_url_content(url)
            if not fb_error and fb_content and len(fb_content) >= 100:
                title, content_html = fb_title, fb_content
            else:
                continue
        content_md = html_to_markdown(content_html) if content_html else ""
        if len(content_md.strip()) < 100:
            fail += 1
            print(f"    [FAIL] Too short ({len(content_md)} chars)")
            continue
        timestamp = datetime.now().strftime('%Y%m%d%H%M')
        display_title = title or search_title
        safe_title = re.sub(r'[\\/:*?"<>|]', '_', display_title)[:60]
        filename = f"[{timestamp}]{safe_title}.md"
        meta = f"""---
title: {display_title}
author: {author}
source: wechat_sogou
url: {url}
harvested_at: {datetime.now().isoformat()}
---

"""
        (RAW_DIR / filename).write_text(meta + content_md, encoding='utf-8')
        cfg.setdefault("harvested_urls", {})[uh] = {
            "url": url, "title": display_title, "file": str(RAW_DIR/filename),
            "author": author, "harvested_at": datetime.now().isoformat(),
            "distilled": False, "source": "wechat_sogou"
        }
        success += 1
        new_count += 1
        print(f"    [OK] {filename} ({len(content_md)} chars)")
        time.sleep(2)

    save_config(cfg)
    print(f"\n[WECHAT DONE] {success} ok, {fail} fail, {new_count} new")
    return success, fail, new_count


# ============ Layer 2.8: RSS/Feed解析 ============

def parse_feed(feed_url):
    """解析RSS/Atom，返回URL列表"""
    import requests
    resp = requests.get(feed_url, headers=HTTP_HEADERS, timeout=15)
    resp.raise_for_status()
    urls = []
    links = re.findall(r'<link[^>]*>([^<]+)</link>', resp.text)
    atom_links = re.findall(r'<link[^>]*href=["\']([^"\']+)["\'][^>]*/?\s*>', resp.text)
    for link in links + atom_links:
        link = link.strip()
        if link.startswith('http') and 'feed' not in link.lower():
            urls.append(link)
    seen = set()
    unique = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            unique.append(u)
    return unique[:20]


def harvest_from_feeds():
    """从RSS/Atom源收割"""
    cfg = load_config()
    feeds = cfg.get("target_feeds", [])
    if not feeds:
        print("[FEED] No feeds configured")
        return 0, 0, 0
    all_urls = []
    for feed in feeds:
        url = feed.get("url","")
        if not url: continue
        print(f"[FEED] Checking: {feed['name']}...")
        try:
            all_urls.extend(parse_feed(url))
        except Exception as e:
            print(f"  [ERR] {e}")
    if all_urls:
        print(f"\n[FEED] Found {len(all_urls)} URLs")
        return harvest_urls(all_urls)
    return 0, 0, 0


# ============ Layer 3: 蒸馏（MiniMax API） ============

def call_llm_api(prompt, system_prompt=None):
    """调用 MiniMax Chat API，返回内容或None"""
    import requests
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {LLM_CONFIG["api_key"]}'
    }
    messages = []
    if system_prompt:
        messages.append({"role":"system","content":system_prompt})
    messages.append({"role":"user","content":prompt})
    payload = {
        "model": LLM_CONFIG["model"],
        "messages": messages,
        "max_tokens": LLM_CONFIG["max_tokens"],
        "temperature": LLM_CONFIG["temperature"]
    }
    try:
        api_url = f'{LLM_CONFIG["base_url"]}/chat/completions'
        resp = requests.post(api_url, headers=headers, json=payload, timeout=60)
        resp.raise_for_status()
        result = resp.json()
        return result.get("choices",[{}])[0].get("message",{}).get("content","")
    except Exception as e:
        print(f"[LLM ERROR] {e}")
        return None


def distill_new(raw_files):
    """原始MD → MiniMax API蒸馏 → 保存模块MD"""
    cfg = load_config()
    count = 0
    for idx, raw_file in enumerate(raw_files, 1):
        try:
            content = raw_file.read_text(encoding='utf-8')
            title = raw_file.stem
            matched_kw = [kw for kw in TARGET_KEYWORDS if kw in content]
            if len(matched_kw) < 2:
                print(f"[{idx}] SKIP low relevance ({len(matched_kw)} kw)")
                continue
            module_num = cfg["module_index"]["current_max"] + 1
            print(f"[{idx}] DISTILL #{module_num}: {title} ({len(content)} chars)")

            # 构建蒸馏prompt
            content_preview = content[:8000]
            system_prompt = """你是认知蒸馏专家。从技术/方法论类文章中提炼可复用的认知框架。
输出要求：1.提取可复用的方法论/框架/模型 2.提炼工具链组合 3.收录金句/洞察 4.遵循SKILL.md现有模块结构
输出格式：## 模块XXX：{标题}\n> 来源：...\n### 核心框架\n... """
            user_prompt = f"请对以下文章进行认知蒸馏：\n\n**标题**: {title}\n**模块编号**: #{module_num}\n\n---\n\n{content_preview}\n\n---\n\n按系统提示词格式输出蒸馏结果。"

            distilled = call_llm_api(user_prompt, system_prompt)
            if not distilled:
                print(f"  [WARN] API empty, skip")
                continue

            out_file = DISTILLED_DIR / f"模块{module_num}-{title}.md"
            out_file.write_text(distilled, encoding='utf-8')
            cfg["module_index"]["current_max"] = module_num
            count += 1
            print(f"  [OK] Saved: {out_file.name}")
            time.sleep(2)
        except Exception as e:
            print(f"[{idx}] ERROR: {e}")
    save_config(cfg)
    print(f"\n[DISTILL] {count} modules distilled")
    return count


def check_raw_files():
    """检查未蒸馏的raw文件"""
    cfg = load_config()
    distilled = set()
    for info in cfg.get("harvested_urls",{}).values():
        if info.get("distilled"):
            distilled.add(info.get("file",""))
    return [f for f in sorted(RAW_DIR.glob('*.md')) if str(f) not in distilled]


# ============ Layer 4: 合并 ============

def merge_to_skill():
    """将distilled模块合并到SKILL.md"""
    cfg = load_config()
    new_files = [f for f in DISTILLED_DIR.glob('模块*.md')
                if f.stem not in (SKILL_FILE.read_text(encoding='utf-8') if SKILL_FILE.exists() else "")]
    if not new_files:
        print("[MERGE] No new modules")
        return 0
    skill_text = SKILL_FILE.read_text(encoding='utf-8')
    append_content = ""
    for df in sorted(new_files):
        append_content += f"\n\n---\n\n# {df.stem}\n\n" + df.read_text(encoding='utf-8')
    # 版本号
    old_ver = cfg["module_index"]["version"]
    parts = old_ver.replace('v','').split('.')
    new_ver = f"v{parts[0]}.{int(parts[1])+1}" if len(parts)>1 else "v11.1"
    cfg["module_index"]["version"] = new_ver
    cfg["module_index"]["last_merge"] = datetime.now().isoformat()
    append_content += f"\n\n---\n\n*SKILL.md {new_ver} · {datetime.now().strftime('%Y-%m-%d')}*\n"
    SKILL_FILE.write_text(skill_text + append_content, encoding='utf-8')
    save_config(cfg)
    # 写日志
    with open(MERGE_LOG, 'a', encoding='utf-8') as f:
        f.write(f"\n## {new_ver} - {datetime.now()}\n- 新增: {[f.name for f in new_files]}\n")
    print(f"[MERGE] {old_ver}->{new_ver}, {len(new_files)} modules")
    return len(new_files)


# ============ Layer 5: Obsidian同步 ============

def sync_to_obsidian():
    """同步raw/distilled/SKILL.md到Obsidian Vault"""
    cfg = load_config()
    synced_raw = synced_dist = 0
    import shutil
    if RAW_DIR.exists():
        dest = OBSIDIAN_RAW_DIR
        dest.mkdir(parents=True, exist_ok=True)
        for src in RAW_DIR.glob('*.md'):
            dst = dest / src.name
            if not dst.exists() or dst.stat().st_size < src.stat().st_size:
                shutil.copy2(src, dst)
                synced_raw += 1
                print(f"[SYNC RAW] {src.name}")
    if DISTILLED_DIR.exists():
        dest = OBSIDIAN_VAULT / 'brain' / 'distilled'
        dest.mkdir(parents=True, exist_ok=True)
        for src in DISTILLED_DIR.glob('*.md'):
            dst = dest / src.name
            if not dst.exists() or dst.stat().st_size < src.stat().st_size:
                shutil.copy2(src, dst)
                synced_dist += 1
                print(f"[SYNC DIST] {src.name}")
    if SKILL_FILE.exists():
        dest = OBSIDIAN_VAULT / 'brain' / 'SKILL.md'
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(SKILL_FILE, dest)
        print(f"[SYNC SKILL] SKILL.md ({SKILL_FILE.stat().st_size//1024}KB)")
    cfg.setdefault("obsidian_sync",{})["last_sync"] = datetime.now().isoformat()
    save_config(cfg)
    print(f"\n[SYNC] {synced_raw+synced_dist} files synced")
    return synced_raw, synced_dist


# ============ 状态 ============

def show_status():
    cfg = load_config()
    raw_n = len(list(RAW_DIR.glob('*.md'))) if RAW_DIR.exists() else 0
    dist_n = len(list(DISTILLED_DIR.glob('*.md'))) if DISTILLED_DIR.exists() else 0
    print("="*50)
    print(f"  SKILL Version:   {cfg['module_index']['version']}")
    print(f"  Raw Articles:    {raw_n}")
    print(f"  Distilled:       {dist_n}")
    print(f"  Harvested URLs:  {len(cfg.get('harvested_urls',{}))}")
    print("="*50)


# ============ 主入口 ============

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Cognitive Distillation Pipeline v2.1')
    parser.add_argument('--mode', required=True,
                        choices=['harvest','distill','merge','full','status','sync','wechat'],
                        help='Operation mode')
    parser.add_argument('--urls', help='Comma-separated URLs')
    parser.add_argument('--keywords', help='Comma-separated keywords for wechat mode')
    args = parser.parse_args()

    if args.mode == 'wechat':
        kw = None
        if args.keywords:
            kw = [k.strip() for k in args.keywords.split(',') if k.strip()]
        harvest_wechat(keywords=kw)

    elif args.mode == 'harvest':
        if args.urls:
            harvest_urls([u.strip() for u in args.urls.split(',') if u.strip()])
        else:
            harvest_from_feeds()

    elif args.mode == 'distill':
        files = check_raw_files()
        print(f"Found {len(files)} raw files")
        if files: distill_new(files)

    elif args.mode == 'merge':
        merge_to_skill()

    elif args.mode == 'full':
        print("=== Full Pipeline ===")
        # 先微信收割，再RSS，再蒸馏合并同步
        kw = None
        if args.keywords:
            kw = [k.strip() for k in args.keywords.split(',') if k.strip()]
        harvest_wechat(keywords=kw)
        harvest_from_feeds()
        files = check_raw_files()
        if files: distill_new(files)
        merge_to_skill()
        sync_to_obsidian()

    elif args.mode == 'sync':
        sync_to_obsidian()

    elif args.mode == 'status':
        show_status()
