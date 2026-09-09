import streamlit as st
import requests
import json
import uuid
import os

# Configuration for your local AI engine (Ollama)
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.1"
CHATS_FILE = "local_chats.json" 

PERSONAS = {
    "Standard Assistant": "You are a helpful, respectful, and concise AI assistant.",
    "Pirate": "You are a swashbuckling pirate navigating the seven seas. Speak strictly like a pirate, use nautical terms, and say 'Arrr' frequently.",
    "Professor": "You are an esteemed, highly intellectual university professor. Speak formally, use advanced vocabulary, and explain concepts thoroughly but clearly.",
    "Mohamed Salah": "You are Mohamed Salah, the famous Egyptian football star playing for Liverpool. Be humble, cheerful, and frequently mention your love for football, scoring goals, Liverpool, and your home country of Egypt.",
    "Clown": "You are a silly, highly energetic clown. Make jokes, use puns, act goofy, and try to make the user laugh in every response."
}

def load_chats():
    """Loads chat history from the JSON file if it exists."""
    if os.path.exists(CHATS_FILE):
        with open(CHATS_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                pass
    return {str(uuid.uuid4()): []}

def save_chats(chats_dict):
    """Saves the current chat dictionary to the JSON file."""
    with open(CHATS_FILE, "w") as f:
        json.dump(chats_dict, f, indent=4)

st.set_page_config(page_title="Offline Chat Bot", layout="wide")

if "chats" not in st.session_state:
    st.session_state.chats = load_chats()
    st.session_state.current_chat_id = list(st.session_state.chats.keys())[0]

with st.sidebar:
    st.title("⚙️ Settings")
    
    selected_persona = st.selectbox("Choose a Persona:", list(PERSONAS.keys()))
    
    st.divider()
    
    if st.button("➕ New Chat", use_container_width=True):
        new_id = str(uuid.uuid4())
        st.session_state.chats[new_id] = []
        st.session_state.current_chat_id = new_id
        save_chats(st.session_state.chats)
        
    st.divider()
    st.write("### Your Chats")
    for chat_id in st.session_state.chats.keys():
        if st.button(f"💬 Chat {chat_id[:5]}", key=chat_id, use_container_width=True):
            st.session_state.current_chat_id = chat_id

st.title(f"Offline Chat Bot - {selected_persona} Mode")

current_history = st.session_state.chats[st.session_state.current_chat_id]
for msg in current_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
if prompt := st.chat_input("Send a message to your local AI..."):
    
    with st.chat_message("user"):
        st.write(prompt)
    current_history.append({"role": "user", "content": prompt})
    save_chats(st.session_state.chats)
    
    system_message = {"role": "system", "content": PERSONAS[selected_persona]}
    messages_to_send = [system_message] + current_history

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        try:
            payload = {
                "model": MODEL,
                "messages": messages_to_send,
                "stream": True
            }
            response = requests.post(OLLAMA_URL, json=payload, stream=True)
            response.raise_for_status()
            
            for line in response.iter_lines():
                if line:
                    chunk = json.loads(line)
                    if "message" in chunk:
                        full_response += chunk["message"]["content"]
                        response_placeholder.markdown(full_response + "▌")
            
            response_placeholder.markdown(full_response)
            current_history.append({"role": "assistant", "content": full_response})
            save_chats(st.session_state.chats)
            
        except requests.exceptions.ConnectionError:
            st.error("Error: Could not connect to the local AI. Please make sure Ollama is running.")
