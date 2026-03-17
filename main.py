import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import os
from agent import analyze_stock_with_agent

def get_fundamentals(ticker):
    """
    Fetch fundamental data for a given ticker using yfinance.
    """
    stock = yf.Ticker(ticker)
    info = stock.info
    fundamentals = {
        'ticker': ticker,
        'marketCap': info.get('marketCap'),
        'trailingPE': info.get('trailingPE'),
        'forwardPE': info.get('forwardPE'),
        'returnOnEquity': info.get('returnOnEquity'),
        'debtToEquity': info.get('debtToEquity'),
        'priceToBook': info.get('priceToBook'),
        'pegRatio': info.get('pegRatio'),
        'beta': info.get('beta'),
        'totalRevenue': info.get('totalRevenue'),
        'netIncome': info.get('netIncome'),
        'freeCashflow': info.get('freeCashflow'),
        'bookValue': info.get('bookValue'),
        'currentPrice': info.get('currentPrice'),
    }
    return fundamentals

def prepare_data(fundamentals_list):
    """
    Prepare data for training: handle missing values, normalize, etc.
    """
    df = pd.DataFrame(fundamentals_list)
    df = df.dropna()  # Simple drop na, in real, impute
    # For simplicity, assume we have labels, but need to add
    # Here, we need historical data with labels (e.g., if stock went up or down)
    # For demo, let's assume random labels or something, but better to collect data
    return df

def train_model(data_path='data/fundamentals.csv'):
    """
    Train a model on prepared data.
    """
    if not os.path.exists(data_path):
        print("Data file not found. Please prepare data first.")
        return None
    df = pd.read_csv(data_path)
    # Assume df has 'label' column: 1 for good investment, 0 for bad
    X = df.drop(['ticker', 'label'], axis=1)
    y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print(f"Model accuracy: {accuracy_score(y_test, predictions)}")
    # Save model
    with open('models/investment_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    return model

def evaluate_investment(ticker, model_path='models/investment_model.pkl'):
    """
    Evaluate if a company is worth investing based on fundamentals.
    """
    fundamentals = get_fundamentals(ticker)
    df = pd.DataFrame([fundamentals])
    df = df.drop('ticker', axis=1)
    # Load model
    if not os.path.exists(model_path):
        print("Model not found. Please train the model first.")
        return None
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    prediction = model.predict(df)[0]
    return "Worth investing" if prediction == 1 else "Not worth investing"

def collect_sample_data(tickers, output_path='data/fundamentals.csv'):
    """
    Collect fundamentals for a list of tickers and assign labels based on simple rules.
    """
    data = []
    for ticker in tickers:
        try:
            fund = get_fundamentals(ticker)
            # Simple rule: if ROE > 10 and trailingPE < 20, label 1 (good), else 0
            roe = fund.get('returnOnEquity', 0) or 0
            pe = fund.get('trailingPE', 100) or 100
            label = 1 if roe > 10 and pe < 20 else 0
            fund['label'] = label
            data.append(fund)
        except Exception as e:
            print(f"Error fetching {ticker}: {e}")
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")

if __name__ == "__main__":
    # Ask user for stock ticker input
    ticker = input("Enter the stock ticker (e.g., TCS.NS, AAPL): ").strip().upper()
    if not ticker:
        print("No ticker provided. Exiting.")
        exit(1)

    result = analyze_stock_with_agent(ticker)
    print('Ticker:', result.get('ticker'))
    print('Data:', result.get('data'))
    print('Insights:', result.get('insights'))
    print('Summary:', result.get('summary'))
