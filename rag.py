from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct
from config import QDRANT_HOST, COLLECTION_NAME, EMBEDDING_MODEL_NAME
import os

#Initialize SentenceTransformer and Qdrant client
embedder = SentenceTransformer(EMBEDDING_MODEL_NAME)
qdrant = QdrantClient(url=QDRANT_HOST)

#Ensure the Qdrant collection exists
def ensure_collection():
    if COLLECTION_NAME not in [c.name for c in qdrant.get_collections().collections]:
        qdrant.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE)
        )

#Embed content from .txt and .md documents into Qdrant
def embed_documents(file_paths):
    docs = []
    for path in file_paths:
        try:
            if path.endswith(('.txt', '.md')):  # Add '.pdf', '.docx' support later
                with open(path, 'r', encoding='utf-8') as f:
                    docs.append((os.path.basename(path), f.read()))
        except Exception as e:
            print(f"❌ Error reading file {path}: {e}")

    if not docs:
        raise ValueError("No valid text documents found to embed.")

    vectors = embedder.encode([content for _, content in docs]).tolist()
    points = [
        PointStruct(id=i, vector=vectors[i], payload={"doc": docs[i][1]})
        for i in range(len(docs))
    ]
    qdrant.upsert(collection_name=COLLECTION_NAME, points=points)

#Retrieve top matching context snippets from Qdrant
def retrieve_context(text):
    vector = embedder.encode([text])[0].tolist()
    hits = qdrant.search(collection_name=COLLECTION_NAME, query_vector=vector, limit=2)
    return "\n\n".join(hit.payload["doc"] for hit in hits if "doc" in hit.payload)
