#!/usr/bin/env python3
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path('.')
SRC = ROOT / 'SUB LINKS'

url_re = re.compile(r"^https?://\S+$")

raw = SRC.read_text(encoding='utf-8').splitlines()
seen: set[str] = set()
out: list[str] = []

for line in raw:
    s = line.strip()
    if not s:
        # collapse multiple blank lines
        if out and out[-1] != '':
            out.append('')
        continue

    if s.startswith('#'):
        # normalize header spacing
        header = '# ' + s.lstrip('#').strip() if s != '#' else '#'
        if out and out[-1] == '':
            out.pop()
        out.append(header)
        out.append('')
        continue

    if s.startswith(('*', '-')):
        s = s[1:].strip()

    if url_re.match(s):
        if s not in seen:
            seen.add(s)
            out.append(s)
        continue

# trim trailing blanks
while out and out[-1] == '':
    out.pop()

SRC.write_text('\n'.join(out) + '\n', encoding='utf-8')
print(f'Wrote {len(out)} lines with {len(seen)} unique URLs')
