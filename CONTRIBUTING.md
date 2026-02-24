# Contributing

## SUB LINKS format
- One URL per line.
- Section headers use comment lines, e.g. `# CLASH`, `# v2ray`, `# other sites`.
- Do not use Markdown list markers (`*` / `-`) inside `SUB LINKS`.
- Keep only direct links when possible.

## Update workflow
1. Add or update sources in `SUB LINKS`.
2. Run normalization:
   ```bash
   python3 scripts/normalize_sub_links.py
   ```
3. Check diff and ensure no accidental non-URL content was added.
4. Commit with a clear message.
