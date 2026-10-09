"""
pdf-spec-extractor 集成补丁 for 1052-OS pipeline.py
将此文件放在 D:\1052-OS\brain\ 目录下，
然后用 `python spec_patch.py` 打补丁，或直接在 pipeline.py 中手动合并。
"""

# ============================================================
# 补丁说明：
# 在 pipeline.py 的 harvest / distill / merge 基础上，
# 新增 --mode spec-extract 模式，专门处理规范 PDF。
# ============================================================

SPEC_EXTRACT_CODE = r'''

# ============ 新增导入（放在 pipeline.py 顶部 import 区域）============
try:
    import pdfplumber
    import pandas as pd
    SPEC_EXTRACT_AVAILABLE = True
except ImportError:
    SPEC_EXTRACT_AVAILABLE = False
    print("[WARN] pdfplumber/pandas 未安装，规范提取功能不可用")
    print("       请运行：pip install pdfplumber pandas openpyxl")

# ============ 新增：规范提取器类（放在 import 之后）============

class ChineseSpecExtractor:
    """中国工程规范 PDF 结构化提取器"""

    CHINA_STD_PATTERN = r'(GB\s*\d+[.\-]\d+|JGJ\s*\d+[.\-]\d+|CJJ\s*\d+|DB\d+/\w+-\d+|GB/T\s*\d+)'
    CLAUSE_PATTERN = r'(\d+[.\-]\d+[.\-]?\d*)'
    MANDATORY_KEYWORDS = ['必须', '严禁', '应', '不应', '不得', '宜', '不宜', '可']

    def __init__(self):
        self.standard_no = ""
        self.clauses = []
        self.toc = []

    def extract(self, pdf_path: str) -> dict:
        """提取规范 PDF 结构化数据，返回 dict"""
        import os, re
        from pathlib import Path

        result = {
            'document_name': os.path.basename(pdf_path),
            'standard_no': '',
            'total_pages': 0,
            'clauses': [],
            'toc': [],
            'errors': []
        }

        try:
            with pdfplumber.open(pdf_path) as pdf:
                result['total_pages'] = len(pdf.pages)
                full_text = ""
                page_texts = []

                for i, page in enumerate(pdf.pages):
                    text = page.extract_text() or ""
                    full_text += text + "\n"
                    if text.strip():
                        page_texts.append((i + 1, text))

                # 识别规范号
                std_matches = re.findall(self.CHINA_STD_PATTERN, full_text[:5000], re.IGNORECASE)
                if std_matches:
                    result['standard_no'] = std_matches[0].replace(' ', '')
                    self.standard_no = result['standard_no']

                # 提取目录
                result['toc'] = self._extract_toc(page_texts)

                # 提取条文
                result['clauses'] = self._extract_clauses(page_texts)

        except Exception as e:
            result['errors'].append(str(e))

        return result

    def _extract_toc(self, page_texts: list) -> list:
        import re
        toc = []
        in_toc = False
        for page_no, text in page_texts[:15]:
            for line in text.split('\n'):
                if '目录' in line or 'CONTENTS' in line.upper():
                    in_toc = True
                    continue
                if in_toc:
                    m = re.match(r'(\d+[.\-]\d+)\s+(.+?)\s+(\d+)', line.strip())
                    if m:
                        toc.append({
                            'clause_no': m.group(1),
                            'title': m.group(2).strip(),
                            'page': int(m.group(3))
                        })
                    # 遇到正文章节，结束目录
                    if re.match(r'^\d+[.\-]\d+\s+[\u4e00-\u9fff]', line):
                        in_toc = False
        return toc

    def _extract_clauses(self, page_texts: list) -> list:
        import re
        clauses = []

        for page_no, text in page_texts:
            lines = text.split('\n')
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                # 匹配条文号：3.1.2 或 A.0.1
                clause_m = re.match(r'^(\d+[.\-]\d+[.\-]?\d*)\s+(.+)', line)
                if not clause_m:
                    # 尝试匹配「3.1.2 条文内容」格式（条文号后有空格）
                    clause_m = re.match(r'^(\d+\.\d+\.?\d*)\s', line)

                if clause_m:
                    clause_no = clause_m.group(1).replace('-', '.')
                    # 收集条文内容（到下一个条文号为止）
                    content_parts = []
                    if len(clause_m.groups()) > 1:
                        content_parts.append(clause_m.group(2))
                    j = i + 1
                    while j < len(lines):
                        next_line = lines[j].strip()
                        # 下一个条文号，停止
                        if re.match(r'^\d+[.\-]\d+', next_line):
                            break
                        # 新章节标题（纯中文，无条文号），停止
                        if re.match(r'^[第\u4e00-\u9fff]', next_line) and not re.match(r'^\d', next_line):
                            break
                        if next_line:
                            content_parts.append(next_line)
                        j += 1

                    content = ' '.join(content_parts).strip()
                    mandatory_level = self._detect_mandatory(content)
                    referenced = self._extract_referenced(content)

                    clauses.append({
                        'clause_no': clause_no,
                        'mandatory_level': mandatory_level,
                        'content': content[:500],  # 摘要，避免过长
                        'content_full': content,
                        'page_no': page_no,
                        'referenced_standards': referenced
                    })
                    i = j
                else:
                    i += 1
        return clauses

    def _detect_mandatory(self, content: str) -> str:
        for kw in self.MANDATORY_KEYWORDS:
            if content[:30].startswith(kw):
                return kw
        return 'unknown'

    def _extract_referenced(self, content: str) -> list:
        import re
        refs = []
        # 中文引用：《GB XXXX》
        cn_refs = re.findall(r'《(' + self.CHINA_STD_PATTERN[1:-1] + r')》', content)
        refs.extend(cn_refs)
        # 英文引用：GB XXXX / ASTM XXXX
        en_refs = re.findall(r'(?:GB|ASTM|ACI|AISC|AWS|UL|NFPA)\s*\d+', content, re.IGNORECASE)
        refs.extend(en_refs)
        return list(set(refs))


# ============ 新增：spec_extract 主函数 ============

def mode_spec_extract(args):
    """--mode spec-extract：处理规范 PDF，结构化提取后蒸馏"""
    import os, json
    from pathlib import Path

    pdf_path = args.pdf_path if hasattr(args, 'pdf_path') and args.pdf_path else None
    pdf_dir = args.pdf_dir if hasattr(args, 'pdf_dir') and args.pdf_dir else None

    if not SPEC_EXTRACT_AVAILABLE:
        print("[ERROR] 请先安装依赖：pip install pdfplumber pandas openpyxl")
        return

    extractor = ChineseSpecExtractor()

    # 确定要处理的文件列表
    pdf_files = []
    if pdf_path:
        pdf_files = [pdf_path]
    elif pdf_dir:
        pdf_files = [str(p) for p in Path(pdf_dir).glob('*.pdf')]
    else:
        print("[ERROR] 请指定 --pdf-path 或 --pdf-dir")
        print("用法：python pipeline.py --mode spec-extract --pdf-dir D:/1052-OS/data/specs")
        return

    print(f"[SPEC] 找到 {len(pdf_files)} 个 PDF 文件")

    all_results = []
    for pdf_file in pdf_files:
        print(f"\n[SPEC] 处理：{os.path.basename(pdf_file)}")
        try:
            result = extractor.extract(pdf_file)
            all_results.append(result)

            std_no = result['standard_no'] or 'unknown'
            clauses_count = len(result['clauses'])
            print(f"  [OK] 规范号：{std_no}，提取条文数：{clauses_count}")

            # 保存 Excel
            if result['clauses']:
                export_spec_to_excel(result, pdf_file)

            # 保存 JSON（供 API 调用）
            json_path = Path(pdf_file).with_suffix('.json')
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            print(f"  [JSON] 已保存：{json_path.name}")

            # 生成 Markdown（供 Obsidian 查看）
            md_path = Path(pdf_file).with_suffix('.md')
            generate_spec_markdown(result, md_path)
            print(f"  [MD] 已保存：{md_path.name}")

            # 调用蒸馏（如果有 LLM 配置）
            if hasattr(args, 'distill') and args.distill:
                distill_spec_clauses(result, pdf_file)

        except Exception as e:
            print(f"  [ERROR] {e}")

    print(f"\n[SPEC] 全部完成，共处理 {len(all_results)} 个文件")


def export_spec_to_excel(result: dict, pdf_path: str):
    """导出规范条文到 Excel"""
    import pandas as pd
    from pathlib import Path

    rows = []
    for c in result['clauses']:
        rows.append({
            '规范号': result['standard_no'],
            '条文号': c['clause_no'],
            '强制等级': c['mandatory_level'],
            '条文内容（摘要）': c['content'],
            '页码': c['page_no'],
            '引用标准': '; '.join(c['referenced_standards']),
        })
    df = pd.DataFrame(rows)
    excel_path = Path(pdf_path).with_suffix('.xlsx')
    df.to_excel(excel_path, index=False, engine='openpyxl')
    print(f"  [EXCEL] 已保存：{excel_path.name}")


def generate_spec_markdown(result: dict, md_path: Path):
    """生成规范 Markdown（供 Obsidian 查看）"""
    lines = []
    lines.append(f"# {result['standard_no'] or '未知规范'}\n")
    lines.append(f"**文件**：{result['document_name']}")
    lines.append(f"**总页数**：{result['total_pages']}")
    lines.append(f"**条文数**：{len(result['clauses'])}\n")
    lines.append("## 目录\n")
    for t in result['toc'][:30]:  # 只显示前30条目录
        lines.append(f"- **{t['clause_no']}** {t['title']}（第 {t['page']} 页）")
    lines.append("\n---\n")
    lines.append("## 条文列表\n")
    for c in result['clauses']:
        level_emoji = {'必须': '🔴', '严禁': '🔴', '应': '🟠', '不应': '🟠',
                        '不得': '🟠', '宜': '🟡', '不宜': '🟡', '可': '🟢'}.get(c['mandatory_level'], '⚪')
        lines.append(f"### {c['clause_no']} {level_emoji} {c['mandatory_level']}")
        lines.append(f"{c['content_full']}\n")
        if c['referenced_standards']:
            lines.append(f"> 引用标准：{'，'.join(c['referenced_standards'])}")
        lines.append("")

    md_path.write_text('\n'.join(lines), encoding='utf-8')


def distill_spec_clauses(result: dict, pdf_path: str):
    """对规范条文逐条蒸馏（调用 LLM）"""
    import os
    from pathlib import Path

    print(f"  [DISTILL] 开始蒸馏 {len(result['clauses'])} 条条文...")

    # 读取 LLM 配置（复用 pipeline.py 的 LLM_CONFIG）
    cfg = load_config()
    llm_cfg = cfg.get('llm_settings', {})
    api_url = llm_cfg.get('base_url', 'https://api.minimax.chat/v1')
    api_key = llm_cfg.get('api_key', '')
    model = llm_cfg.get('model', 'MiniMax-M2.7')

    if not api_key or api_key == 'your-key-here':
        print("  [WARN] LLM API Key 未配置，跳过蒸馏")
        return

    # 逐条蒸馏（批量处理，每批10条）
    distilled_dir = Path(r'D:\1052-OS\brain\distilled_spec')
    distilled_dir.mkdir(exist_ok=True)

    import requests
    headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}

    for i, clause in enumerate(result['clauses']):
        prompt = f"""请对以下工程规范条文进行6维认知蒸馏：

规范号：{result['standard_no']}
条文号：{clause['clause_no']}
强制等级：{clause['mandatory_level']}
条文内容：
{clause['content_full']}

请按以下格式输出：
## 事实层
（条文的核心事实信息）

## 方法层
（涉及的工程方法/计算方法，如无则写"无"）

## 洞见层
（这条条文背后的工程逻辑/设计哲学）

## 反常识层
（与其他规范/常识可能冲突的点，如无则写"无"）

## 适用边界
（适用条件/不适用场景）

## 置信度
（1-5分，依据充分度）
"""

        try:
            resp = requests.post(
                f"{api_url}/chat/completions",
                headers=headers,
                json={'model': model, 'messages': [{'role': 'user', 'content': prompt}], 'temperature': 0.3},
                timeout=30
            )
            if resp.status_code == 200:
                distilled = resp.json()['choices'][0]['message']['content']
                out_file = distilled_dir / f"{result['standard_no']}_{clause['clause_no'].replace('.', '_')}.md"
                out_file.write_text(f"# {result['standard_no']} {clause['clause_no']}\n\n{distilled}", encoding='utf-8')
        except Exception as e:
            print(f"    [ERROR] 条文 {clause['clause_no']} 蒸馏失败：{e}")

    print(f"  [DISTILL] 完成，输出目录：{distilled_dir}")


# ============ 新增：命令行参数（放在 args 解析区域）============
# 在 main() 函数的 args 解析部分新增：
#
#   parser.add_argument('--pdf-path', type=str, default=None,
#                       help='规范 PDF 文件路径（单文件模式）')
#   parser.add_argument('--pdf-dir', type=str, default=None,
#                       help='规范 PDF 文件夹路径（批量模式）')
#   parser.add_argument('--distill', action='store_true',
#                       help='是否对提取的条文进行 LLM 蒸馏')
#

# ============ 新增：mode 分支（放在 main() 的 mode 判断区域）============
# 在 main() 函数的 mode 分支中新增：
#
#   elif args.mode == 'spec-extract':
#       mode_spec_extract(args)
#

'''

