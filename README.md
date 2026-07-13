# Android Documentation
Personal notes of [Android Documentation](https://developer.android.com/?hl=en)

## Scraper

Script to create a local Markdown mirror of Android Developer Documentation pages.

> ⚠️ For educational and personal use only. Respect Google's terms of service and the Creative Commons Attribution 2.5 license.

### Requirements

- Python 3.x

### Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Dependencies:
- `requests` — HTTP requests
- `beautifulsoup4` — HTML parsing
- `html2text` — HTML → Markdown conversion
- `lxml` — XML/HTML parser

### Usage

```bash
# Scrape from the main page (limited to 100 pages by default)
python scrape_android_docs.py

# Scrape a specific section with a custom limit
python scrape_android_docs.py --url https://developer.android.com/guide --max-pages 50

# Change the delay between requests (default: 2s)
python scrape_android_docs.py --delay 1

# Change the output directory (default: docsMirror/)
python scrape_android_docs.py --output my_folder
```

### Options

| Argument | Default | Description |
|-----------|---------|-------------|
| `--url` | `https://developer.android.com/?hl=en` | Starting URL |
| `--max-pages` | `100` | Maximum number of pages to download |
| `--delay` | `2` | Seconds to wait between requests |
| `--output` | `docsMirror` | Output directory |

