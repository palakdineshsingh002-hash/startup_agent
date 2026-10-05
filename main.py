import sys
from agent import build_market_intelligence_agent

def main():
    print("=== AI Market Intelligence Agent ===")
    
    # Accept industry input from user or default to fintech
    industry = input("Enter the industry to analyze (default 'fintech'): ").strip()
    if not industry:
        industry = "fintech"
        
    print(f"\nInitializing agent and analyzing industry: {industry.upper()}...\n")
    
    try:
        agent_executor = build_market_intelligence_agent()
        
        # Formulate query
        query = (
            f"Conduct comprehensive market research on the {industry} industry. "
            f"Find top leading startups, latest technology and market trends, recent prominent funding rounds, "
            f"and provide an executive market summary."
        )
        
        # Run agent
        response = agent_executor.invoke({
            "input": query,
            "chat_history": []
        })
        
        print("\n" + "="*40)
        print("FINAL MARKET INTELLIGENCE REPORT")
        print("="*40 + "\n")
        print(response.get("output", "No output generated."))
        
    except Exception as e:
        print(f"\nError running the agent: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()