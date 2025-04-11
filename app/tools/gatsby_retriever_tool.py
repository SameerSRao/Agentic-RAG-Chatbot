from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
from app.embeddings.vectorstore import VectorStoreUtil

class RetrievalInput(BaseModel):
    query: str = Field(..., description="The question to search in the Gatsby vector database.")

class GatsbyRetrieverTool(BaseTool):
    name: str = "gatsby_retriever"
    description: str = "Retrieves the most relevant passages from the Gatsby vector DB."
    args_schema: Type[BaseModel] = RetrievalInput

    def _run(self, query: str) -> str:
        vs = VectorStoreUtil(collection_name="gatsby_rag")
        return "\n".join(vs.search(query, top_k=5))
