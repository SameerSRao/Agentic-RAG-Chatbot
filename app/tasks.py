from crewai import Task

def get_retrieval_task(agent, query):
    return Task(
        description=f"Use the GatsbyRetriever tool to find relevant passages for the question: '{query}'.",
        expected_output="A list of relevant text chunks from The Great Gatsby.",
        agent=agent
    )

def get_generation_task(agent, query):
    return Task(
        description=f"Using the context provided by the Retriever Agent, generate a clear, helpful answer to the question: '{query}'.",
        expected_output="A well-structured and insightful answer to the question, grounded in the context.",
        agent=agent
    )
