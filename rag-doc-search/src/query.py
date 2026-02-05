import requests
import msgpack
import zlib
from src.embed import embed_text

BASE_URL = "http://localhost:8080"
INDEX_NAME = "documents"

query = "What is RAG?"

payload = {
    "vector": embed_text(query),
    "k": 2,
    "include_vectors": False
}

response = requests.post(
    f"{BASE_URL}/api/v1/index/{INDEX_NAME}/search",
    json=payload
)

print("Status Code:", response.status_code)

if response.status_code == 200:
    results = msgpack.unpackb(response.content)

    print("\n🔍 Search Results:\n")

    for r in results:
        score, doc_id, compressed_text, meta, _, _ = r

        if compressed_text:
            text = zlib.decompress(compressed_text).decode("utf-8")
        else:
            text = "(empty)"

        print(f"📄 ID: {doc_id}")
        print(f"⭐ Similarity: {score}")
        print(f"📝 Content: {text}")
        print("-" * 50)
else:
    print("Error:", response.text)
