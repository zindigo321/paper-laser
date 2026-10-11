#!/usr/bin/env python3
"""Offline integrity checks for the literature repository; standard library only."""
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


def main():
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / 'source_manifest.json').read_text(encoding='utf-8'))
    papers = manifest['papers']
    errors = []
    warnings = []
    link_count = page_count = table_count = math_count = diagram_count = 0
    external = set()
    if len(papers) != 7:
        errors.append('Expected seven papers in this collection.')
    published = [p for p in papers if p.get('pdf_in_repository', True)]
    if manifest.get('distribution_mode') == 'public-licensed-pdfs':
        if manifest.get('required_visibility') != 'public':
            errors.append('Public release has inconsistent visibility metadata.')
        if len(published) != manifest.get('published_pdf_count'):
            errors.append('Published PDF count does not match manifest.')
        allowed_files = {root / p['directory'] / 'paper.pdf' for p in published}
        for pdf in root.rglob('*.pdf'):
            if pdf not in allowed_files:
                errors.append(f'PDF outside approved public set: {pdf.relative_to(root)}')
    pdf_pages = {}
    for paper in papers:
        directory = root / paper['directory']
        include_pdf = paper.get('pdf_in_repository', True)
        required = ('notes.md', 'citation.bib', 'paper.pdf' if include_pdf else 'source.md')
        for name in required:
            if not (directory / name).is_file():
                errors.append(f'Missing {paper["directory"]}/{name}')
        pdf = directory / 'paper.pdf'
        if not include_pdf and pdf.exists():
            errors.append(f'Unapproved PDF in public repository: {pdf.relative_to(root)}')
        if not include_pdf:
            source = directory / 'source.md'
            pdf_pages[source.resolve()] = paper['pdf_pages']
            if source.exists():
                content = source.read_text(encoding='utf-8')
                for page in range(1, paper['pdf_pages'] + 1):
                    if f'### PDF page {page}\n' not in content:
                        errors.append(f'Missing source page anchor: {source.relative_to(root)}: {page}')
        if pdf.is_file():
            raw = pdf.read_bytes()
            if not raw.startswith(b'%PDF-'):
                errors.append(f'Invalid PDF header: {pdf.relative_to(root)}')
            if len(raw) != paper['pdf_bytes']:
                errors.append(f'PDF size mismatch: {pdf.relative_to(root)}')
            if hashlib.sha256(raw).hexdigest() != paper['pdf_sha256']:
                errors.append(f'PDF SHA-256 mismatch: {pdf.relative_to(root)}')
            pdf_pages[pdf.resolve()] = paper['pdf_pages']
        bib_path = directory / 'citation.bib'
        if bib_path.exists():
            bib = bib_path.read_text(encoding='utf-8')
            if len(re.findall(r'@article\{', bib)) != 1:
                errors.append(f'Expected one BibTeX article in {bib_path.relative_to(root)}')
            for field, value in (('title',paper['title']), ('year',str(paper['year'])), ('doi',paper['doi'])):
                if f'{field} = {{{value}}}' not in bib:
                    errors.append(f'BibTeX {field} mismatch: {bib_path.relative_to(root)}')
            if bib.count('{') != bib.count('}'):
                errors.append(f'Unbalanced BibTeX braces: {bib_path.relative_to(root)}')
    combined = (root / 'references.bib').read_text(encoding='utf-8')
    if len(re.findall(r'@article\{', combined)) != len(papers):
        errors.append('Combined bibliography entry count mismatch.')
    expected_checksums = ''.join(p['pdf_sha256']+'  '+p['directory']+'/paper.pdf\n' for p in published)
    if (root/'checksums.sha256').read_text(encoding='ascii') != expected_checksums:
        errors.append('Checksum list does not match manifest.')

    documents = sorted(root.rglob('*.md'))
    for document in documents:
        if '.git' in document.parts:
            continue
        text = document.read_text(encoding='utf-8')
        rel = str(document.relative_to(root))
        fence_open = False
        fence_math = False
        math_open = False
        table_width = None
        math_parts = []
        current_math = []
        for line_num, line in enumerate(text.splitlines(),1):
            if line.lstrip().startswith('```'):
                if fence_open and fence_math:
                    math_parts.append('\n'.join(current_math))
                    current_math = []
                fence_math = not fence_open and line.strip() == '```math'
                fence_open = not fence_open
                if fence_math:
                    math_count += 1
                if fence_open and line.strip() == '```mermaid':
                    diagram_count += 1
                table_width = None
                continue
            if fence_open:
                if fence_math:
                    current_math.append(line)
                continue
            if line.strip() == '$$':
                if math_open:
                    math_parts.append('\n'.join(current_math))
                    current_math = []
                math_open = not math_open
                if math_open:
                    math_count += 1
                continue
            if math_open:
                current_math.append(line)
                continue
            no_code = re.sub(r'`[^`]*`','',line)
            if len(re.findall(r'(?<!\\)\$', no_code)) % 2:
                errors.append(f'Unpaired inline math dollar: {rel}:{line_num}')
            if line.startswith('|') and line.endswith('|'):
                cells = re.split(r'(?<!\\)\|',line)[1:-1]
                if table_width is None:
                    table_width = len(cells)
                    table_count += 1
                elif len(cells) != table_width:
                    errors.append(f'Table column count mismatch: {rel}:{line_num}')
            else:
                table_width = None
        if fence_open:
            errors.append(f'Unclosed code fence: {rel}')
        if math_open:
            errors.append(f'Unclosed display math block: {rel}')
        for expr in math_parts:
            cleaned = re.sub(r'\\[{}]','',expr)
            if cleaned.count('{') != cleaned.count('}'):
                errors.append(f'Unbalanced math braces: {rel}')
            if len(re.findall(r'\\left\b',expr)) != len(re.findall(r'\\right\b',expr)):
                errors.append(f'Unbalanced left/right delimiters: {rel}')

        for _, target in re.findall(r'\[([^\]]*)\]\(([^\s)]+)\)', text):
            parsed = urlsplit(target)
            if parsed.scheme in ('http','https'):
                if not parsed.netloc:
                    errors.append(f'Invalid external URL: {rel}: {target}')
                external.add(target)
                continue
            if parsed.scheme:
                errors.append(f'Unsupported URI scheme: {rel}: {target}')
                continue
            if not parsed.path:
                continue
            resolved = (document.parent / unquote(parsed.path)).resolve()
            if root.resolve() not in resolved.parents and resolved != root.resolve():
                errors.append(f'Link leaves repository: {rel}: {target}')
                continue
            link_count += 1
            if not resolved.exists():
                errors.append(f'Broken local link: {rel}: {target}')
                continue
            match = re.fullmatch(r'page=(\d+)|pdf-page-(\d+)', parsed.fragment)
            if match:
                page_count += 1
                page = int(match[1] or match[2])
                if resolved not in pdf_pages or not 1 <= page <= pdf_pages[resolved]:
                    errors.append(f'Out-of-range PDF page: {rel}: {target}')
                if match[2] and resolved.is_file():
                    if f'### PDF page {page}\n' not in resolved.read_text(encoding='utf-8'):
                        errors.append(f'Missing source page anchor: {rel}: {target}')
        if re.search(r'github_pat_[A-Za-z0-9_]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|\bsk-[A-Za-z0-9]{25,}',text):
            errors.append(f'Possible credential detected in {rel}')

    for paper in published:
        pdf = root/paper['directory']/'paper.pdf'
        try:
            from pypdf import PdfReader
        except ImportError:
            warnings.append('pypdf unavailable: PDF page totals trusted from original extraction manifest; hashes verified.')
            break
        if len(PdfReader(pdf).pages) != paper['pdf_pages']:
            errors.append(f'PDF parsed page count mismatch: {pdf.relative_to(root)}')

    result = dict(
        ok=not errors,
        paper_count=len(papers),
        pdf_count=len(list((root/'papers').rglob('paper.pdf'))),
        notes_count=len(list((root/'papers').rglob('notes.md'))),
        per_paper_bib_count=len(list((root/'papers').rglob('citation.bib'))),
        markdown_documents=len(documents),
        checked_local_links=link_count,
        checked_pdf_page_links=page_count,
        tables=table_count,
        display_math_blocks=math_count,
        mermaid_diagrams=diagram_count,
        external_urls=sorted(external),
        errors=errors,
        warnings=warnings,
        limits='Offline structural checks do not verify publisher access, live GitHub rendering, TeX semantic equivalence, or remote push.',
    )
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0 if not errors else 1


if __name__ == '__main__':
    sys.exit(main())
