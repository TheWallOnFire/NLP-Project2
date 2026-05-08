import streamlit as st
import requests
import json

# Set page config for a premium look
st.set_page_config(
    page_title="Banking AI-Agent",
    page_icon="🏦",
    layout="wide"
)

# Custom CSS for premium styling
st.markdown("""
    <style>
    .main {
        background-color: #f8fafc;
    }
    .stButton>button {
        border-radius: 12px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .input-container {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
    }
    .output-container {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        border-left: 5px solid #1e3a8a;
    }
    .section-header {
        color: #1e3a8a;
        font-weight: 700;
        margin-bottom: 20px;
        border-bottom: 2px solid #e2e8f0;
        padding-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    st.markdown("<h1 style='text-align: center; color: #1e3a8a;'>🏦 Banking Assistant AI-Agent</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b;'>Next-Generation Agentic Workflow Support</p>", unsafe_allow_html=True)
    st.divider()

    # Session state initialization
    if 'query_input' not in st.session_state:
        st.session_state.query_input = ""
    if 'last_response' not in st.session_state:
        st.session_state.last_response = None

    # Main Layout: 2 Columns
    col_input, col_output = st.columns([1, 1], gap="large")

    # --- LEFT COLUMN: INPUT ---
    with col_input:
        st.markdown("<div class='section-header'>📥 Customer Input</div>", unsafe_allow_html=True)
        
        # Text Input
        query = st.text_area("Enter your banking request:", 
                             value=st.session_state.query_input, 
                             placeholder="e.g., I've lost my debit card, please help!",
                             height=150)
        
        btn_process = st.button("🚀 Process through Agent Workflow", use_container_width=True)

        # Suggestions
        st.markdown("---")
        st.write("💡 **Quick Suggestions**")
        samples = [
            "What is my account balance?",
            "I lost my credit card!",
            "My transfer to John failed.",
            "How do I unblock my account?"
        ]
        
        # Grid for suggestions
        sug_col1, sug_col2 = st.columns(2)
        for i, sample in enumerate(samples):
            target_col = sug_col1 if i % 2 == 0 else sug_col2
            if target_col.button(sample, key=f"sug_{i}", use_container_width=True):
                st.session_state.query_input = sample
                st.rerun()

    # --- RIGHT COLUMN: OUTPUT ---
    with col_output:
        st.markdown("<div class='section-header'>📤 Assistant Output</div>", unsafe_allow_html=True)
        
        if btn_process and query:
            with st.spinner("🧠 Agent is thinking..."):
                try:
                    response = requests.post("http://localhost:8000/process", json={"query": query})
                    response.raise_for_status()
                    st.session_state.last_response = response.json()
                except Exception as e:
                    st.error(f"Connection Error: {e}")
                    st.info("Ensure the FastAPI backend is running.")

        if st.session_state.last_response:
            data = st.session_state.last_response
            
            # 1. Main Response
            with st.chat_message("assistant"):
                st.markdown(data["response"])

            # 2. Agentic Workflow Trace
            with st.expander("🔍 Deep Trace: Agentic Reasoning", expanded=True):
                trace = data["trace"]
                
                t_col1, t_col2 = st.columns(2)
                with t_col1:
                    st.markdown("**Intent Detection**")
                    st.code(f"{trace['intent']['intent']} ({trace['intent']['confidence']*100:.1f}%)")
                    
                    st.markdown("**Priority Assessment**")
                    level = trace['priority']['level'].upper()
                    st.write(f"Level: **{level}**")
                    st.caption(trace['priority']['reason'])

                with t_col2:
                    st.markdown("**Policy Grounding**")
                    st.write(f"Source: *{trace['policy']['source']}*")
                    st.caption(trace['policy']['policy_snippet'])

                st.divider()
                st.markdown("**Validation & Routing**")
                st.write(f"Status: {'✅ Valid' if trace['validation']['is_valid'] else '❌ Clarification Needed'}")
                st.write(f"Decision: `{trace['router']['decision']}`")
                st.caption(trace['router']['explanation'])

            # 3. Export/Copy Section
            st.divider()
            st.write("📄 **Export Content**")
            
            plain_text = f"CUSTOMER QUERY: {query}\n\nASSISTANT RESPONSE: {data['response']}\n\nWORKFLOW TRACE:\n- Intent: {trace['intent']['intent']}\n- Priority: {trace['priority']['level']}\n- Decision: {trace['router']['decision']}"
            
            st.markdown("Copy the text below:")
            st.code(plain_text, language="text")
            
        else:
            st.info("Waiting for a request to process...")

if __name__ == "__main__":
    main()
