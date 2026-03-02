import streamlit as st
from rag_code import *

# Page config
st.set_page_config(
    page_title="RAG Website Chatbot",
    page_icon=":robot:",
    layout="wide"
)

# -------------------------
# SIDEBAR
# -------------------------

urls = []

url1 = st.sidebar.text_input("URL 1")
url2 = st.sidebar.text_input("URL 2")
url3 = st.sidebar.text_input("URL 3")

if url1:
    urls.append(url1)

if url2:
    urls.append(url2)

if url3:
    urls.append(url3)

query = st.sidebar.text_input("Enter your question")

st.sidebar.header("Model Performance Options")

chunk_size = st.sidebar.number_input(
    "Chunk Size",
    min_value=200,
    max_value=800,
    value=300
)

temperature = st.sidebar.slider(
    "Temperature",
    0.1,
    1.0,
    0.3,
    0.1
)

# -------------------------
# MAIN PAGE
# -------------------------

st.title("RAG Based Website Chatbot")

st.markdown(
"""
Provide URLs and ask questions based on website content.
"""
)

# Instructions
with st.expander("Instructions and Tips"):

    st.write("""
### Instructions

1. Enter URLs
2. Click **Process URLs**
3. Ask question

Tool will:

- Load URLs
- Generate embeddings
- Store in vector DB
- Retrieve answers
""")

# -------------------------
# Buttons
# -------------------------

col1, col2 = st.columns(2)

with col1:

    if st.button("Process URLs"):
        load_models(temperature)

        if not urls:

            st.warning("Enter URLs")

        else:

            with st.spinner("Processing URLs..."):

                process_urls(urls, chunk_size)

            st.success("Vector DB Ready")


with col2:

    if st.button("Ask Question"):

        if not query:

            st.warning("Enter question")

        else:

            with st.spinner("Generating answer..."):

                answer, sources = ask_question(query)

            st.subheader("Answer")

            st.write(answer)

            st.subheader("Sources")

            st.write(sources)