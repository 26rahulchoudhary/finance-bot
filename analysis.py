from typing import List, Dict
from langchain.tools import tool

@tool
def analyze_fundamentals(data: Dict) -> List[str]:
    """
    Perform rule-based analysis on financial data to generate insights.

    Args:
        data (dict): Financial data from get_stock_data

    Returns:
        List[str]: List of insights based on rules
    """
    insights = []

    # Valuation analysis
    pe = data.get('pe_ratio')
    if pe:
        if pe < 15:
            insights.append("Stock appears potentially undervalued (low P/E ratio)")
        elif pe > 25:
            insights.append("Stock appears potentially overvalued (high P/E ratio)")
        else:
            insights.append("P/E ratio is in a reasonable range")

    # Profitability analysis
    roe = data.get('roe')
    if roe:
        if roe > 15:
            insights.append("Company shows strong profitability (high ROE)")
        elif roe < 5:
            insights.append("Company profitability is concerning (low ROE)")
        else:
            insights.append("Profitability is moderate")

    # Growth analysis (simplified, as we don't have trends)
    revenue = data.get('revenue')
    if revenue:
        # For simplicity, assume positive if revenue exists and is high
        if revenue > 1e9:  # Arbitrary threshold
            insights.append("Company has significant revenue scale")
        else:
            insights.append("Revenue is modest")

    # Market cap insight
    market_cap = data.get('market_cap')
    if market_cap:
        if market_cap > 1e11:  # Large cap
            insights.append("Large-cap company with stability")
        elif market_cap < 1e9:
            insights.append("Small-cap company with growth potential")

    # EPS insight
    eps = data.get('eps')
    if eps and eps > 0:
        insights.append("Positive earnings per share")
    elif eps and eps < 0:
        insights.append("Negative earnings per share (potential concern)")

    # Profit margin
    margin = data.get('profit_margin')
    if margin:
        if margin > 0.1:
            insights.append("Strong profit margins")
        elif margin < 0.05:
            insights.append("Thin profit margins")

    return insights

# Standalone function
def generate_insights(data: Dict) -> List[str]:
    """
    Standalone function for analysis.
    """
    return analyze_fundamentals(data)
