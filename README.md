# Local Persona Chat

An offline, privacy-focused LLM chat application built with Streamlit and powered locally by Ollama. It features streaming responses, persistent multi-session chat history, and customizable AI personas.

## 🚀 Features

* **100% Local & Private:** Connects directly to local Ollama instances (`llama3.1`)—no data leaves your machine.
* **Customizable Personas:** Switch dynamically between built-in personas (Professor, Mohamed Salah, Pirate, Clown, Standard Assistant) to adapt the tone and behavior of the model.
* **Real-time Token Streaming:** Streams tokens live as they are generated using Ollama's HTTP chat endpoint.
* **Multi-Session Chat History:** Create and switch between independent chat sessions, persisted locally via `local_chats.json`.

## 🛠️ Tech Stack

* **Frontend & UI:** Streamlit
* **LLM Engine:** Ollama (`llama3.1`)
* **Language:** Python 3.10+
* **Networking & Persistence:** Requests, JSON, UUID

## 📋 Prerequisites

1. Install **[Ollama](https://ollama.ai/)**.
2. Pull the default model used in the script:
bash
`ollama pull llama3.1`

⚙️ Installation & Setup
1. Clone the repository:

Bash
`git clone [https://github.com/Abdo-0x04/local-persona-chat.git](https://github.com/Abdo-0x04/local-persona-chat.git)
cd local-persona-chat`
2. Set up a virtual environment:

Bash
# Windows
`python -m venv venv
venv\Scripts\activate`

# macOS / Linux
`python3 -m venv venv
source venv/bin/activate`

3. Install dependencies:

Bash
`pip install -r requirements.txt`

💻 Running the App
Start the Streamlit application:

Bash
`streamlit run local_persona_bot.py`

**3. Managing Personas:**
To add or modify a persona, simply edit the `PERSONAS` dictionary at the top of the `local_persona_bot.py` file:
`python
PERSONAS = {
    "Your New Persona": "Your custom system prompt describing how the AI should act.",
    "Standard Assistant": "You are a helpful, respectful, and concise AI assistant.",
    # ...
}
`
👤 Author
Abdelrahman Sherif

GitHub: [@Abdo-0x04](https://github.com/Abdo-0x04/)

LinkedIn: [Abdelrahman Sherif Ali](https://www.linkedin.com/in/abdelrahman-sherif-ali/)
