# Tools Module

This module contains modular tool implementations used by agents in the Agentic RAG Chatbot system. Each tool encapsulates a callable capability that extends an agent's ability to interact with external systems or apply specific evaluation logic.

Tools in CrewAI are autonomous and can be invoked by agents during planning and execution. They allow agents to remain stateless while leveraging well-defined functional capabilities.

---

## Tool Overview

| Tool Name              | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `gatsby_retriever_tool.py` | Retrieves semantically relevant passages from a Qdrant vector store.        |
| `deepeval_tool.py`     | Uses DeepEval metrics to evaluate generated answers against the query and context. |

---

## Tool Design Philosophy

Each tool extends the CrewAI `BaseTool` class and includes:

- **`name`**: The tool’s invocation name within the agent planner.
- **`description`**: What the tool does, used by the CrewAI planner to reason about tool selection.
- **`args_schema`**: A `pydantic` model that defines the expected input fields.
- **`_run()`**: The core method containing the tool’s execution logic.
- (Optional) **`_arun()`**: Placeholder for asynchronous usage (currently not implemented in this project).

---

## Tool Implementations

### `gatsby_retriever_tool.py`

A semantic search utility built on top of the `VectorStoreUtil`. It queries the Qdrant database and returns the top-k relevant text chunks.

**Key Features:**
- Uses pre-chunked and embedded data from *The Great Gatsby*.
- Encapsulates all retrieval logic, keeping agents clean.

### `deepeval_tool.py`
Evaluates a generated answer against both a baseline (ideal) answer and the retrieved context using DeepEval’s suite of metrics.

**Metrics Used:**
- **Answer Relevancy:** Does the answer directly address the user’s query?
- **Faithfulness:** Is the answer truthful to the given context?
- **Contextual Precision:** How precisely does the answer use the retrieved context?
- **Contextual Recall:** How completely does the answer use all relevant context?
- **Contextual Relevancy:** Are the used parts of context actually relevant?

Baseline Generation: Uses `ChatOpenAI` to generate the "ideal" answer for the query to use as `expected_output`.
