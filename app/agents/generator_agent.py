# app/agents/generator_agent.py
from crewai import Agent
from langchain_openai import ChatOpenAI

def create_generator_agent():
    llm = ChatOpenAI(
        model="gpt-4-0613",
        temperature=0
    )

    agent = Agent(
        name="Generator Agent",
        role="Insightful Writer",
        goal="Generate grounded answers using the retrieved context.",
        backstory="An AI known for insightful, well-written responses grounded in context.",
        tools=[],
        llm=llm,  # We can extract this for manual use
        verbose=True
    )

    return agent, llm
