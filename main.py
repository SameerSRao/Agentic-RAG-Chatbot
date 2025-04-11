from app.embeddings.vectorstore import VectorStoreUtil
from app.pipeline import run_pipeline
import os

if __name__ == "__main__":
    vs = VectorStoreUtil(collection_name="gatsby_rag")
    if not os.path.exists("vectorstore_ready.flag"):
        vs.chunk_embed_store("app/data/docs/great_gatsby.txt")
        with open("vectorstore_ready.flag", "w") as f:
            f.write("ok")

    while True:
        query = input("Ask a question about the Great Gatsby: ")
        result = run_pipeline(query)

        print("\n--- Answer ---")
        print(result)
        print()
