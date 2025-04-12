## Architecture Overview

### High-Level Flow

```text
[User Query]
     │
     ▼
[Retriever Agent]
     └── uses Qdrant vector DB to fetch top-k chunks
     │
     ▼
[Generator Agent]
     └── generates an answer grounded in retrieved context
     │
     ▼
[Evaluator Agent]
     └── uses DeepEvalTool to evaluate the output
     │
     ▼
[Final Output]
     └── includes: Answer and Evaluation Scores
```

## Agents & Roles

| Agent           | Role               | Tool(s) Used          | Description                                               |
|----------------|--------------------|------------------------|-----------------------------------------------------------|
| RetrieverAgent | Book Researcher     | `GatsbyRetrieverTool` | Fetches relevant context from Qdrant vector database      |
| GeneratorAgent | Literary Analyst    | (no tool)              | Uses context to generate a grounded, well-written answer  |
| EvaluatorAgent | Answer Evaluator    | `DeepEvalTool`        | Evaluates the answer using DeepEval metrics               |


