import os
os.environ["ANONYMIZED_TELEMETRY"] = "False"

from dotenv import load_dotenv
from langchain_community.document_loaders import SeleniumURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQAWithSourcesChain
from uuid import uuid4

from config import *

load_dotenv()

# Global objects
vector_store = None
llm = None

# --------------------
# Load Models
# --------------------

def load_models(temperature):
    global llm, vector_store

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    vector_store = Chroma(
        collection_name="real_estate",
        embedding_function=embeddings,
        persist_directory=VECTOR_DB_DIR
    )

    llm = ChatGroq(
        model=LLM_MODEL,
        temperature=temperature,
        max_tokens=500
    )


# --------------------
# Process URLs
# --------------------

def process_urls(urls, CHUNK_SIZE):

    global vector_store

    if vector_store is None:
        raise Exception("Load models first")

    vector_store.reset_collection()

    loader = SeleniumURLLoader(urls=urls)

    data = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        separators = ["\n\n", "\n", ".", " "],
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function = len
    )

    docs = splitter.split_documents(data)

    ids = [str(uuid4()) for _ in range(len(docs))]

    vector_store.add_documents(docs, ids=ids)


# --------------------
# Ask Question
# --------------------

def ask_question(query):

    global vector_store, llm

    if vector_store is None or llm is None:
        raise Exception("Please process URLs first")

    chain = RetrievalQAWithSourcesChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever()
    )

    result = chain.invoke({"question": query})

    return result["answer"], result["sources"]