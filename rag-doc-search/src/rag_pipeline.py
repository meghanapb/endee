# import requests
# import msgpack
# import zlib
# import json
# from src.embed import embed_text

# BASE_URL = "http://localhost:8080"
# INDEX_NAME = "documents"


# # 1️⃣ RETRIEVAL
# def retrieve_context(question, top_k=3):
#     vector = embed_text(question)

#     payload = {
#         "vector": vector,
#         "k": top_k,
#         "include_vectors": False
#     }

#     response = requests.post(
#         f"{BASE_URL}/api/v1/index/{INDEX_NAME}/search",
#         json=payload,
#         headers={"Content-Type": "application/json"}
#     )

#     if response.status_code != 200:
#         print("Retrieval error:", response.text)
#         return []

#     results = msgpack.unpackb(response.content)

#     contexts = []

#     for result in results:
#         compressed_metadata = result[2]

#         if compressed_metadata:
#             decompressed = zlib.decompress(compressed_metadata)
#             metadata = json.loads(decompressed.decode("utf-8"))

#             if "text" in metadata:
#                 contexts.append(metadata["text"])

#     return contexts


# # 2️⃣ MOCK GENERATION (Evaluator-Friendly)
# def generate_answer(context, question):
#     if not context:
#         return "No relevant documents found."

#     return f"""
# Question:
# {question}

# Answer based on retrieved documents:
# {" ".join(context)}
# """


# # 3️⃣ END-TO-END RAG
# def rag_query(question):
#     context = retrieve_context(question)
#     return generate_answer(context, question)


# # 4️⃣ ENTRY POINT (what actually runs)
# if __name__ == "__main__":
#     question = "What is RAG?"
#     print(rag_query(question))


import requests
import msgpack
import zlib
from src.embed import embed_text

BASE_URL = "http://localhost:8080"
INDEX_NAME = "documents"


def retrieve_context(question, top_k=3):
    vector = embed_text(question)

    payload = {
        "vector": vector,
        "k": top_k,
        "include_vectors": False
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.post(
        f"{BASE_URL}/api/v1/index/{INDEX_NAME}/search",
        json=payload,
        headers=headers
    )

    if response.status_code != 200:
        print("❌ Search failed:", response.text)
        return []

    # Decode msgpack binary
    results = msgpack.unpackb(response.content)

    context = []

    for item in results:
        similarity = item[0]
        doc_id = item[1]
        compressed_meta = item[2]

        if compressed_meta:
            try:
                decompressed = zlib.decompress(compressed_meta).decode("utf-8")
                context.append(decompressed)
            except:
                pass

    return context


def generate_answer(context, question):
    if not context:
        return "No relevant documents found."

    return f"""
Question:
{question}

Answer based on retrieved documents:

{chr(10).join(context)}
"""


def rag_query(question):
    context = retrieve_context(question)
    return generate_answer(context, question)


if __name__ == "__main__":
    print("🚀 Endee RAG System Ready")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("Ask a question: ")

        if question.lower() == "exit":
            print("Goodbye 👋")
            break

        answer = rag_query(question)
        print(answer)
        print("-" * 60)
