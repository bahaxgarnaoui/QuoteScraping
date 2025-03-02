from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.options import Options
import datetime
import uuid
import requests

from tags_gemini import tag_generator_gemini
from image_scraping_beautifulsoup import image_url_scraping
from replacer import parse_quote
from tags_generator import tags_generator

def scrape_anime_quotes(url):
    request = requests.get(url)
    """
        edge_options = Options()
    edge_options.add_argument('--headless=new')
    driver = webdriver.Edge(options=edge_options)
    
    # Navigate to the URL
    driver.get(url)
    html_content = driver.page_source
    driver.quit()
    """

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(request.content, 'lxml')
    
    # Find all paragraph elements
    quotes= soup.find_all('span', class_="bordered-description")
    #quotes = soup.find_all('p')
    
    data = []
    for quote in quotes:
        quote_text, quote_author, quote_source = parse_quote(quote.text)
        
        if quote_author and quote_source and quote_text:
            search_query = quote_author.replace(' ', '+') + "+" + quote_source.replace(' ', '+')
            image_url = image_url_scraping(search_query)
            if image_url:
                current_date = datetime.datetime.now()
                date_added = current_date.strftime("%Y-%m-%d %H:%M:%S")
                tags = tags_generator(quote_text)
                data.append({
                    'id': str(uuid.uuid4()),
                    'quote': quote_text,
                    'author': quote_author,
                    'source': quote_source,
                    'image_url': image_url,
                    'tags': tags,
                    'is_favorite': False
                })
    
    return data

