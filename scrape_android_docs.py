#!/usr/bin/env python3
"""
Script para crear mirror de páginas de Android Developer Documentation
ADVERTENCIA: Este script es solo para uso educativo y personal.
Respeta los términos de servicio de Google y la licencia Creative Commons Attribution 2.5.
"""

import os
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from pathlib import Path
import html2text
import argparse
from collections import deque

# Configuración
BASE_URL = "https://developer.android.com"
OUTPUT_DIR = "docsMirror"
RATE_LIMIT_DELAY = 2  # segundos entre requests
MAX_PAGES = 100  # límite de páginas para evitar scraping masivo
USER_AGENT = "Mozilla/5.0 (Educational/Personal Documentation Mirror)"

class AndroidDocsScraper:
    def __init__(self, output_dir=OUTPUT_DIR, max_pages=MAX_PAGES, delay=RATE_LIMIT_DELAY):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.max_pages = max_pages
        self.delay = delay
        self.visited = set()
        self.to_visit = deque()
        self.html_converter = html2text.HTML2Text()
        self.html_converter.ignore_links = False
        self.html_converter.ignore_images = False
        self.html_converter.body_width = 0

        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': USER_AGENT
        })

    def is_valid_android_url(self, url):
        """Verifica si la URL pertenece a developer.android.com"""
        parsed = urlparse(url)
        return parsed.netloc == "developer.android.com"

    def get_file_path(self, url):
        """Convierte URL a ruta de archivo .md"""
        parsed = urlparse(url)
        path = parsed.path.strip('/')

        if not path:
            path = "index"

        # Remover parámetros de idioma
        path = path.replace('?hl=en', '')

        # Asegurar extensión .md
        if not path.endswith('.md'):
            path = f"{path}.md"

        return self.output_dir / path

    def fetch_page(self, url):
        """Obtiene el contenido de una página"""
        try:
            print(f"Fetching: {url}")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None

    def extract_links(self, html, base_url):
        """Extrae links de documentación de la página"""
        soup = BeautifulSoup(html, 'html.parser')
        links = set()

        # Buscar links en el contenido principal
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(base_url, href)

            # Solo incluir links de documentación válidos
            if self.is_valid_android_url(full_url):
                # Limpiar URL
                full_url = full_url.split('#')[0]  # Remover anclas
                full_url = full_url.split('?')[0]  # Remover query params
                if full_url not in self.visited:
                    links.add(full_url)

        return links

    def html_to_markdown(self, html, url):
        """Convierte HTML a Markdown"""
        soup = BeautifulSoup(html, 'html.parser')

        # Intentar extraer solo el contenido principal
        main_content = soup.find('main') or soup.find('article') or soup.find('div', class_='devsite-article-body')

        if main_content:
            content_html = str(main_content)
        else:
            content_html = html

        # Agregar metadatos
        title = soup.find('title')
        title_text = title.text.strip() if title else "Android Documentation"

        markdown = f"# {title_text}\n\n"
        markdown += f"**Source:** [{url}]({url})\n\n"
        markdown += "---\n\n"
        markdown += self.html_converter.handle(content_html)

        return markdown

    def save_page(self, url, html):
        """Guarda la página como archivo Markdown"""
        file_path = self.get_file_path(url)
        file_path.parent.mkdir(parents=True, exist_ok=True)

        markdown = self.html_to_markdown(html, url)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"Saved: {file_path}")

    def scrape(self, start_url):
        """Inicia el proceso de scraping"""
        print(f"Starting scraper...")
        print(f"Max pages: {self.max_pages}")
        print(f"Rate limit delay: {self.delay}s")
        print(f"Output directory: {self.output_dir}")
        print("\n" + "="*50 + "\n")

        self.to_visit.append(start_url)

        while self.to_visit and len(self.visited) < self.max_pages:
            url = self.to_visit.popleft()

            if url in self.visited:
                continue

            self.visited.add(url)

            # Respetar rate limiting
            time.sleep(self.delay)

            # Obtener página
            html = self.fetch_page(url)
            if not html:
                continue

            # Guardar página
            self.save_page(url, html)

            # Extraer y agregar nuevos links
            links = self.extract_links(html, url)
            for link in links:
                if link not in self.visited:
                    self.to_visit.append(link)

            print(f"Progress: {len(self.visited)}/{self.max_pages} pages scraped, {len(self.to_visit)} in queue\n")

        print("\n" + "="*50)
        print(f"Scraping completed. Total pages scraped: {len(self.visited)}")


def main():
    parser = argparse.ArgumentParser(
        description='Scrape Android Developer Documentation (Educational use only)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Scrape starting from main page (limited to 100 pages)
  python scrape_android_docs.py

  # Scrape specific section with custom limit
  python scrape_android_docs.py --url https://developer.android.com/guide --max-pages 50

  # Faster scraping (be respectful!)
  python scrape_android_docs.py --delay 1

IMPORTANT: This is for educational and personal use only.
Respect Google's terms of service and robots.txt.
        """
    )

    parser.add_argument(
        '--url',
        default=f"{BASE_URL}/?hl=en",
        help='Starting URL (default: Android Developer homepage)'
    )

    parser.add_argument(
        '--max-pages',
        type=int,
        default=MAX_PAGES,
        help=f'Maximum number of pages to scrape (default: {MAX_PAGES})'
    )

    parser.add_argument(
        '--delay',
        type=float,
        default=RATE_LIMIT_DELAY,
        help=f'Delay in seconds between requests (default: {RATE_LIMIT_DELAY})'
    )

    parser.add_argument(
        '--output',
        default=OUTPUT_DIR,
        help=f'Output directory (default: {OUTPUT_DIR})'
    )

    args = parser.parse_args()

    # Verificar dependencias
    try:
        import html2text
    except ImportError:
        print("Error: html2text not installed.")
        print("Install with: pip install html2text")
        return

    scraper = AndroidDocsScraper(
        output_dir=args.output,
        max_pages=args.max_pages,
        delay=args.delay
    )

    scraper.scrape(args.url)


if __name__ == "__main__":
    main()
