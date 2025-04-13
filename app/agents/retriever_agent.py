from crewai import Agent
from langchain_openai import ChatOpenAI
from app.tools.gatsby_retriever_tool import GatsbyRetrieverTool

#creates retreiver agent: finds relevant chunks from Qdrant based on query
def create_retriever_agent():
    return Agent(
        role="Book Researcher",
        goal="Find passages from The Great Gatsby relevant to any literary question.",
        backstory="An AI literary detective with deep knowledge of Gatsby.",
        tools=[GatsbyRetrieverTool()],
        llm=ChatOpenAI(model="gpt-4-0613", temperature=0),
        verbose=True
    )
