from utilis.persona_detector import detect_persona

queries = [
    "Can you explain API authentication failure and logs?",
    "I've tried everything and nothing works!",
    "How does this issue impact operations?"
]

for query in queries:
    print("Query:", query)
    print("Persona:", detect_persona(query))
    print()