from crewai import Agent
from app.tools.gatsby_retriever_tool import GatsbyRetrieverTool

#creates retreiver agent: finds relevant chunks from Qdrant based on query
def create_retriever_agent():
    return Agent(
        role="Book Researcher",
        goal="Find passages from The Great Gatsby relevant to any literary question.",
        backstory="An AI literary detective with deep knowledge of Gatsby.",
        tools=[GatsbyRetrieverTool()],
        verbose=True
    )
