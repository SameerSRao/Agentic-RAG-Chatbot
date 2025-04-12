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
## Folder Structure
```
Agentic-RAG-Chatbot/
├── app/
│   ├── agents/              # Agent definitions (retriever, generator, evaluator)
│   ├── data/                # Source documents (e.g., The Great Gatsby)
│   ├── embeddings/          # Vector store utilities using Qdrant
│   ├── tools/               # Custom tools for retrieval and DeepEval
│   ├── pipeline.py          # Orchestrates the full multi-agent RAG pipeline
│   └── tasks.py             # Defines how tasks are passed between agents
│
├── main.py                  # Entry point to run the system interactively
├── requirements.txt         # Python dependencies
├── README.md                # (You are here)
```
---
## High-Level Flow

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
## Screenshots
<img width="1470" alt="Screenshot 2025-04-12 at 3 31 40 PM" src="https://github.com/user-attachments/assets/cadd2860-1582-40d1-b745-9190dfa47131" />
<img width="1470" alt="Screenshot 2025-04-12 at 3 33 25 PM" src="https://github.com/user-attachments/assets/3fa16fc7-33e6-4586-97b8-cea708840ea1" />


