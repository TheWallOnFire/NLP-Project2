import streamlit as st
import requests
import json
import base64
from streamlit_mic_recorder import mic_recorder

# Set page config for a premium look
st.set_page_config(
    page_title="Banking AI-Agent",
    page_icon="🏦",
    layout="centered"
)

# Custom CSS for better aesthetics
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #1e3a8a;
        color: white;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
    }
    .response-card {
        padding: 20px;
        background-color: white;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .trace-section {
        background-color: #e5e7eb;
        padding: 15px;
        border-radius: 10px;
        margin-top: 10px;
    }
    .priority-high { color: #dc2626; font-weight: bold; }
    .priority-medium { color: #d97706; font-weight: bold; }
    .priority-low { color: #059669; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

def speak_text(text):
    """
    Client-side text to speech using Javascript
    """
    js = f"""
    <script>
    var msg = new SpeechSynthesisUtterance("{text.replace('"', "'")}");
    window.speechSynthesis.speak(msg);
    </script>
    """
    st.components.v1.html(js, height=0)

def main():
    st.title("🏦 Banking Assistant AI")
    st.markdown("How can I help you with your account today?")

    # Initialize session state for the query
    if 'query_input' not in st.session_state:
        st.session_state.query_input = ""

    # Voice Input
    st.write("🎤 **Voice Input**")
    audio = mic_recorder(
        start_prompt="Click to Speak",
        stop_prompt="Stop Recording",
        just_once=True,
        use_container_width=True,
        key='recorder'
    )

    if audio:
        # Note: In a real app, we'd send this to an STT service.
        # For this demo, we'll assume the user might also type, 
        # or we could integrate OpenAI Whisper / Google STT if needed.
        st.info("Audio recorded successfully! (STT integration pending - please use text for now)")

    # Text Input
    query = st.text_input("Enter your request:", value=st.session_state.query_input, placeholder="e.g., I lost my credit card...")

    if st.button("Process Request") and query:
        with st.spinner("Processing your request through the agentic workflow..."):
            try:
                response = requests.post("http://localhost:8000/process", json={"query": query})
                response.raise_for_status()
                data = response.json()

                # Display Response
                st.markdown("### 🤖 Assistant's Response")
                with st.chat_message("assistant"):
                    st.markdown(data["response"])
                
                # TTS
                speak_text(data["response"])

                # Display Trace
                with st.expander("🔍 View Agentic Workflow Trace"):
                    trace = data["trace"]
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("**1. Intent Detection**")
                        st.write(f"Intent: `{trace['intent']['intent']}`")
                        st.write(f"Confidence: {trace['intent']['confidence']:.2f}")
                        
                        st.markdown("**2. Priority Assessment**")
                        p_level = trace['priority']['level']
                        st.markdown(f"Level: <span class='priority-{p_level}'>{p_level.upper()}</span>", unsafe_allow_html=True)
                        st.write(f"Reason: {trace['priority']['reason']}")

                    with col2:
                        st.markdown("**3. Policy Retrieval**")
                        st.write(f"Source: {trace['policy']['source']}")
                        st.caption(f"Snippet: {trace['policy']['policy_snippet']}")

                    st.divider()
                    
                    col3, col4 = st.columns(2)
                    with col3:
                        st.markdown("**4. Drafting & Validation**")
                        st.write(f"Valid: {'✅' if trace['validation']['is_valid'] else '❌'}")
                        if trace['validation']['feedback']:
                            st.write(f"Feedback: {trace['validation']['feedback']}")
                        
                        st.write("**Missing Info:**")
                        if trace['draft']['missing_information']:
                            for item in trace['draft']['missing_information']:
                                st.write(f"- {item}")
                        else:
                            st.write("None")

                    with col4:
                        st.markdown("**5. Final Routing**")
                        st.write(f"Decision: `{trace['router']['decision']}`")
                        st.write(f"Explanation: {trace['router']['explanation']}")
                        st.write(f"Next Action: {trace['draft']['next_action']}")

            except Exception as e:
                st.error(f"Error connecting to backend: {e}")
                st.info("Make sure the FastAPI server is running (python run.py)")

    # Sample Requests
    st.divider()
    st.markdown("### 💡 Examples")
    samples = [
        "What is my account balance?",
        "I lost my credit card at the mall!",
        "My transfer to John failed last night.",
        "How do I unblock my account?"
    ]
    
    cols = st.columns(2)
    for i, sample in enumerate(samples):
        if cols[i % 2].button(sample, key=f"sample_{i}"):
            st.session_state.query_input = sample
            st.rerun()

if __name__ == "__main__":
    main()
