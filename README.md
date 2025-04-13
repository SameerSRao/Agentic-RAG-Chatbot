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
---

## Sample Interaction
<img width="1150" alt="Screenshot 2025-04-12 at 11 32 24 PM" src="https://github.com/user-attachments/assets/a2307c07-1869-4678-ad54-ed527d8c216c" />

---
## Getting Started
Follow these steps to set up the Agentic-RAG-Chatbot locally.

### Prerequisites
Make sure you have the following installed:
```
- Python 3.9+
- pip
- Docker (for Qdrant)
- Git
```
### Clone the Repository
```bash
git clone https://github.com/SameerSRao/Agentic-RAG-Chatbot.git
cd Agentic-RAG-Chatbot
```
### Set Up Environment 
Using virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### Configure Environment Variables
```bash
cp .env.example .env
```
### Start Qdrant
```bash
docker pull qdrant/qdrant  #install qdrant if not installed locally
docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant
```
### Run App
```bash
python main.py
```
