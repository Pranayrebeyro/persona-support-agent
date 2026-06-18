from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

DB_PATH = "chroma_db"

# Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load ChromaDB
vectorstore = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embedding_model
)


def retrieve_documents(query, k=3):
    results = vectorstore.similarity_search(query, k=k)

    return results