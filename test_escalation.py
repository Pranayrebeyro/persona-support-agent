from utilis.escalation import should_escalate

queries = [
    "I want a refund immediately!",
    "Can you explain API authentication?",
    "This is the worst experience ever!"
]

for query in queries:
    print("Query:", query)
    print("Escalate:", should_escalate(query))
    print()