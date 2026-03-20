# 🚀 Rag-Research-Tool

### 🔎 AI-Powered Website Chatbot using RAG (Retrieval-Augmented Generation)

Rag-Research-Tool is an intelligent **URL-based chatbot** that allows users to input website links and ask questions based on their content. It uses **Retrieval-Augmented Generation (RAG)** to fetch relevant information from webpages and generate accurate answers with sources.

---

## ✨ Features

* 🌐 **Multi-URL Input** – Analyze up to 3 websites at once
* 🧠 **RAG Pipeline** – Combines retrieval + LLM for accurate answers
* 🔍 **Source-backed Responses** – Provides answer with references
* ⚡ **Fast Inference** – Powered by Groq LLM (LLaMA 3)
* 📊 **Customizable Chunking** – Adjustable chunk size
* 🎛️ **Temperature Control** – Tune creativity vs accuracy
* 🖥️ **Interactive UI** – Built with Streamlit

---

## 🏗️ Tech Stack

| Component    | Technology                     |
| ------------ | ------------------------------ |
| UI           | Streamlit                      |
| LLM          | Groq (LLaMA 3.3 70B)           |
| Embeddings   | HuggingFace (all-MiniLM-L6-v2) |
| Vector DB    | Chroma                         |
| Framework    | LangChain                      |
| Data Loading | SeleniumURLLoader              |

---

## 🧠 How It Works

1. User inputs website URLs
2. System loads content using Selenium
3. Text is split into chunks
4. Embeddings are generated
5. Stored in Chroma vector database
6. User asks a question
7. Relevant chunks are retrieved
8. LLM generates answer with sources

---

## 📂 Project Structure

```
RAG/
│── config.py          # Configuration settings
│── main_rag.py        # Streamlit UI
│── rag_code.py        # Core RAG pipeline
│── vectorstore/       # Chroma DB storage
│── .env               # API keys
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Rag-Research-Tool.git
cd Rag-Research-Tool
```

### Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### Setup Environment Variables

Create `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run main_rag.py
```

---

## 🧪 Usage

1. Enter up to 3 URLs
2. Click **"Process URLs"**
3. Ask your question
4. Get answer with sources

---

## 📸 Demo

* Input URLs (e.g., news articles)
* Ask questions like:

  * *"What is the mortgage rate?"*
  * *"What did the Fed announce?"*

---

## ⚡ Configuration

Modify in `config.py`:

```python
CHUNK_SIZE = 300
CHUNK_OVERLAP = 50
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
LLM_MODEL = "llama-3.3-70b-versatile"
```

---

## 🚀 Future Improvements

* ✅ PDF & document support
* ✅ Deployment
* ✅ Add guardrails for safety

---

## ⚠️ Limitations

* Selenium-based loading may be slow
* Accuracy depends on webpage content quality
* No long-term memory (stateless queries)

---

