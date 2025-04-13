# Agents Module

This module defines the autonomous agents in the Agentic RAG Chatbot system. Each agent is implemented using the CrewAI `Agent` class and encapsulates a distinct role, goal, backstory, and optional toolset.

These agents form the foundation of the agentic pipeline, handling information retrieval, grounded answer generation, and evaluation. All agents are designed to be modular and reusable within different Crew configurations.

---

## Agents Overview
| Agent           | Role               | Tool(s) Used          | Description                                               |
|----------------|--------------------|------------------------|-----------------------------------------------------------|
| RetrieverAgent | Book Researcher     | `GatsbyRetrieverTool` | Fetches relevant context from Qdrant vector database      |
| GeneratorAgent | Literary Analyst    | (no tool)              | Uses context to generate a grounded, well-written answer  |
| EvaluatorAgent | Answer Evaluator    | `DeepEvalTool`        | Evaluates the answer using DeepEval metrics               |



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

- Agents that require tools (e.g., `GatsbyRetrieverTool`, `DeepEvalTool`) import and register them for use in CrewAI’s action planner.
- Each agent is designed to be easily extended or swapped with alternate toolsets or LLM configurations.

---

## Modularity and Reusability

- Agents are **stateless** and **encapsulated**, which allows them to be reused in different crew or task configurations.
- Each agent is created through a factory function (`create_<role>_agent`) to make instantiation declarative and testable.
- Roles and goals are domain-specific, allowing seamless adaptation to other literary works or corpora.
