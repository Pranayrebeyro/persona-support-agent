def detect_persona(user_message):
    message = user_message.lower()

    # Technical Expert
    technical_keywords = [
        "api", "logs", "error", "configuration",
        "authentication", "token", "endpoint", "server"
    ]

    # Frustrated User
    frustrated_keywords = [
        "nothing works", "frustrated", "urgent",
        "again", "still not working", "angry", "issue"
    ]

    # Business Executive
    business_keywords = [
        "impact", "operations", "timeline",
        "business", "revenue", "customer", "resolution"
    ]

    if any(word in message for word in technical_keywords):
        return "Technical Expert"

    elif any(word in message for word in frustrated_keywords):
        return "Frustrated User"

    elif any(word in message for word in business_keywords):
        return "Business Executive"

    else:
        return "General User"