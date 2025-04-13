from chonkie import SentenceChunker 
from sentence_transformers import SentenceTransformer
from app.config import QDRANT_PORT, QDRANT_URL
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import uuid

#chunks and embeds data source, populates vector db, searches db for relevant chunks
class VectorStoreUtil:
    def __init__(self, collection_name='rag_chunks', embedding_dimension=384):
        self.collection_name=collection_name
        self.chunker = SentenceChunker(
            tokenizer_or_token_counter="gpt2",  
            chunk_size=512,                     
            chunk_overlap=128,                
            min_sentences_per_chunk=1       
        )
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.client = QdrantClient(url=QDRANT_URL, port=QDRANT_PORT)
        self.embedding_dimension = embedding_dimension

    def recreate_collection(self):
        if self.client.collection_exists(self.collection_name):
            self.client.delete_collection(collection_name=self.collection_name)
        
        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(size=self.embedding_dimension, distance=Distance.COSINE),
        )
        
    def chunk_embed_store(self, doc_path):
        with open(doc_path, 'r', encoding='utf-8') as f:
            raw_text = f.read()
        chunks = self.chunker.chunk(raw_text)
        chunks = [chunk.text for chunk in chunks] 
        embeddings = self.model.encode(chunks).tolist()
        points = []
        for vec, chunk in zip(embeddings, chunks):
            points.append(PointStruct(id=str(uuid.uuid4()), vector=vec, payload={"text":chunk}))
        self.recreate_collection()
        self.client.upsert(collection_name=self.collection_name, points=points)

    def search(self, query, top_k=5):
        query_vector = self.model.encode([query])[0].tolist()
        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            limit=top_k
        )
        return [point.payload["text"] for point in results]
