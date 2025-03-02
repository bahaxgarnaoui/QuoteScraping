import time

from tags_gemini import tag_generator_gemini

def tags_generator(quote_text):
    tags = []
    max_tries = 5
    ok = False
    while not ok and max_tries > 0:
        max_tries -= 1
        ok = True
        try:
            tags= tag_generator_gemini(quote_text)
            ok = True
        except:
            ok = False
            time.sleep(60)
    tags.insert(0, 'anime')
    return tags