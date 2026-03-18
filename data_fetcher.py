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
    pass

# Standalone function for direct use
def fetch_fundamentals(ticker: str) -> dict:
    """
    Standalone function to fetch fundamentals without LangChain tool wrapper.
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        data = {
            # =========================
            # 🔹 BASIC INFO
            # =========================
            'NAME': info.get('longName'),
            'TICKER': ticker,
            'CMP': info.get('currentPrice'),

            # =========================
            # 🔹 VALUATION
            # =========================
            'PE': round(info.get('trailingPE'), 2) if info.get('trailingPE') else None,
            'forwardPE': info.get('forwardPE'),
            'pegRatio': info.get('pegRatio'),
            'priceToBook': info.get('priceToBook'),

            # =========================
            # 🔹 PROFITABILITY
            # =========================
            'EPS': info.get('trailingEps'),
            'ROE%': (info.get('returnOnEquity') * 100) if info.get('returnOnEquity') else None,
            'ROA%': (info.get('returnOnAssets') * 100) if info.get('returnOnAssets') else None,
            'PROFIT%': (info.get('profitMargins') * 100) if info.get('profitMargins') else None,
            'OPERATING_MARGIN%': (info.get('operatingMargins') * 100) if info.get('operatingMargins') else None,

            # =========================
            # 🔹 GROWTH
            # =========================
            'REVENUE': info.get('totalRevenue'),
            'REVENUE_GROWTH%': (info.get('revenueGrowth') * 100) if info.get('revenueGrowth') else None,
            'EARNINGS_GROWTH%': (info.get('earningsGrowth') * 100) if info.get('earningsGrowth') else None,

            # =========================
            # 🔹 FINANCIAL HEALTH
            # =========================
            'MARKET_CAP': info.get('marketCap'),
            'debtToEquity': info.get('debtToEquity'),
            'freeCashflow': info.get('freeCashflow'),
            'operatingCashflow': info.get('operatingCashflow'),
            'netIncome': info.get('netIncome'),
            'bookValue': info.get('bookValue'),

            # =========================
            # 🔹 MARKET & RISK
            # =========================
            'beta': info.get('beta'),
            '52W_HIGH': info.get('fiftyTwoWeekHigh'),
            '52W_LOW': info.get('fiftyTwoWeekLow'),
            'avgVolume': info.get('averageVolume'),
            'volume': info.get('volume'),

            # =========================
            # 🔹 DIVIDENDS
            # =========================
            'dividendYield%': (info.get('dividendYield') * 100) if info.get('dividendYield') else None,
            'payoutRatio': info.get('payoutRatio'),
        }

        # Filter out None values
        data = {k: v for k, v in data.items() if v is not None}

        return data
    except Exception as e:
        return {"error": f"Failed to fetch data for {ticker}: {str(e)}"}
