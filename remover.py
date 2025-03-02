import json

# Function to filter and process quotes
def process_quotes(quotes):
    # Remove 'date_added' and 'is_favorite' properties from each quote
    for quote in quotes:
        if 'is_favorite' in quote:
            del quote['is_favorite']
    
    # Filter quotes based on conditions
    filtered_quotes = [quote for quote in quotes if len(quote['quote']) >= 30 and len(quote['author']) <= 50 and len(quote['source']) <= 50]

    # Separate the first tag from the tags list
    for quote in filtered_quotes:
        if quote['tags']:
            quote['genre'] = quote['tags'][0]
            quote['tags'] = quote['tags'][1:]

    return filtered_quotes

# Read JSON file
def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return []
    except json.JSONDecodeError:
        print(f"Failed to parse JSON in file {file_path}.")
        return []

# Write JSON data to file
def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Main function
def main():
    
    input_file_path = './anime_quotes.json'  # Replace with your input JSON file path
    output_file_path = './anime_quotes_filtered.json'  # Replace with your desired output JSON file path

    # Read JSON data from file
    quotes = read_json_file(input_file_path)

    # Process and filter quotes
    filtered_quotes = process_quotes(quotes)

    # Write filtered data to output file
    write_json_file(output_file_path, filtered_quotes)

if __name__ == "__main__":
    main()