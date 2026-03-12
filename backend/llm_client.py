"""
Gemini LLM Client
"""
from langchain_google_genai import ChatGoogleGenerativeAI
from backend.config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
    MAX_TOKENS,
    TEMPERATURE,
    SYSTEM_PROMPT
)

def get_llm():
    """
    Initialize and return the Gemini LLM client
    """
    return ChatGoogleGenerativeAI(
        model=GEMINI_MODEL,
        google_api_key=GEMINI_API_KEY,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
    )

def get_chat_response(user_message: str, context: str = "") -> str:
    """
    Get response from Gemini LLM with optional context

    Args:
        user_message: The user's question/message
        context: Optional context from RAG retrieval

    Returns:
        LLM response as string
    """
    llm = get_llm()

    # Build the prompt with context if available
    if context:
        prompt = f"""Context from past campaigns:
{context}

---
User Question: {user_message}

Please provide a strategic answer based on the context above and your training on marketing campaigns."""
    else:
        prompt = f"""{SYSTEM_PROMPT}

User Question: {user_message}"""

    response = llm.invoke(prompt)
    return response.content if hasattr(response, 'content') else str(response)