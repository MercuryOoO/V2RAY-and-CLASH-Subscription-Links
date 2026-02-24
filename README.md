# CLASH-V2RAY-Subscription-Links

Collect lots of Clash & V2ray & Base64 subscription links from GitHub and public sources.

## Files
- `SUB LINKS`: source list (one URL per line, with section comments).
- `scripts/normalize_sub_links.py`: normalizes formatting and removes duplicate links.

## Usage
You can read raw links directly from `SUB LINKS`, or preprocess before consumption.

Example: output only URL lines.

```bash
rg '^https?://' 'SUB LINKS'
```

## Maintenance
Before committing updates to `SUB LINKS`, run:

```bash
python3 scripts/normalize_sub_links.py
```

This will:
- trim spaces,
- normalize section comment format,
- remove markdown bullets,
- deduplicate URLs while keeping first occurrence order.

## Risk notice
These links are collected from public sources. Availability, correctness, and safety are not guaranteed.
Please review and validate remote content before use.
