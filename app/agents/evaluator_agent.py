from crewai import Agent
from app.tools.deepeval_tool import DeepEvalTool

#creates evaluator agent: evaluates generated answer with DeepEval
def create_evaluator_agent():
    return Agent(
        role="Answer Evaluator",
        goal="Evaluate generated answers using DeepEvalTool for quality scoring.",
        backstory="An expert evaluator focused on relevance, faithfulness, and precision.",
        tools=[DeepEvalTool()],
        verbose=True
    )
