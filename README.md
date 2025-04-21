# FashionFinder Agent 👗

An AI-powered fashion assistant that provides personalized style advice, trend insights, and fashion recommendations using LangGraph, Groq, and OpenAI.

## Features ✨

- Real-time fashion advice and recommendations
- Web search capability using Tavily API
- Multiple AI model support (Groq and OpenAI)
- Interactive web interface built with Streamlit
- REST API backend using FastAPI

## Prerequisites 🛠️

- Python 3.8+
- pip package manager

## Setup Steps 📝

1. **Clone the Repository**
```sh
git clone <repository-url>
cd chatbot_agentic
```

2. **Install Dependencies**
```sh
pip install -r requirements.txt
```

3. **Get API Keys**

You'll need to obtain API keys from:

- **Groq API Key**:
  - Visit [Groq Console](https://console.groq.com)
  - Sign up for an account
  - Navigate to API Keys section
  - Create a new API key

- **OpenAI API Key**:
  - Go to [OpenAI Platform](https://platform.openai.com)
  - Create an account/Login
  - Navigate to API section
  - Generate a new API key

- **Tavily API Key**:
  - Visit [Tavily AI](https://tavily.com)
  - Sign up for an account
  - Go to API section
  - Generate your API key

4. **Configure Environment Variables**

Create a `.env` file in the root directory:

```sh
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

5. **Start the Backend Server**
```sh
cd src/app
python backend.py
```

6. **Launch the Streamlit App**
Open a new terminal and run:
```sh
cd src/app
streamlit run streamlit_App.py
```

## Using the Application 🚀

1. **Access the Web Interface**
   - Open your browser and go to `http://localhost:8501`

2. **Configure Settings**
   - Choose model provider (Groq or OpenAI)
   - Select AI model
   - Enable/disable web search

3. **Ask Fashion Questions**
   - Type your fashion-related questions
   - Use trending tags for quick queries
   - Get AI-powered fashion advice

## Project Structure 📂

```
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
└── src/
    └── app/
        ├── ai_agent.py       # AI agent implementation
        ├── backend.py        # FastAPI backend
        ├── constants.py      # System prompts and constants
        └── streamlit_App.py  # Streamlit frontend
```

## API Endpoints 🔌

- **POST** `/chat`
  - Endpoint for fashion-related queries
  - Accepts JSON payload with model settings and query
  - Returns AI-generated fashion advice

## Models Supported 🤖

**Groq Models:**
- llama3-70b-8192
- llama-3.3-70b-versatile
- mixtral-8x7b-32768

**OpenAI Models:**
- gpt-4o-mini
