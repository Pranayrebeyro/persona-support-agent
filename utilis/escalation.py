def should_escalate(query):
    query = query.lower()

    escalation_keywords = [
        "manager",
        "supervisor",
        "human agent",
        "refund immediately",
        "angry",
        "frustrated",
        "lawsuit",
        "cancel my account",
        "terrible service",
        "worst experience"
    ]

    return any(keyword in query for keyword in escalation_keywords)