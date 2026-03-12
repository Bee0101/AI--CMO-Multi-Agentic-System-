"""
Configuration settings for the AI Twin Marketing System
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Gemini API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")

# Pinecone Configuration
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY", "")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT", "us-east-1")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "ai-twin-marketing")

# Embedding Model
EMBEDDING_MODEL = "text-embedding-3-small"

# Campaign Data Path
CAMPAIGN_DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "campaigns")

# Chat Settings
MAX_TOKENS = 2000
TEMPERATURE = 0.7
SYSTEM_PROMPT = """You are an AI Marketing Strategist that has been trained on past marketing campaigns.
You understand campaign strategy, content creation, social media marketing, and brand messaging.
Use the context from past campaigns to provide relevant, actionable advice.

When answering questions:
1. Reference specific campaigns and examples when relevant
2. Provide actionable recommendations
3. Consider the brand voice and style from previous work
4. Be specific about what worked and what didn't"""

# Integration Settings
HOOTSUITE_API_KEY = os.getenv("HOOTSUITE_API_KEY", "")
SPROUT_SOCIAL_API_KEY = os.getenv("SPROUT_SOCIAL_API_KEY", "")