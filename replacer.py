import re
from  fill_missing_info import info_filler

numbers_first =r'[0-9]{1,3}\s*. \s*'
def parse_quote(quote_string):
    
    patterns= [
        #Pattern : "quote" - "author" , "source"
        r'(.*)\s*-\s*(.*),\s*(.*)',
        r'(.*)\s*—\s*(.*),\s*(.*)',
        r'(.*)\s*–\s*(.*),\s*(.*)',
        
        #Pattern : "quote" - "author" (source)
         r'(.*)\s*―\s*(.*?)\s*\((.*?)\)',
         r'(.*)\s*-\s*(.*?)\s*\((.*?)\)',
         r'(.*)\s*–\s*(.*?)\s*\((.*?)\)',
        
        #Pattern : "quote" - "author" from "source"
        r'(.*)\s*-\s*(.*)\s*From\s*(.*)',
        r'(.*)\s*—\s*(.*)\s*From\s*(.*)',
        r'(.*)\s*–\s*(.*)\s*From\s*(.*)',
           
        #Pattern : "quote" - "author" in "source"
        r'(.*)\s*-\s*(.*)in\s*(.*)',
        r'(.*)\s*—\s*(.*)in\s*(.*)',
        
    ]
    for pattern in patterns:
        match = re.match(pattern, quote_string)
        if match:
           try:
            quote = match.group(1).replace('"', "").replace("'","").replace('“', "").replace('”', "")
            author = match.group(2).replace('"', "").replace("'","").replace('“', "").replace('”', "").lower().title()
            anime = match.group(3).replace('"', "").replace("'","").replace('“', "").replace('”', "").lower().title()
            #author = info_filler(quote,anime).replace('"', "").replace("'","").replace('“', "").replace('”', "").lower().title()
            if len(quote) > 30 and len(author)<50 and len(anime)<50:
             return quote.strip(), author.strip(), anime.strip()
           except:
            print(quote_string)
            print("Failed to parse the quote string.")
            return None, None, None

    print(quote_string)
    print("Failed to parse the quote string.")
    return None, None, None





    
    """
            
                            # Example usage
quote_string = '“It’s just pathetic to give up on something before you even give it a shot.” - Reiko Mikami, Another'
parsed_quote = parse_quote(quote_string)

if parsed_quote:
    quote, author, anime = parsed_quote
    print(f"Quote: {quote}")
    print(f"Author: {author}")
    print(f"Anime: {anime}")
else:
    print("Failed to parse the quote string.")
    """

    
   

    
  

    
    

  





   


    
    


    
    


