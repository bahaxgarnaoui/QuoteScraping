import requests
from bs4 import BeautifulSoup
import random

def image_url_scraping(search_text):
    url = f"https://www.bing.com/images/search?q={search_text}&qft=+filterui:aspect-wide&form=IRFLTR&first=1"
    ok=False
    max_retries = 10
    while not ok and max_retries > 0:
        ok=True
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml')
            image_urls = [img.get('src') for img in soup.find_all('img', class_='mimg') if img.get('src')]
            if image_urls:
                image_url = random.choice(image_urls)
                return image_url
            else:
                ok=False
        else:
            ok=False
        max_retries -= 1
    return None