import os
from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    Docx2txtLoader
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Folder containing support documents
DOCS_PATH = "docs"

# Vector database directory
DB_PATH = "chroma_db"

documents = []

# Load documents
for file in os.listdir(DOCS_PATH):
    path = os.path.join(DOCS_PATH, file)

    try:
        if file.endswith(".txt"):
            loader = TextLoader(path)

        elif file.endswith(".pdf"):
            if os.path.getsize(path) == 0:
                print(f"Skipping empty PDF: {file}")
                continue
            loader = PyPDFLoader(path)

        elif file.endswith(".docx"):
            loader = Docx2txtLoader(path)

        else:
            continue

        documents.extend(loader.load())

    except Exception as e:
        print(f"Error loading {file}: {e}")

for i, doc in enumerate(documents):
    print(f"\nDocument {i+1}")
    print("Length:", len(doc.page_content))
    print("Content preview:")
    print(doc.page_content[:200])

# Chunk documents
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")

# Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create Chroma vector database
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory=DB_PATH
)

print("ChromaDB created successfully!")