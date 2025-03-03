import google.generativeai as genai
import time
import os
api_key = os.getenv("GEMINI_API_KEY")

if api_key is None:
    raise ValueError("API key not found. Set the GOOGLE_GENAI_API_KEY environment variable.")
genai.configure(api_key=api_key) 
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)
def info_filler_gemini(info, anime):
  chat_session = model.start_chat()

  response = chat_session.send_message(
      f"who said this quote? {info} from anime {anime} respond with the name of the author only",
      )
  return response.text


def info_filler(info_text,source):
    max_tries = 5
    ok = False
    while not ok and max_tries > 0:
        max_tries -= 1
        ok = True
        try:
            info= info_filler_gemini(info_text,source)
            ok = True
        except:
            ok = False
            time.sleep(60)
    return info