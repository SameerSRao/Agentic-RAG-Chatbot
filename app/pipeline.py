from crewai import Crew
from app.agents.retriever_agent import create_retriever_agent
from app.agents.generator_agent import create_generator_agent
from app.tasks import create_tasks

def run_pipeline(query: str):
    retriever = create_retriever_agent()
    generator = create_generator_agent()

    tasks = create_tasks(retriever, generator, query)

    crew = Crew(
        agents=[retriever, generator],
        tasks=tasks,
        verbose=True,
        planning=True
    )

    return crew.kickoff()
