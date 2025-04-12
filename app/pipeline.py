from crewai import Crew
from app.agents.retriever_agent import create_retriever_agent
from app.agents.generator_agent import create_generator_agent
from app.agents.evaluator_agent import create_evaluator_agent
from app.tasks import create_tasks

def run_pipeline(query: str):
    retriever = create_retriever_agent()
    generator = create_generator_agent()
    evaluator = create_evaluator_agent()

    retrieval_task, generation_task, evaluation_task = create_tasks(retriever, generator, evaluator, query)

    crew = Crew(
        agents=[retriever, generator, evaluator],
        tasks=[retrieval_task, generation_task, evaluation_task],
        verbose=True,
        planning=True
    )

    crew.kickoff()

    return {
        "answer": generation_task.output,
        "context": retrieval_task.output,
        "evaluation": evaluation_task.output
    }
