import os
from dotenv import load_dotenv
from google import genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from tools import get_market_research_tools

load_dotenv()

def build_market_intelligence_agent():
    """Builds and returns the LangChain Agent powered by Google Gemini and Tavily search."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")

    # Initialize Google Gemini model (gemini-2.5-flash handles tool calling efficiently)
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key,
        temperature=0.2
    )

    # Get tools
    tools = get_market_research_tools()

    # Prompt structure guiding the agent to gather data and format it precisely
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are an expert AI Market Intelligence Agent. Your job is to conduct comprehensive market research on a given industry.\n"
            "You have access to search tools to find real-time data on startups, trends, and funding rounds.\n"
            "You must perform searches, synthesize the findings, and format your final report precisely as requested:\n\n"
            "Top startups:\n"
            "- [Startup 1]\n"
            "- [Startup 2]\n"
            "- [Startup 3]\n\n"
            "Latest trends:\n"
            "- [Trend 1]\n"
            "- [Trend 2]\n"
            "- [Trend 3]\n\n"
            "Top funding rounds:\n"
            "- [Funding Detail 1]\n"
            "- [Funding Detail 2]\n\n"
            "Market summary:\n"
            "[A concise analytical overview of the industry status, growth drivers, and outlook.]"
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    # Create tool calling agent
    agent = create_tool_calling_agent(llm, tools, prompt)
    
    # Create agent executor
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=tools, 
        verbose=True, 
        handle_parsing_errors=True
    )
    
    return agent_executor