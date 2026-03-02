import streamlit as st
from rag_code import process_urls, ask_question

st.title("News Research Tool")

urls = []

url1 = st.text_input("URL 1")
url2 = st.text_input("URL 2")
url3 = st.text_input("URL 3")

if url1:
    urls.append(url1)

if url2:
    urls.append(url2)

if url3:
    urls.append(url3)


query = st.text_input("Enter your question")


if st.button("Process URLs"):

    if not urls:
        st.warning("Enter URLs")

    else:
        with st.spinner("Processing URLs..."):
            process_urls(urls)

        st.success("Vector database ready")


if st.button("Ask Question"):

    if not query:
        st.warning("Enter a question")

    else:

        with st.spinner("Generating answer..."):

            answer, sources = ask_question(query)

        st.write("Answer:")
        st.write(answer)

        st.write("Sources:")
        st.write(sources)