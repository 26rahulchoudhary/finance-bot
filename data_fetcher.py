import yfinance as yf
from langchain.tools import tool

@tool
def get_stock_data(ticker: str) -> dict:
    """
    Fetch fundamental financial data for a given stock ticker using yfinance.

    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL', 'TCS.NS')

    Returns:
        dict: Dictionary containing key financial metrics
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        data = {
            'ticker': ticker,
            'current_price': info.get('currentPrice'),
            'pe_ratio': info.get('trailingPE'),
            'eps': info.get('trailingEps'),
            'roe': info.get('returnOnEquity'),
            'revenue': info.get('totalRevenue'),
            'profit_margin': info.get('profitMargins'),
            'market_cap': info.get('marketCap')
        }

        # Filter out None values
        data = {k: v for k, v in data.items() if v is not None}

        return data
    except Exception as e:
        return {"error": f"Failed to fetch data for {ticker}: {str(e)}"}

# Standalone function for direct use
def fetch_fundamentals(ticker: str) -> dict:
    """
    Standalone function to fetch fundamentals without LangChain tool wrapper.
    """
    return get_stock_data(ticker)
