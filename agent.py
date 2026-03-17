from langchain_groq import ChatGroq
from data_fetcher import fetch_fundamentals
from analysis import generate_insights
import os
from dotenv import load_dotenv
from typing import Dict

# Load environment variables
load_dotenv()

# Initialize LLM
llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.1,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

def analyze_stock_with_agent(ticker: str) -> Dict:
    """
    Analyze a stock's fundamentals using direct function calls and LLM for explanation.

    Args:
        ticker (str): Stock ticker

    Returns:
        Dict: Analysis result with data, insights, and summary
    """
    try:
        # Fetch data
        data = fetch_fundamentals(ticker)
        if "error" in data:
            return {"error": data["error"]}

        # Generate insights
        insights = generate_insights(data)

        # Use LLM to generate summary
        prompt_text = f"""
        Based on the following financial data and insights for {ticker}, provide a clear, concise explanation suitable for beginners. Do not give investment advice.

        Financial Data: {data}

        Insights: {insights}

        Structure your response as:
        - Overview
        - Strengths
        - Weaknesses
        - Final Summary
        """

        # Use LLM to generate summary
        try:
            summary = llm.invoke(prompt_text).content
        except Exception as e:
            # Fallback for demo if API key is invalid
            summary = f"Demo Summary for {ticker}: Based on the data, the stock shows {len(insights)} key insights. Please set a valid GROQ_API_KEY for full LLM explanation."

        return {
            "ticker": ticker,
            "data": data,
            "insights": insights,
            "summary": summary
        }

    except Exception as e:
        return {"error": f"Analysis failed: {str(e)}"}
