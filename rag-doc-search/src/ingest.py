# import requests
# from src.embed import embed_text

# BASE_URL = "http://localhost:8080"
# INDEX_NAME = "documents"

# # Create index
# requests.post(
#     f"{BASE_URL}/api/v1/index/create",
#     json={
#         "index_name": INDEX_NAME,
#         "dimension": 384
#     }
# )

# with open("data/sample_docs/docs.txt", "r", encoding="utf-8") as f:
#     docs = f.readlines()

# for i, doc in enumerate(docs):
#     vectors_payload = {
#         "index_name": INDEX_NAME,
#         "id": str(i),
#         "vector": embed_text(doc),
#         "metadata": {"text": doc.strip()}
#     }

#     requests.post(
#     f"{BASE_URL}/api/v1/index/{INDEX_NAME}/vector/insert",
#     json=vectors_payload
# )


# print("✅ Documents ingested into Endee")


# src/ingest.py

import requests
from src.embed import embed_text

BASE_URL = "http://localhost:8080"
INDEX_NAME = "documents"

with open("data/sample_docs/docs.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    text = line.strip()
    if not text:
        continue

    vector = embed_text(text)

    payload = {
        "id": f"doc_{i}",
        "vector": vector,
        "metadata": {
            "text": text
        }
    }

    requests.post(
        f"{BASE_URL}/api/v1/index/{INDEX_NAME}/insert",
        json=payload
    )

print("✅ All documents ingested")
