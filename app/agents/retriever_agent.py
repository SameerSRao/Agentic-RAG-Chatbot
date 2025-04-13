from crewai import Agent
from langchain_openai import ChatOpenAI
from app.tools.gatsby_retriever_tool import GatsbyRetrieverTool

#creates retreiver agent: finds relevant chunks from Qdrant based on query
def create_retriever_agent():
    return Agent(
        role="Coffee Researcher",
        goal="Find passages from the articles about Coffee relevant to any question.",
        backstory="An AI literary detective with deep knowledge of Coffee.",
        tools=[GatsbyRetrieverTool()],
        llm=ChatOpenAI(model="gpt-4-0613", temperature=0),
        verbose=True
    )
