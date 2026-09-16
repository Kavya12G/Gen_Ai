"""Tool calling: allows an LLM to decide when it needs an external function or service, 
generate the function name and structured arguments, and let the application execute that 
function and return the result to the model.

- 3 types of tool calling → a) your own function  b) built-in provider tools  c) MCP tools"""

from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
) 


# -------------------------
# 1. Actual Python function
# -------------------------

def get_temperature(location: str):

    print(f"Python function called for: {location}")

    return {
        "location": location,
        "temperature": 28,
        "unit": "Celsius"
    }


# -------------------------
# 2. Tell Gemini about it
# -------------------------

weather_tool = {
    "type": "function",
    "name": "get_temperature",
    "description": "Gets the current temperature for a location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name"
            }
        },
        "required": ["location"]
    }
}


# -------------------------
# 3. Ask Gemini
# -------------------------

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="What is the temperature in Bangalore?",
    config={
        "tools": [weather_tool]
    }
)


print(response)