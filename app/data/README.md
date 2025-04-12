# app/data

This directory contains all static data assets used by the Agentic RAG Chatbot system. These assets are used during the retrieval and evaluation processes.

---

## Contents

### `docs/`
This folder holds source documents that serve as the knowledge base for the chatbot. For example:
- `great_gatsby.txt`: The primary source text used to answer literary questions.
  
---

## Usage

- The file `great_gatsby.txt` is read by the `VectorStoreUtil` class and chunked into semantically meaningful passages using `chonkie`.
- These passages are embedded and stored in Qdrant, forming the foundation for contextual retrieval.
- All queries answered by the chatbot rely on this embedded knowledge base.

---

## Guidelines

- Add new documents only in `.txt` format.
- Ensure documents are cleaned of footnotes, page numbers, or irrelevant metadata for best retrieval quality.
- If using multiple documents, consider separating them into subfolders or naming them descriptively for clarity.


