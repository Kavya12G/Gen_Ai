"""BASIC chatbot for understanding"""

from openai import OpenAI

# Point to local Ollama (or cloud provider)
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

# Set systemic behavior and initialize chat memory
messages = [
    {"role": "system", "content": "You are a helpful, concise assistant."}
]

print("Chatbot initialized! Type 'exit' or 'quit' to stop.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    # 1. Append user input to history
    messages.append({"role": "user", "content": user_input})

    # 2. Call local model with full conversation history
    response = client.chat.completions.create(
        model="llama3.2",
        messages=messages,
        stream=True
    )

    print("Bot: ", end="", flush=True)
    full_bot_response = ""

    # 3. Stream output back to terminal
    for chunk in response:
        content = chunk.choices[0].delta.content or ""
        print(content, end="", flush=True)
        full_bot_response += content

    print("\n")

    # 4. Save assistant response into memory for next turn
    messages.append({"role": "assistant", "content": full_bot_response})