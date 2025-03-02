import json
from fuzzywuzzy import fuzz

def remove_similar_quotes(quotes, threshold=90):
    unique_quotes = []
    for quote in quotes:
        if not any(fuzz.ratio(quote['quote'], q['quote']) > threshold for q in unique_quotes):
            unique_quotes.append(quote)
    return unique_quotes

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def main():
    file_path = "./anime_quotes_filtered.json"
    quotes = load_json_file(file_path)
    
    unique_quotes = remove_similar_quotes(quotes)
    print(len(quotes))
    print(len(unique_quotes))
    # Optionally, save the unique quotes back to a JSON file
    with open('unique_quotes.json', 'w') as file:
        json.dump(unique_quotes, file, indent=4)

if __name__ == "__main__":
    main()