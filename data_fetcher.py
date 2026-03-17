import yfinance as yf
from langchain.tools import tool

@tool
# Standalone function for direct use
def fetch_fundamentals(ticker: str) -> dict:
    """
    Standalone function to fetch fundamentals without LangChain tool wrapper.
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        def indian_format(n):
            s = str(int(n))
            last3 = s[-3:]
            rest = s[:-3]
            if rest:
                rest = ",".join([rest[max(i - 2, 0):i] for i in range(len(rest), 0, -2)][::-1])
                return rest + "," + last3
            return last3

        def format_in_crores(num):
            if num is None:
                return None
            crores = num / 1e7
            return f"₹ {indian_format(crores)} Cr"

        data = {
            'TICKER': ticker,
            'CMP': info.get('currentPrice'),
            'PE': info.get('trailingPE'),
            'EPS': info.get('trailingEps'),
            'ROE%': (info.get('returnOnEquity')*100),  # numeric

            # RAW values (for logic)
            'REVENUE_RAW': info.get('totalRevenue'),
            'MARKET_CAP_RAW': info.get('marketCap'),

            # FORMATTED values (for UI)
            'REVENUE': format_in_crores(info.get('totalRevenue')),
            'MARKET_CAP': format_in_crores(info.get('marketCap')),

            'PROFIT%': (info.get('profitMargins')*100)
        }

        # Filter out None values
        data = {k: v for k, v in data.items() if v is not None}

        return data
    except Exception as e:
        return {"error": f"Failed to fetch data for {ticker}: {str(e)}"}
