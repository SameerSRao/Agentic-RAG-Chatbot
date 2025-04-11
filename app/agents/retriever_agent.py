# app/agents/retriever_agent.py
from crewai import Agent

def create_retriever_agent():
    return Agent(
        name="Retriever Agent",
        role="Semantic Search Expert",
        goal="Find relevant context from the Gatsby vector DB",
        backstory="An expert literary researcher who understands semantic search and book structure.",
        tools=[],  # Not using CrewAI tools
        verbose=True
    )
