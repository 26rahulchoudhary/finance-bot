from fastapi import FastAPI, HTTPException
from agent import analyze_stock_with_agent
from typing import Dict

app = FastAPI(title="AI Stock Analysis Agent", version="1.0.0")

@app.get("/analyze/{ticker}")
async def analyze_stock(ticker: str) -> Dict:
    """
    Analyze a stock's fundamentals.

    Args:
        ticker (str): Stock ticker symbol

    Returns:
        Dict: Analysis result
    """
    result = analyze_stock_with_agent(ticker)

    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])

    return result

@app.get("/")
async def root():
    return {"message": "AI Stock Analysis Agent API", "endpoint": "/analyze/{ticker}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
