from crewai import Task

def create_tasks(retriever, generator, evaluator, query):
    retrieval_task = Task(
        description=f"Use the GatsbyRetriever tool to search for passages relevant to this question: '{query}'",
        expected_output="A list of all the text excerpts that directly relate to the question.",
        agent=retriever
    )

    generation_task = Task(
        description=f"Use the passages found by the retriever to write a clear, grounded answer to the question: '{query}'",
        expected_output="A concise, well-structured answer in paragraph form.",
        agent=generator,
        context=[retrieval_task]
    )

    evaluation_task = Task(
        description="Evaluate the generated answer using DeepEvalTool with respect to the original question and context.",
        expected_output="Evaluation scores for answer relevancy, faithfulness, and contextual precision.",
        agent=evaluator,
        context=[retrieval_task, generation_task]
    )

    return retrieval_task, generation_task, evaluation_task
