from crewai import Agent
from langchain_openai import ChatOpenAI
from app.tools.deepeval_tool import DeepEvalTool

def create_evaluator_agent():
    return Agent(
        role="Answer Evaluator",
        goal="Evaluate generated answers using DeepEvalTool for quality scoring.",
        backstory="An expert evaluator focused on relevance, faithfulness, and precision.",
        tools=[DeepEvalTool()],
        llm=ChatOpenAI(model="gpt-4-0613", temperature=0),
        verbose=True
    )
