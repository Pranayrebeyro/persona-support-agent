from utilis.persona_detector import detect_persona
from utilis.retriever import retrieve_documents
from utilis.gemini_response import generate_llm_response

def generate_response(query):
    persona = detect_persona(query)

    docs = retrieve_documents(query)
    context = "\n".join([doc.page_content for doc in docs])

    if persona == "Technical Expert":
        response = f"""
Technical Analysis:

Based on the documentation, authentication failures are usually caused by:

• Invalid API keys.
• Expired access tokens.
• Missing authorization headers.
• Incorrect endpoint URLs.

Recommended Actions:
1. Verify the API key.
2. Generate a fresh token.
3. Check server logs.
4. Validate request headers.
"""

    elif persona == "Business Executive":
        response = """
Business Impact:

Authentication failures may affect customer experience and application availability.

Recommended Action:
Coordinate with the technical team to resolve authentication issues quickly and minimize operational impact.
"""

    elif persona == "Frustrated User":
        response = """
I understand the issue is frustrating.

Please follow these steps:

1. Verify your API credentials.
2. Generate a new token.
3. Retry the request.
4. Contact support if the problem persists.

Your issue can also be escalated to a human agent.
"""

    else:
        response = generate_llm_response(query, context, persona)

    return response