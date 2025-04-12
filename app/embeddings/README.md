# Embeddings Module

This module manages semantic chunking, embedding, storage, and retrieval of document text using local embedding models and a Qdrant vector database. It is a critical component of the Agentic RAG Chatbot's information retrieval pipeline.

---

## Purpose

To split *The Great Gatsby* into overlapping, semantically meaningful chunks, encode them into dense vector embeddings, and store them in Qdrant. These embeddings enable semantic search for grounding LLM responses.

---

## File: `vectorstore.py`

### Class: `VectorStoreUtil`

This class encapsulates all logic related to document processing, vector generation, and Qdrant interactions.

### `__init__()`

- Initializes the Qdrant client.
- Loads a `SentenceTransformer` embedding model (`all-MiniLM-L6-v2`).
- Sets up a `SentenceChunker` using the `chonkie` library.
  
### `recreate_collection()`

- Deletes the collection (if it exists).
- Creates a fresh Qdrant collection using cosine similarity and the expected vector size.

Used before inserting new document embeddings to prevent duplicates.


### `chunk_embed_store()`
- Loads raw text from the given file.
- Splits it into overlapping chunks using `SentenceChunker`.
- Embeds each chunk using `SentenceTransformer`.
- Stores each vector + its text as a `PointStruct` in Qdrant.

### `search()`
- Encodes the query using the same embedding model.
- Searches the vector database for the most similar chunks.
- Returns the top matching text snippets.
