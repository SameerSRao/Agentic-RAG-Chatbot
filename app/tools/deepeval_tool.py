from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type, List
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric, ContextualPrecisionMetric, ContextualRecallMetric, ContextualRelevancyMetric
from langchain_openai import ChatOpenAI

#generates expected_output based on ChatGPT4 answer using the user question
def generate_baseline(query: str) -> str:
    llm = ChatOpenAI(model="gpt-4-0613", temperature=0)
    prompt = (
        f"Please provide the ideal, best answer to the following question based on The Great Gatsby:\n"
        f"Question: {query}\n"
        "Answer in a clear and concise paragraph."
    )
    response = llm.invoke(prompt)
    return response.content 


#input for DeepEval tool
class DeepEvalInput(BaseModel):
    query: str = Field(..., description="The user question")
    answer: str = Field(..., description="The generated answer")
    context: List[str] = Field(..., description="List of retrieved context strings")

#runs DeepEval metrics on the generated answer
class DeepEvalTool(BaseTool):
    name: str = "DeepEvalTool"
    description: str = "Evaluates an LLM answer using DeepEval metrics."
    args_schema: Type[BaseModel] = DeepEvalInput

    def _run(self, query: str, answer: str, context: str = "") -> str:
        expected_output = generate_baseline(query)
        
        test_case = LLMTestCase(
            input=query,
            actual_output=answer,
            retrieval_context=context,
            expected_output=expected_output
        )

        metrics = [
            AnswerRelevancyMetric(include_reason=True),
            FaithfulnessMetric(include_reason=True),
            ContextualPrecisionMetric(include_reason=True),
            ContextualRecallMetric(include_reason=True),
            ContextualRelevancyMetric(include_reason=True),
        ]

        metric_names = [
            'Answer Relevancy',
            'Faithfulness',
            'Contextual Precision',
            'Contextual Recall',
            'Contextual Relevancy'
        ]

        results = []
        for metric, name in zip(metrics, metric_names):
            score = metric.measure(test_case)
            results.append(f"{name}: {round(score * 100, 2)}%")

        return "\n".join(results)
