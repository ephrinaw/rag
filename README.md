# Student-Wellbeing Chatbot

This chatbot uses retrieval-augmented generation (RAG) to answer questions based on vector search and web retrieval, while also performing hallucination checks to ensure answer accuracy.

## Features

- Document retrieval
- Web search fallback
- Answer generation
- Hallucination check
- Streamlit UI for deployment

## Installation Guide

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd project-root
```

### Step 2: Set Up Virtual Environment

```bash
python3 -m venv env
source env/bin/activate
```

### Step 3: Install Requirements

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

Create a .env file at the root of your project and add your configuration:

```bash
TAVILY_API_KEY=<Your Tavily API Key>
```

### Step 5: Run the Chatbot

```bash
python src/main.py
```
