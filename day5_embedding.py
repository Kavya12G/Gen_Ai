"""An embedding is a numerical representation of data—usually text—where similar meanings tend 
to be represented by vectors that are close together in the embedding space."""

import numpy as np
import ollama


def embed(text):
    response = ollama.embed(
        model="nomic-embed-text",
        input=text
    )

    return response["embeddings"][0]


def cosine_similarity(a, b):

    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


text1 = "I love developing applications using Python"

text2 = "Python is my favorite programming language"

text3 = "I like eating pizza"


embedding1 = embed(text1)
embedding2 = embed(text2)
embedding3 = embed(text3)


print(
    "Python similarity:",
    cosine_similarity(embedding1, embedding2)
)


print(
    "Pizza similarity:",
    cosine_similarity(embedding1, embedding3)
)



# """-----------------------------------------------------------------------------------------------------
# "I love developing applications using Python"
#                      ↓
#                   embedding
#                      ↓
#                  Vector A

# "Python is my favorite programming language"
#                      ↓
#                   embedding
#                      ↓
#                  Vector B

# "I like eating pizza"
#                      ↓
#                   embedding
#                      ↓
#                  Vector C

# --------------------------------------------------------------------------------------------------------
# similarity(A, B)
#       ↓
#      high

# similarity(A, C)
#       ↓
#      lower"""