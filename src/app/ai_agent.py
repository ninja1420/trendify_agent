from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage
from constants import SYSTEM_PROMPT
load_dotenv()

os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

openai_llm = ChatOpenAI(model="gpt-4o-mini")
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")


def get_response_from_agent(llm_id: str, query: str, allow_search: bool, provider: str) -> str:
    """
        Generates a response from an AI agent based on the provided parameters.
        Args:
            llm_id (str): The identifier for the language model to be used.
            query (str): The input query or prompt for the agent.
            allow_search (bool): Whether to enable search functionality for the agent.
            provider (str): The provider of the language model (e.g., "Groq", "OpenAI").
        Returns:
            str: The final response generated by the AI agent.
    """

    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)
    tools = [TavilySearchResults(max_results=2)] if allow_search else []
    agent = create_react_agent(
            model=llm,
            tools=tools,
            state_modifier=SYSTEM_PROMPT)
    
    state = {"messages":query}
    response = agent.invoke(state)
    messages = response["messages"]
    ai_messages = [m.content for m in messages if isinstance(m, AIMessage)]
    return ai_messages[-1]




