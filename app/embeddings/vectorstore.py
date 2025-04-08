from chonkie import SentenceChunker 
from sentence_transformers import SentenceTransformer

def chunk(doc_path):
    chunker = SentenceChunker(
        tokenizer_or_token_counter="gpt2",     # Supports string identifiers
        chunk_size=512,                        # Maximum tokens per chunk
        chunk_overlap=128,                     # Overlap between chunks
        min_sentences_per_chunk=1              # Minimum sentences in each chunk
    )

    model = SentenceTransformer("all-MiniLM-L6-v2")

    with open(doc_path, 'r', encoding='utf-8') as f:
        raw_text = f.read()
    
    chunks = chunker.chunk(raw_text)
    embeddings = model.encode(chunks)



if __name__ == "__main__":
    chunk('../data/docs/great_gatsby.text')
