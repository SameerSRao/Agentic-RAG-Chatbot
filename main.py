from app.embeddings.vectorstore import VectorStoreUtil
from app.pipeline import run_pipeline
import os

if __name__ == "__main__":
    
    # if adding new data, change collection_name in main.py and tools/gatsby_retreiver.py
    vs = VectorStoreUtil(collection_name="coffee-rag")
    if not os.path.exists("vectorstore_ready.flag"):
        print('Reading Documents...')
        vs.chunk_embed_store("app/data/docs/wikipedia.txt") #change to match document text file
        with open("vectorstore_ready.flag", "w") as f:
            f.write("ok")

    while True:
        print("\n===== Input =====")
        query = input("Ask a question about the document: ")
        result = run_pipeline(query)

        print("\n===== Query =====")
        print(query)
        print()

        print("\n===== Generated Answer =====")
        print(result['answer'].raw)
        print()

        print("\n===== Evaluation =====")
        print(result["evaluation"].raw)
        print()
