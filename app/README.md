# App Module
The App module contains the core logic and structure of the project. It brings together agents, tools, tasks, and the execution pipeline. This module defines how different components interact, making the RAG chatbot system modular, organized, and easy to extend or modify.

## Design Philosophy
- Each major component of the system (agents, tools, embeddings, and pipeline logic) is modularized to encourage code reuse and make reasoning about behavior easier.
- Tasks are structured such that outputs from one agent (retriever) become the working context for another (generator, evaluator).
- New tasks, tools, and agents can be added easily without modifying existing modules. This supports ongoing experimentation and system improvement.

---

## Component Overviews

### `agents/`
Contains:
- `retriever_agent.py`: Uses a Qdrant-based tool to extract relevant text.
- `generator_agent.py`: Uses retrieved context to generate answers to query.
- `evaluator_agent.py`: Uses DeepEvalTool to score generated answers.

Each agent is configured with:
- A **goal** and **backstory**
- A set of **tools**
- `verbose=True` for clear tracing during runs

---

### `embeddings/`
Handles vector storage and similarity search:
- `vectorstore.py`: Uses `Chonkie` to chunk the input document, embeds with OpenAI, and stores into a Qdrant collection.

---

### `tools/`
Includes:
- `gatsby_retriever_tool.py`: Tool used by the retriever agent to query Qdrant.
- `deepeval_tool.py`: Tool used by the evaluator agent to run DeepEval metrics.

Tools inherit from `BaseTool` and define:
- A name and description
- `args_schema` for input validation
- `_run()` implementation to execute logic

---

### `tasks.py`
Defines CrewAI tasks such as:
- Retrieving context from the document
- Generating a grounded response
- Evaluating the generated output

Each task includes:
- A natural language description
- `expected_output`
- References to agents and context variables

---

### `pipeline.py`
Top-level function to:
- Create agents
- Create tasks
- Wire up a Crew
- Run kickoff()
- Collect structured output (answer, context, evaluation)

---

## Usage Flow

1. **Chunk + Embed** the document once via `main.py` or shell script.
2. **Run the pipeline** from `main.py`, which calls `run_pipeline()` inside `pipeline.py`.
3. The crew:
   - Retrieves relevant context
   - Generates a response
   - Evaluates it using DeepEval

---

## Extending This Module

- To add a new tool → create a new class in `tools/`
- To add a new agent → create a new file in `agents/`
- To experiment with evaluation metrics → edit `tools/deepeval_tool.py`
- To change the behavior of the pipeline → edit `pipeline.py`
