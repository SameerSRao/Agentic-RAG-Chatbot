# Agents

This directory defines the autonomous agents in the Agentic RAG Chatbot system. Each agent is implemented using the CrewAI `Agent` class and encapsulates a distinct role, goal, backstory, and optional toolset.

These agents form the foundation of the agentic pipeline, handling information retrieval, grounded answer generation, and evaluation. All agents are designed to be modular and reusable within different Crew configurations.

---

## Agents Overview

| File                   | Agent Role        | Description                                                                 |
|------------------------|-------------------|-----------------------------------------------------------------------------|
| `retriever_agent.py`   | Book Researcher   | Retrieves relevant passages from *The Great Gatsby* using semantic search. |
| `generator_agent.py`   | Literary Analyst  | Synthesizes a well-structured answer based on retrieved passages.          |
| `evaluator_agent.py`   | Answer Evaluator  | Evaluates the generated answer using DeepEval's scoring framework.         |

---

## Agent Design Philosophy

Each agent is defined using the following structure:
- **`role`**: Describes the agent’s functional responsibility.
- **`goal`**: Outlines the agent’s objective within the pipeline.
- **`backstory`**: Adds character and narrative to the agent for improved prompting and behavior.
- **`tools`** (optional): A set of tools the agent can invoke autonomously using CrewAI’s planner.

The agents communicate via CrewAI’s internal task orchestration mechanism and share intermediate outputs without manual piping.

---

## Implementation Strategy

- All agents use the `ChatOpenAI` LLM from the `langchain_openai` module with deterministic settings (temperature = 0) to ensure consistent behavior.
- Agents that require tools (e.g., `GatsbyRetrieverTool`, `DeepEvalTool`) import and register them for use in CrewAI’s action planner.
- Each agent is designed to be easily extended or swapped with alternate toolsets or LLM configurations.

---

## Modularity and Reusability

- Agents are **stateless** and **encapsulated**, which allows them to be reused in different crew or task configurations.
- Each agent is created through a factory function (`create_<role>_agent`) to make instantiation declarative and testable.
- Roles and goals are domain-specific, allowing seamless adaptation to other literary works or corpora.
