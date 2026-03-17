# AI Finance Bot

An AI-powered bot that evaluates whether a company is worth investing in based on its fundamental financial data, focusing on Indian companies listed on NSE and BSE.

## Features

- Fetches fundamental data (P/E ratio, ROE, debt-to-equity, etc.) using yfinance for Indian stocks (e.g., RELIANCE.NS).
- Trains a machine learning model (Random Forest) on sample data to predict investment worth.
- Evaluates new companies and provides recommendations.

## Setup

1. Clone the repository and navigate to the project directory.
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `venv\Scripts\Activate.ps1` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Set up environment variables: Copy `.env` and add your OpenAI API key (OPENAI_API_KEY).
6. Run the bot: `python main.py` or start the API with `python api.py`

## Usage

- The script collects sample data for a list of Indian tickers, trains the model, and evaluates a specific ticker.
- Modify the tickers list in `main.py` to include more NSE/BSE companies (use .NS for NSE, .BO for BSE).
- Use `evaluate_investment(ticker)` to check a new company.

## API Usage

Start the FastAPI server:

```
python api.py
```

Then, access `http://localhost:8000/analyze/{ticker}` (e.g., `http://localhost:8000/analyze/TCS.NS`)

Response format:

```json
{
  "ticker": "TCS.NS",
  "data": {
    "current_price": 3500.0,
    "pe_ratio": 25.0,
    "eps": 140.0,
    "roe": 0.35,
    "revenue": 200000000000,
    "profit_margin": 0.22,
    "market_cap": 1200000000000
  },
  "insights": [
    "Stock appears potentially overvalued (high P/E ratio)",
    "Company shows strong profitability (high ROE)",
    "Company has significant revenue scale",
    "Large-cap company with stability",
    "Positive earnings per share",
    "Strong profit margins"
  ],
  "summary": "LLM-generated explanation with Overview, Strengths, Weaknesses, Final Summary"
}
```

## Project Structure

- `main.py`: Main script containing data fetching, model training, and evaluation functions.
- `data_fetcher.py`: Module for fetching stock data using yfinance, with LangChain tool.
- `analysis.py`: Rule-based analysis engine to generate insights.
- `agent.py`: LangChain agent setup with tools for automated analysis.
- `api.py`: FastAPI application providing REST API for stock analysis.
- `data/`: Directory for storing training data (e.g., fundamentals.csv).
- `models/`: Directory for saved trained models (e.g., investment_model.pkl).
- `src/`: (Reserved for additional source files if needed).
- `requirements.txt`: List of Python dependencies.
- `.gitignore`: Git ignore file.
- `.env`: Environment variables (API keys).

## Dependencies

- yfinance: For fetching financial data.
- pandas: For data manipulation.
- scikit-learn: For machine learning model.
- numpy: For numerical operations.
- matplotlib: For potential visualizations.
- langchain: For agent framework.
- openai: For LLM integration.
- fastapi: For API framework.
- uvicorn: For running the API server.
- python-dotenv: For loading environment variables.

## Future Improvements

- Use more comprehensive datasets for training.
- Implement backtesting for model validation.
- Add more features like technical indicators.
- Deploy as a web app or API.
