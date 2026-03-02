from pathlib import Path

VECTOR_DB_DIR = str(Path(__file__).parent / "vectorstore")

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

LLM_MODEL = "llama-3.3-70b-versatile"

CHUNK_SIZE = 300
CHUNK_OVERLAP = 50