from utilis.retriever import retrieve_documents

query = "How do I reset my password?"

results = retrieve_documents(query)

print("\nRetrieved Documents:\n")

for i, doc in enumerate(results, 1):
    print(f"Result {i}")
    print(doc.page_content)
    print("-" * 50)