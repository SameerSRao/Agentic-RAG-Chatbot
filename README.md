# Agentic RAG Chatbot

A modular, agent-based Retrieval-Augmented Generation (RAG) system that answers questions about *The Great Gatsby* using the CrewAI framework, integrated with DeepEval for answer evaluation. This system demonstrates thoughtful architectural design, tool use, and autonomous reasoning across a multi-step pipeline.

---

## Project Goals

- Design an **agent-based RAG chatbot** that answers literary questions based on a source document (e.g., *The Great Gatsby*).
- Use the CrewAI framework to model agents with tools, roles, goals, and backstories.
- Integrate an **evaluator agent** using DeepEval to score outputs based on:
  - Answer Relevance
  - Contextual Precision, Recall, and Relevancy 
  - Faithfulness
- Store and retrieve context from a **Qdrant vector store**.
- Ensure **modularity** with reusable tools, agents, and pipeline logic.

---


