from web_scraping import scrape_anime_quotes
from data_saver import save_data_to_json
import time

def main():
    url="https://www.boredpanda.com/anime-quotes/"
    data = scrape_anime_quotes(url)
    save_data_to_json(data, './anime_quotes_10.json')

if __name__ == "__main__":
    start_time = time.time()
    print("Start time: ", time.ctime())
    main()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {int(execution_time//60)} minutes and {int(execution_time%60)} seconds")