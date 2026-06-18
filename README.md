# 🤖 Persona-Based AI Support Agent

## 📌 Project Overview

The Persona-Based AI Support Agent is an intelligent customer support system that adapts its responses based on the user's persona. It combines Retrieval-Augmented Generation (RAG), vector databases, and human escalation mechanisms to provide grounded and context-aware responses.

The system supports:

* Technical Expert
* Frustrated User
* Business Executive

The chatbot retrieves information from a knowledge base and provides persona-specific responses. If required, the conversation is escalated to a human support agent with a generated support ticket.

---

# 🚀 Features

* ✅ Persona Detection
* ✅ Retrieval-Augmented Generation (RAG)
* ✅ ChromaDB Vector Database
* ✅ Sentence Transformer Embeddings
* ✅ Human Escalation System
* ✅ Ticket Generation
* ✅ ChatGPT-style Interface
* ✅ Conversation History
* ✅ Feedback System
* ✅ Streamlit Web Application

---

# 📂 Knowledge Base Documents

The system uses a custom SaaS customer support knowledge base consisting of:

* account_lock.txt
* api_authentication.txt
* dashboard_errors.txt
* data_export.txt
* email_verification.txt
* login_issue.txt
* mfa_setup.txt
* password_reset.txt
* payment_failure.txt
* rate_limits.txt
* refund_policy.txt
* security_policy.txt
* subscription_plans.txt
* user_roles.txt

---

# 🛠 Tech Stack

### Language

* Python 3.11+

### Framework

* Streamlit

### Embedding Model

* Sentence Transformers
* all-MiniLM-L6-v2

### Vector Database

* ChromaDB

### Libraries

* LangChain
* LangChain Community
* LangChain Chroma
* LangChain Text Splitters
* HuggingFace Embeddings
* Sentence Transformers

---

# 📁 Project Structure

```text
persona-support-agent/
│
├── docs/
│
├── chroma_db/
│
├── utils/
│     ├── __init__.py
│     ├── persona_detector.py
│     ├── retriever.py
│     ├── response_generator.py
│     ├── escalation.py
│     ├── handoff.py
│     ├── ticket_generator.py
│
├── app.py
├── ingest.py
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Architecture

```text
User Query
     ↓
Persona Detection
     ↓
Retriever (ChromaDB)
     ↓
Knowledge Base Documents
     ↓
Response Generator
     ↓
Escalation Check
     ↓
Human Handoff
```

---

# 🧠 Supported Personas

## Technical Expert

Characteristics:

* Technical terminology
* API requests
* Configuration issues
* Detailed explanations

---

## Frustrated User

Characteristics:

* Emotional language
* Repeated complaints
* Urgent requests

---

## Business Executive

Characteristics:

* Outcome-focused
* Business impact
* Concise responses

---

# 🔥 Escalation Logic

Conversations are escalated when:

* User expresses frustration
* Human assistance is requested
* Billing or refund issues arise
* Critical keywords are detected

During escalation:

* Ticket ID is generated
* Priority is assigned
* Human support handoff is performed

---

# 📊 Example Queries

### Technical Expert

```
Can you explain API authentication failures?
```

### Frustrated User

```
Nothing works and I am frustrated.
```

### Business Executive

```
How does this issue impact operations?
```

---

# ▶️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd persona-support-agent
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run ingestion:

```bash
python ingest.py
```

Run application:

```bash
streamlit run app.py
```

---

# 🎯 Future Improvements

* Gemini API Integration
* Conversation Memory
* Logging and Analytics
* Download Chat History
* Multi-turn Memory
* Streamlit Deployment

---

# 👨‍💻 Author

Pranay Rebeyro

Final Year Electronics and Communication Engineering

GenAI | Machine Learning | RAG | LLM Applications
