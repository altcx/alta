import requests
from bs4 import BeautifulSoup
import random
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_page(url):
    """Fetch the HTML content of a webpage."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return None

def parse_articles(html, source):
    """Parse articles from the HTML content."""
    soup = BeautifulSoup(html, 'html.parser')
    articles = []

    if source == 'example_stem_site':
        for item in soup.select('.article-class'):  # Update with actual selectors
            title = item.select_one('.title-class').get_text(strip=True)
            link = item.select_one('a')['href']
            articles.append({'title': title, 'link': link, 'source': source})

    elif source == 'example_politics_site':
        for item in soup.select('.news-item-class'):  # Update with actual selectors
            title = item.select_one('.headline-class').get_text(strip=True)
            link = item.select_one('a')['href']
            articles.append({'title': title, 'link': link, 'source': source})

    return articles

def scrape_sources():
    """Scrape multiple sources for articles."""
    sources = {
        'example_stem_site': 'https://example.com/stem',
        'example_politics_site': 'https://example.com/politics'
    }

    all_articles = []

    for source, url in sources.items():
        logging.info(f"Scraping {source}...")
        html = fetch_page(url)
        if html:
            articles = parse_articles(html, source)
            all_articles.extend(articles)

        # Random delay to avoid detection
        time.sleep(random.uniform(1, 3))

    return all_articles

def main():
    """Main function to run the scraper."""
    articles = scrape_sources()
    logging.info(f"Scraped {len(articles)} articles.")
    for article in articles:
        logging.info(f"{article['title']} - {article['link']} ({article['source']})")

if __name__ == '__main__':
    main()
