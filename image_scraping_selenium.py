from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

def image_url_scraping(search_text):
    # Set up the WebDriver options for headless mode
    edge_options = Options()
    edge_options.add_argument('--headless=new')

    # Initialize the WebDriver
    driver = webdriver.Edge(options=edge_options)

    # Navigate to the Bing image search page
    url = f"https://www.bing.com/images/search?q={search_text}&qft=+filterui:aspect-wide&form=IRFLTR&first=1"
    driver.get(url)

   # Wait for the images to load
    images = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'mimg'))
    )


    # Extract image URLs directly from Selenium elements
    image_elements = driver.find_elements(By.CLASS_NAME, 'mimg')
    image_urls = [img.get_attribute('src') for img in image_elements if img.get_attribute('src')]

    # Close the WebDriver
    driver.quit()
    
    if image_urls:
        image_url = random.choice(image_urls)
        for img in image_urls:
            print(img)
        print(len(image_urls))
        return image_url
    else:
        print("No image URLs found.")
        return None

image_url_scraping("luffy")
    
"""
    
        while image_urls:
        if image_processing(image_url):
            return image_url
        image_urls.remove(image_url)
        if image_urls:
            image_url = random.choice(image_urls)
    """