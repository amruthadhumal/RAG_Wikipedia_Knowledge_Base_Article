# Dynamic AI Knowledge Assistant using RAG and Wikipedia

## Project Overview

This project is a Retrieval-Augmented Generation (RAG) application that automatically builds a knowledge base from Wikipedia articles and uses a Large Language Model (LLM) to answer user questions.

The system retrieves relevant information from a custom knowledge base before generating responses, helping reduce hallucinations and improve answer accuracy.

---

## Features

* Automatic Wikipedia article collection
* Knowledge base creation using text documents
* Document chunking for efficient retrieval
* Text embeddings using Sentence Transformers
* FAISS vector database for semantic search
* Retrieval-Augmented Generation (RAG) pipeline
* Question-answering using an LLM (TinyLlama)
* Easy-to-understand implementation for learning purposes

---

## Project Architecture

<img width="631" height="508" alt="image" src="https://github.com/user-attachments/assets/0f5c672e-cb7a-49f6-8463-cc64c66d80da" />


---

## Technologies Used

### Programming Language

* Python

### Libraries

* LangChain
* Hugging Face Transformers
* Sentence Transformers
* FAISS
* Pandas
* Wikipedia API
* tqdm

### Models

#### Embedding Model

* all-MiniLM-L6-v2

#### Large Language Model

* TinyLlama-1.1B-Chat-v1.0

---

## Project Workflow

### Step 1: Collect Wikipedia Articles

Relevant Wikipedia articles are downloaded and stored locally as text files.

### Step 2: Load Documents

Articles are loaded into LangChain Document objects.

### Step 3: Split Documents

Large documents are divided into smaller chunks to improve retrieval quality.

### Step 4: Generate Embeddings

Each chunk is converted into vector embeddings using a Sentence Transformer model.

### Step 5: Create FAISS Index

Embeddings are stored in a FAISS vector database for fast similarity search.

### Step 6: Retrieve Relevant Context

When a user asks a question, the retriever finds the most relevant document chunks.

### Step 7: Generate Answer

Retrieved context and the user question are passed to the LLM, which generates the final response.

---

## Example Query

### User Question

```text
What is Machine Learning?
```

### Generated Answer

```text
Machine Learning is a branch of Artificial Intelligence that enables systems to learn patterns from data and make predictions without being explicitly programmed.
```

---

## Advantages of RAG

* Reduces hallucinations
* Uses external knowledge sources
* Easy to update without retraining
* Improves answer accuracy
* Cost-effective compared to fine-tuning


---

## Learning Outcomes

Through this project, I gained experience with:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* FAISS Indexing
* Embedding Models
* LangChain Framework
* Prompt Engineering
* Large Language Models (LLMs)

---

<img width="1416" height="562" alt="image" src="https://github.com/user-attachments/assets/dd6fcb45-8b41-4c82-87a9-553fd6ff8063" />


---

<img width="1393" height="178" alt="image" src="https://github.com/user-attachments/assets/ed8a5db0-f0a9-41cb-b4e3-292f3299f232" />

---

<img width="1385" height="567" alt="image" src="https://github.com/user-attachments/assets/1de54706-1bd0-4459-ac14-54178415bb58" />



