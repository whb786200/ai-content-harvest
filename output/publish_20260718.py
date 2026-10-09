import re
import json
import urllib.request
from pathlib import Path

# 配置
md_path = Path('D:/1052-OS/brain/output/2026-07-18-164-163-AI协作铁律.md')
html_path = Path('D:/1052-OS/article.html')
api_url = 'http://119.29.168.239:8899/api/publish_ext'

md_text = md_path.read_text(encoding='utf-8')
lines = md_text.splitlines()

def escape_html(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def parse_inline(text):
    # 加粗 **text**
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # 斜体 *text*
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', text)
    return text

html_blocks = []
i = 0
while i < len(lines):
    line = lines[i].strip()

    if not line:
        i += 1
        continue

    if line.startswith('#'):
        level = len(line) - len(line.lstrip('#'))
        level = min(max(level, 1), 6)
        text = line.lstrip('#').strip()
        text = parse_inline(text)
        if level == 1:
            html_blocks.append(f'<h1 style="font-size:22px;font-weight:bold;color:#0F4C81;margin:24px 0 16px 0;padding-bottom:8px;border-bottom:2px solid #0F4C81;">{text}</h1>')
        elif level == 2:
            html_blocks.append(f'<h2 style="font-size:18px;font-weight:bold;color:#0F4C81;margin:22px 0 12px 0;padding-left:10px;border-left:4px solid #0F4C81;">{text}</h2>')
        elif level == 3:
            html_blocks.append(f'<h3 style="font-size:16px;font-weight:bold;color:#333;margin:18px 0 10px 0;padding-left:8px;border-left:3px solid #0F4C81;">{text}</h3>')
        else:
            html_blocks.append(f'<h{level} style="font-size:15px;font-weight:bold;color:#333;margin:14px 0 8px 0;">{text}</h{level}>')
        i += 1
        continue

    if line == '---' or line == '***':
        html_blocks.append('<hr style="border:none;border-top:1px solid #E0E0E0;margin:20px 0;"/>')
        i += 1
        continue

    if line.startswith('>'):
        quote_lines = []
        while i < len(lines) and lines[i].strip().startswith('>'):
            qline = lines[i].strip()[1:].strip()
            quote_lines.append(qline)
            i += 1
        quote_text = '<br/>'.join(parse_inline(l) for l in quote_lines if l)
        html_blocks.append(f'<blockquote style="margin:16px 0;padding:12px 16px;background:#F0F4F8;border-left:4px solid #0F4C81;color:#555;font-size:15px;line-height:1.75;">{quote_text}</blockquote>')
        continue

    if line.startswith('|'):
        rows = []
        while i < len(lines) and lines[i].strip().startswith('|'):
            cells = [c.strip() for c in lines[i].strip().split('|')[1:-1]]
            rows.append(cells)
            i += 1
        body_rows = []
        for r in rows:
            if all(re.match(r'^:?-+:?$', c.strip()) for c in r):
                continue
            body_rows.append(r)
        if body_rows:
            thead = '<tr>' + ''.join(f'<th style="padding:10px;background:#0F4C81;color:#fff;text-align:left;font-weight:bold;border:1px solid #ddd;">{escape_html(c)}</th>' for c in body_rows[0]) + '</tr>'
            tbody = ''
            for r in body_rows[1:]:
                tbody += '<tr>' + ''.join(f'<td style="padding:10px;border:1px solid #ddd;text-align:left;">{parse_inline(escape_html(c))}</td>' for c in r) + '</tr>'
            html_blocks.append(f'<div style="overflow-x:auto;margin:16px 0;"><table style="width:100%;border-collapse:collapse;font-size:14px;line-height:1.6;">{thead}<tbody>{tbody}</tbody></table></div>')
        continue

    para_lines = []
    while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith(('#', '>', '|', '---')):
        para_lines.append(lines[i].strip())
        i += 1
    para_text = ' '.join(para_lines)
    para_text = parse_inline(para_text)
    html_blocks.append(f'<p style="font-size:15px;line-height:1.75;color:#333;margin:12px 0;text-align:justify;">{para_text}</p>')

content_html = '\n'.join(html_blocks)
full_html = f'<section style="font-family:-apple-system, BlinkMacSystemFont, \'PingFang SC\', \'Microsoft YaHei\', sans-serif; padding: 10px 0;">\n{content_html}\n</section>'

html_path.write_text(full_html, encoding='utf-8')
print(f'HTML saved to: {html_path}')

article_title = '工程人玩转AI的两条铁律：把决策交给代码，把目标交给AI'

payload = {
    'account': 'default',
    'title': article_title,
    'content': full_html,
    'thumb_media_id': ''
}

try:
    data = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(api_url, data=data, headers={'Content-Type': 'application/json'}, method='POST')
    with urllib.request.urlopen(req, timeout=30) as resp:
        resp_text = resp.read().decode('utf-8')
        print('API response:', resp_text)
        result = json.loads(resp_text)
        if result.get('media_id'):
            print('SUCCESS')
            print(f"media_id={result.get('media_id')}")
        else:
            print('FAILURE: no media_id')
except Exception as e:
    print('FAILURE:', str(e))
