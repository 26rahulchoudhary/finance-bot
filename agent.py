from langchain_openai import ChatOpenAI
from data_fetcher import get_stock_data
from analysis import analyze_fundamentals
import os
from dotenv import load_dotenv
from typing import Dict

# Load environment variables
load_dotenv()

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.1,
    openai_api_key=os.getenv("OPENAI_API_KEY")
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
        data = get_stock_data(ticker)
        if "error" in data:
            return {"error": data["error"]}

        # Generate insights
        insights = analyze_fundamentals(data)

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

        summary = llm.invoke(prompt_text).content

        return {
            "ticker": ticker,
            "data": data,
            "insights": insights,
            "summary": summary
        }

    except Exception as e:
        return {"error": f"Analysis failed: {str(e)}"}
