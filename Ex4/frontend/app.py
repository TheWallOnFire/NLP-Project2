import streamlit as st
import requests
import os

st.set_page_config(page_title="Banking AI-Agent", page_icon="🏦")

st.title("🏦 Banking AI-Agent")
st.markdown("Welcome to your AI-powered banking assistant. Ask me anything!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

api_base_url = os.getenv("API_BASE_URL", "http://localhost:8000")

if prompt := st.chat_input("How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    f"{api_base_url}/classify",
                    json={"message": prompt},
                    timeout=60
                )
                response.raise_for_status()
                data = response.json()
                
                intent = data.get("intent")
                confidence = data.get("confidence")
                reason = data.get("reason")
                agent_response = data.get("response")
                
                st.markdown(agent_response)
                st.caption(f"Intent: {intent} (Confidence: {confidence:.2f})")
                st.caption(f"Reason: {reason}")
                
                st.session_state.messages.append({"role": "assistant", "content": agent_response})
            except Exception as e:
                error_msg = f"Sorry, I'm having trouble connecting to the service. Error: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
