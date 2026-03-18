import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import os
from agent import analyze_stock_with_agent


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
