# Local Persona Chat

An offline, fully localized LLM chat application featuring customizable AI personas and Retrieval-Augmented Generation (RAG) capabilities. Built with privacy and performance in mind, this project runs open-source models completely locally while maintaining independent chat sessions and contextual memory.

## 🚀 Features

* **Customizable AI Personas:** Switch between dynamically prompted personas (e.g., Professor, Football Player) to tailor the assistant's tone and expertise.
* **100% Offline Execution:** Powered by Ollama, ensuring that all prompts, documents, and chat histories remain completely on your local machine.
* **Vector-Based Context Retrieval:** Integrates ChromaDB via Docker for efficient semantic search and document retrieval (RAG pipeline).
* **Session Management:** Maintains independent chat sessions and saves historical chat data to local JSON files for persistent memory.
* **Interactive UI & Robust Backend:** Features a clean Streamlit frontend communicating with a FastAPI backend.

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** FastAPI, Python
* **LLM Engine:** Ollama (Open-source local models)
* **Vector Database:** ChromaDB 
* **Containerization:** Docker (ChromaDB deployment)

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
* [Python 3.8+](https://www.python.org/downloads/)
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) (for running ChromaDB)
* [Ollama](https://ollama.ai/) (with your preferred model pulled, e.g., `ollama run llama3`)

## ⚙️ Installation & Setup

**1. Clone the repository:**
```bash
git clone [https://github.com/Abdo-0x04/local-persona-chat.git](https://github.com/Abdo-0x04/local-persona-chat.git)
cd local-persona-chat
```
2. Set up a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
pip install -r requirements.txt

4. Start the ChromaDB Vector Store:
docker run -p 8000:8000 chromadb/chroma

💻 Usage
1. Start the FastAPI backend:

Bash
(uvicorn main:app --reload)

2. Launch the Streamlit frontend:

Open a new terminal window and run:
Bash 
(streamlit run app.py)


👤 Author
Abdelrahman Sherif

GitHub: [@Abdo-0x04](https://github.com/Abdo-0x04/)

LinkedIn: [Abdelrahman Sherif Ali](https://www.linkedin.com/in/abdelrahman-sherif-ali/)
