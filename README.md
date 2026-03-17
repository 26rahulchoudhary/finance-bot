# AI Finance Bot

An AI-powered bot that evaluates whether a company is worth investing in based on its fundamental financial data.

## Features

- Fetches fundamental data (P/E ratio, ROE, debt-to-equity, etc.) using yfinance.
- Trains a machine learning model (Random Forest) on historical data to predict investment worth.
- Evaluates new companies and provides recommendations.

## Setup

1. Clone the repository and navigate to the project directory.
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `venv\Scripts\Activate.ps1` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run the bot: `python main.py`

## Usage

- The script collects sample data for a list of tickers, trains the model, and evaluates a specific ticker.
- Modify the tickers list in `main.py` to include more companies for training.
- Use `evaluate_investment(ticker)` to check a new company.

## Project Structure

- `main.py`: Main script containing data fetching, model training, and evaluation functions.
- `data/`: Directory for storing training data (e.g., fundamentals.csv).
- `models/`: Directory for saved trained models (e.g., investment_model.pkl).
- `src/`: (Reserved for additional source files if needed).
- `requirements.txt`: List of Python dependencies.
- `.gitignore`: Git ignore file.

## Dependencies

- yfinance: For fetching financial data.
- pandas: For data manipulation.
- scikit-learn: For machine learning model.
- numpy: For numerical operations.

## Future Improvements

- Use more comprehensive datasets for training.
- Implement backtesting for model validation.
- Add more features like technical indicators.
- Deploy as a web app or API.
