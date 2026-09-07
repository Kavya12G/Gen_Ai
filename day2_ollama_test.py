""" Ollama is a tool/runtime that allows developers to run Large Language Models (LLMs) 
locally on their own computer or server, without depending on a cloud-based LLM API."""

# #generate api(simple text msg)
# import requests

# url = "http://localhost:11434/api/generate"

# data = {
#     "model": "llama3.2:latest",
#     "prompt": "Explain what an API is in one simple sentence.",
#     "stream": False
# }

# response = requests.post(url, json=data)

# print("Status:", response.status_code)
# print("Response:", response.json()["response"])

# #--------------------------------------------------------------------------------------------------------
# #chat api(conversation with multiple messages)
# import requests

# response = requests.post(
#     "http://localhost:11434/api/chat",
#     json={
#         "model": "llama3.2:latest",
#         "messages": [
#             {
#                 "role": "user",
#                 "content": "What is Python?"
#             },
#             {
#                 "role": "user",
#                 "content": "benefits?"
#             }
#         ],
#         "stream": False
#     }
# )

# print(response.json()["message"]["content"])

#-------------------------------------------------------------------------------------------------------------------
# #tags api(you can see installed models)
# import requests

# response = requests.get(
#     "http://localhost:11434/api/tags"
# )

# print(response.json())

#------------------------------------------------------------------------------------------------------------
# #show api(get information about a specific model)
# import requests

# response = requests.post(
#     "http://localhost:11434/api/show",
#     json={
#         "name": "llama3.2:latest"
#     }
# )

# print(response.json())

#--------------------------------------------------------------------------------------------------------------
# #pull api(download a model from api)
# import requests

# response = requests.post(
#     "http://localhost:11434/api/pull",
#     json={
#         "model": "llama3.2:latest"
#     }
# )

# print(response.text))

#-----------------------------------------------------------------------------------------------------
# #delete api(delete locally installed model)
# import requests

# response = requests.delete(
#     "http://localhost:11434/api/delete",
#     json={
#         "model": "llama3.2:latest"
#     }
# )

# print(response.status_code)

#------------------------------------------------------------------------------------------------------
# #embed api(generate embedding for a text)
# import requests

# response = requests.post(
#     "http://localhost:11434/api/embed",
#     json={
#         "model": "your-embedding-model",
#         "input": "What is Python?"
#     }
# )

# print(response.json())

#-----------------------------------------------------------------------------------------------------------
#embeddings(An embedding converts text into a list of numbers (vector) that represents the meaning of the text)
