import google.generativeai as genai
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
def tag_generator_gemini(quote):
  chat_session = model.start_chat()

  response = chat_session.send_message(
      f"generate 5 one worded tags as array from this quote, get creative while doing it and don't use any of these tags [quote,motivation,anime]  {quote} ",
      )
  return eval(response.text)

print(tag_generator_gemini("Human strength lies in the ability to change yourself."))