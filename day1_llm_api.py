"""1. LLM : Which application is using LLM(chatGPT or Gemini etc) as a brain to generate responses.
2. LLM API : A way for your application/code to communicate with an LLM to get responses."""

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)    

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="explain how to call llm api's",
)

print(response.text)


