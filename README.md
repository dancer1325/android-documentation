# Android Documentation

Personal notes of [Android Documentation](https://developer.android.com/?hl=en)

## documentation

* [here](docs)

## Scraper

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
# Scrape everything starting from the main page (no limit)
python scrape_android_docs.py

# Resume a previous session — already scraped URLs in scraped_urls.txt are skipped automatically
python scrape_android_docs.py

# Scrape a specific section
python scrape_android_docs.py --url https://developer.android.com/guide

# Limit the number of pages
python scrape_android_docs.py --max-pages 50

# Change the delay between requests (default: 2s)
python scrape_android_docs.py --delay 1

# Change the output directory (default: docsMirror/)
python scrape_android_docs.py --output my_folder
```

### Registry

Each scraped URL is appended to `scraped_urls.txt` immediately after being processed. On the next run, the script loads this file and skips any URL already in it. This means:

- Interrupted runs resume from where they left off
- Re-running the script only fetches pages not yet scraped

To force a full re-scrape, delete `scraped_urls.txt`.

### Options

| Argument | Default | Description |
|-----------|---------|-------------|
| `--url` | `https://developer.android.com/?hl=en` | Starting URL |
| `--max-pages` | `0` (unlimited) | Maximum number of pages to download |
| `--delay` | `2` | Seconds to wait between requests |
| `--output` | `docsMirror` | Output directory |

