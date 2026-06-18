import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_llm_response(query, context, persona):

    prompt = f"""
You are a customer support assistant.

Persona: {persona}

Knowledge Base:
{context}

User Query:
{query}

Generate a helpful response according to the user's persona.
Use only the information from the knowledge base.
"""

    response = model.generate_content(prompt)

    return response.text