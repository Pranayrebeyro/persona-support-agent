import streamlit as st

from utilis.persona_detector import detect_persona
from utilis.response_generator import generate_response
from utilis.escalation import should_escalate
from utilis.handoff import handoff_to_human

# Page Configuration
st.set_page_config(
    page_title="Persona-Based AI Support Agent",
    page_icon="🤖"
)

# Sidebar
st.sidebar.title("🤖 Persona Support Agent")

st.sidebar.markdown("""
### Features

✅ Persona Detection

✅ Retrieval-Augmented Generation (RAG)

✅ Human Escalation

✅ Ticket Generation

✅ Feedback System

✅ Chat History
""")

# Title
st.title("🤖 Persona-Based AI Support Agent")
st.write("Ask your questions and receive intelligent support.")

# Initialize Chat History
if "history" not in st.session_state:
    st.session_state.history = []

# User Input
query = st.text_area("Enter your query")

# Submit Button
if st.button("Submit"):

    if query:

        # Detect Persona
        persona = detect_persona(query)

        st.subheader("Detected Persona")
        st.success(persona)

        # Generate Response
        response = generate_response(query)

        st.subheader("AI Response")
        st.info(response)

        # Save Chat History
        st.session_state.history.append(
            {
                "query": query,
                "response": response
            }
        )

        # Escalation
        if should_escalate(query):

            st.error("⚠ Human Escalation Required")

            st.subheader("Human Support Ticket")

            st.warning(handoff_to_human())

        # Feedback Section
        st.subheader("Feedback")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("👍 Helpful"):
                st.success("Thank you for your feedback!")

        with col2:
            if st.button("👎 Not Helpful"):
                st.warning("Feedback recorded.")

# Chat History
st.subheader("Chat History")

for item in reversed(st.session_state.history):

    st.write("👤 User:")
    st.write(item["query"])

    st.write("🤖 Assistant:")
    st.write(item["response"])

    st.divider()

# Clear Chat Button
if st.button("Clear Chat"):
    st.session_state.history = []
    st.rerun()