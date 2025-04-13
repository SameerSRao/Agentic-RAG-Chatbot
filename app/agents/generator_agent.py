from crewai import Agent

#creates generator agent: generates answer based on context from retreiver agent
def create_generator_agent():
    return Agent(
        role="Coffee Analyst",
        goal="Answer questions based on the Coffee articles with insight and clarity.",
        backstory="A thoughtful AI with a background in coffee.",
        tools=[],
        verbose=True
    )
