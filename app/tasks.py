from crewai import Task

def create_tasks(retriever, generator, query):
    retrieval_task = Task(
        description=f"Use the GatsbyRetriever tool to search for passages relevant to this question: '{query}'",
        expected_output="A list of text excerpts that directly relate to the question.",
        agent=retriever
    )

    generation_task = Task(
        description=f"Use the passages found by the retriever to write a clear, grounded answer to the question: '{query}'",
        expected_output="A concise, well-structured answer in paragraph form.",
        agent=generator
    )

    return [retrieval_task, generation_task]