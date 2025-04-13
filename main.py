from app.embeddings.vectorstore import VectorStoreUtil
from app.pipeline import run_pipeline
import os

if __name__ == "__main__":
    vs = VectorStoreUtil(collection_name="gatsby_rag")
    if not os.path.exists("vectorstore_ready.flag"):
        print('Reading Documents...')
        vs.chunk_embed_store("app/data/docs/great_gatsby.txt")
        with open("vectorstore_ready.flag", "w") as f:
            f.write("ok")

    while True:
        print("\n===== Input =====")
        query = input("Ask a question about the Great Gatsby: ")
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
