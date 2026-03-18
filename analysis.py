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
    pass

# Standalone function
def generate_insights(data):
    insights = []

    # =========================
    # 🔹 VALUATION ANALYSIS
    # =========================
    pe = data.get('PE')
    forward_pe = data.get('forwardPE')
    peg = data.get('pegRatio')

    if pe is not None:
        if pe < 15:
            insights.append("Stock appears potentially undervalued (low P/E ratio)")
        elif pe > 25:
            insights.append("Stock appears potentially overvalued (high P/E ratio)")
        else:
            insights.append("P/E ratio is in a reasonable range")

    if peg is not None:
        if peg < 1:
            insights.append("PEG ratio suggests undervaluation relative to growth")
        elif peg > 2:
            insights.append("PEG ratio indicates the stock may be expensive for its growth")

    # =========================
    # 🔹 PROFITABILITY ANALYSIS
    # =========================
    roe = data.get('ROE%')
    roa = data.get('ROA%')
    margin = data.get('PROFIT%')
    op_margin = data.get('OPERATING_MARGIN%')

    if roe is not None:
        if roe > 15:
            insights.append("Company shows strong profitability (high ROE)")
        elif roe < 5:
            insights.append("Company profitability is concerning (low ROE)")

    if roa is not None and roa > 10:
        insights.append("Efficient asset utilization (high ROA)")

    if margin is not None:
        if margin > 10:
            insights.append("Strong profit margins")
        elif margin < 5:
            insights.append("Thin profit margins")

    if op_margin is not None and op_margin > 15:
        insights.append("Strong operating efficiency")

    # =========================
    # 🔹 GROWTH ANALYSIS
    # =========================
    revenue_growth = data.get('REVENUE_GROWTH%')
    earnings_growth = data.get('EARNINGS_GROWTH%')

    if revenue_growth is not None:
        if revenue_growth > 10:
            insights.append("Company is showing strong revenue growth")
        elif revenue_growth < 0:
            insights.append("Revenue is declining")

    if earnings_growth is not None:
        if earnings_growth > 10:
            insights.append("Earnings are growing strongly")
        elif earnings_growth < 0:
            insights.append("Earnings are declining")

    # =========================
    # 🔹 SCALE (SIZE)
    # =========================
    market_cap = data.get('MARKET_CAP')

    if market_cap is not None:
        if market_cap > 1e11:
            insights.append("Large-cap company with stability")
        elif market_cap < 1e9:
            insights.append("Small-cap company with high growth potential (and risk)")

    # =========================
    # 🔹 FINANCIAL HEALTH
    # =========================
    debt = data.get('debtToEquity')
    fcf = data.get('freeCashflow')

    if debt is not None:
        if debt > 150:
            insights.append("High debt levels may be a concern")
        elif debt < 50:
            insights.append("Company has low debt (financially stable)")

    if fcf is not None:
        if fcf > 0:
            insights.append("Company generates positive free cash flow")
        else:
            insights.append("Negative free cash flow (watch closely)")

    # =========================
    # 🔹 EPS
    # =========================
    eps = data.get('EPS')
    if eps is not None:
        if eps > 0:
            insights.append("Positive earnings per share")
        else:
            insights.append("Negative earnings per share (potential concern)")

    # =========================
    # 🔹 RISK & MARKET BEHAVIOR
    # =========================
    beta = data.get('beta')
    if beta is not None:
        if beta > 1.2:
            insights.append("Stock is more volatile than the market (high beta)")
        elif beta < 0.8:
            insights.append("Stock is less volatile than the market (defensive)")

    # =========================
    # 🔹 PRICE CONTEXT
    # =========================
    high_52 = data.get('52W_HIGH')
    low_52 = data.get('52W_LOW')
    cmp = data.get('CMP')

    if all(v is not None for v in [high_52, low_52, cmp]):
        if cmp > 0.9 * high_52:
            insights.append("Stock is trading near its 52-week high (strong momentum)")
        elif cmp < 1.1 * low_52:
            insights.append("Stock is near its 52-week low (possible value or weakness)")

    return insights