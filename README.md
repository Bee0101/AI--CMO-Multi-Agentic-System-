# AI Twin / Multi-Agent Marketing Strategist 🤖📈

A multi-agent marketing strategist digital twin system. This project is a Minimum Viable Product (POC) designed to train an AI on past marketing campaigns, enabling it to answer strategic questions and generate actions using Retrieval-Augmented Generation (RAG).

## 🌟 Key Features
- **Core AI Trained on Past Campaigns:** Uses historical marketing data (e.g., campaigns from Bonsey Jaden, Publicis Singapore, Subway, Shangri-La) to learn to think and write effectively.
- **Strategic Q&A (RAG System):** Answers questions such as "What content should we post this week?" with insightful, data-backed strategies using a Pinecone vector database.
- **Social Media Integration:** Connects seamlessly with platforms like Hootsuite and Sprout Social to demonstrate execution (e.g., preparing or scheduling a post).
- **Web Chat Interface:** A streamlined, auth-free chat UI to query the AI directly.

## 🛠️ Tech Stack
- **Backend Framework:** FastAPI (Python)
- **AI / LLMs:** DeepSeek API (chat), OpenAI API (embeddings), LangChain
- **Vector Database:** Pinecone
- **Document Processing:** pypdf, python-docx
- **Frontend:** Vanilla HTML, CSS, JavaScript (Jinja2 optional templating)

---

## 💻 System Setup & Installation

### 1. Prerequisites
- **Python 3.9+** installed on your system.
- API Keys for DeepSeek, OpenAI, and Pinecone.
- (Optional) API Keys for Hootsuite / Sprout Social.

### 2. Clone/Obtain the Repository
Make sure you have downloaded or cloned the project folder onto your device. Navigate to the project directory:
```bash
cd AI--CMO-Multi-Agentic-System-
```

### 3. Create a Virtual Environment
It is highly recommended to isolate your dependencies using a Python virtual environment.
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
Install all required Python packages listed in the `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 5. Environment Variables Configuration
Create a `.env` file in the root of the project (if it does not exist) and add the following configuration variables:

```env
# DeepSeek LLM Configuration
DEEPSEEK_API_KEY=your_deepseek_api_key
DEEPSEEK_BASE_URL=https://api.deepseek.com
DEEPSEEK_MODEL=deepseek-chat

# Pinecone Vector Database
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=us-east-1
PINECONE_INDEX_NAME=ai-twin-marketing

# Embedding Model (use OpenAI for embeddings)
OPENAI_API_KEY=your_openai_api_key
EMBEDDING_MODEL=text-embedding-3-small

# Social Media Integrations (Optional)
HOOTSUITE_API_KEY=your_hootsuite_api_key
SPROUT_SOCIAL_API_KEY=your_sprout_social_api_key
```
*(Note: Do not commit your real `.env` keys to version control.)*

---

## 🚀 Run Commands

### Start the Backend API Server
With your virtual environment activated, start the FastAPI server via Uvicorn:
```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```
- **API Documentation (Swagger UI):** Available at `http://localhost:8000/docs`
- **Health Check:** Verify the API is running at `http://localhost:8000/api/health`

### Launch the Frontend Chat Interface
The frontend consists of static files (`index.html`, `app.js`, `style.css`). Since the backend provides a REST API, you can easily open the UI using any local development server. 

For instance, using Python's built-in HTTP server:
```bash
# Open a new terminal, navigate to the frontend directory
cd frontend
python -m http.server 3000
```
Then, open your browser and navigate to `http://localhost:3000/templates/index.html`.

### Initial Training / Ingesting Campaign Data
To train the AI on past campaigns:
1. Ensure your PDF/Word campaign documents are placed in `data/campaigns/` (create this folder if not present).
2. Send a POST request to `/api/train` via the `/docs` UI or cURL to process the documents and populate the Pinecone database.

---

## 📂 Project Structure
```text
AI--CMO-Multi-Agentic-System-/
├── backend/                  # FastAPI backend containing the core logic
│   ├── main.py               # Main API application 
│   ├── config.py             # Configuration & Environment loading
│   ├── document_loader.py    # Processing campaign docs (PDF, Word)
│   ├── vector_store.py       # Pinecone DB interactions
│   ├── rag_chain.py          # RAG pipeline logic
│   └── integrations.py       # Social media tools (Hootsuite/Sprout)
├── frontend/                 # Chat interface UI
│   ├── static/             
│   │   ├── app.js            # Chat UI logic
│   │   └── style.css         # Chat styling
│   └── templates/
│       └── index.html        # Main chat webpage
├── .env                      # Environment variables
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```
