# app/pipeline.py
from app.agents.retriever_agent import create_retriever_agent
from app.agents.generator_agent import create_generator_agent
from app.embeddings.vectorstore import VectorStoreUtil

def run_agentic_pipeline(query: str):
    # Create agents
    retriever_agent = create_retriever_agent()
    generator_agent, llm = create_generator_agent()

    # Step 1: Manual context retrieval
    vs = VectorStoreUtil(collection_name="gatsby_rag")
    chunks = vs.search(query)
    context = "\n".join(chunks)

    # print("\n--- Retrieved Context ---")
    # print(context)

    # Step 2: Manually call the LLM with system/user prompt
    prompt = f"Use the following context to answer the question.\n\nContext:\n{context}\n\nQuestion: {query}"
    answer = llm.invoke(prompt)

    return answer