# ============================================================
# 自动打补丁（将以上代码追加到 pipeline.py 末尾）
# ============================================================

def apply_patch():
    pipeline_path = r'D:\1052-OS\brain\pipeline.py'
    import os

    if not os.path.exists(pipeline_path):
        print(f"[ERROR] 找不到 {pipeline_path}")
        print("请手动将 SPEC_EXTRACT_CODE 中的代码合并到 pipeline.py")
        return False

    # 备份
    backup_path = pipeline_path + '.bak'
    import shutil
    shutil.copy2(pipeline_path, backup_path)
    print(f"[PATCH] 已备份原文件到：{backup_path}")

    # 追加代码
    with open(pipeline_path, 'a', encoding='utf-8') as f:
        f.write('\n\n' + '=' * 60 + '\n')
        f.write('# === PATCH: pdf-spec-extractor 集成（自动追加）===\n')
        f.write('=' * 60 + '\n\n')
        f.write(SPEC_EXTRACT_CODE)

    print(f"[PATCH] 已将补丁代码追加到：{pipeline_path}")
    print("\n[PATCH] 请手动完成以下两步：")
    print("  1. 在 pipeline.py 顶部 import 区域加上：")
    print("     try:")
    print("         import pdfplumber, pandas as pd")
    print('         SPEC_EXTRACT_AVAILABLE = True')
    print("     except ImportError:")
    print('         SPEC_EXTRACT_AVAILABLE = False')
    print("\n  2. 在 main() 的 args 解析区域加上 --pdf-path / --pdf-dir / --distill 参数")
    print("  3. 在 main() 的 mode 分支加上：")
    print("     elif args.mode == 'spec-extract':")
    print("         mode_spec_extract(args)")
    return True


def generate_standalone_script():
    """生成独立脚本 spec_extract.py（不修改 pipeline.py）"""
    script_path = r'D:\1052-OS\brain\spec_extract.py'
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(SPEC_EXTRACT_CODE)
    print(f"[STANDALONE] 已生成独立脚本：{script_path}")
    print(f"[STANDALONE] 运行方式：python {script_path} --pdf-dir D:/1052-OS/data/specs")


if __name__ == '__main__':
    import sys
    print("=" * 60)
    print("pdf-spec-extractor 集成补丁工具")
    print("=" * 60)
    print()
    print("选择集成方式：")
    print("  1. 自动追加到 pipeline.py（推荐，会自动备份）")
    print("  2. 生成独立脚本 spec_extract.py（不修改 pipeline.py）")
    print("  3. 仅显示补丁代码（手动合并）")
    print()

    choice = input("请输入 1/2/3：").strip()

    if choice == '1':
        apply_patch()
    elif choice == '2':
        generate_standalone_script()
    elif choice == '3':
        print("\n" + "=" * 60)
        print("补丁代码（复制到 pipeline.py 末尾）：")
        print("=" * 60)
        print(SPEC_EXTRACT_CODE)
    else:
        print("[ERROR] 无效选择")
