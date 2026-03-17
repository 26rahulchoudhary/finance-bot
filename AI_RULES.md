# Rules for AI Finance Bot

This document outlines the rules and guidelines that govern the actions and decision-making processes of the AI Finance Bot. The bot is designed to evaluate investment worth for Indian companies listed on NSE and BSE, using a mix of rule-based systems and machine learning.

## IMPORTANT: Rules for AI Assistant Actions
- **Do not commit or push without code-owner's permission**: All Git commits and pushes must be explicitly authorized by the code owner.
- **Always read this AI_RULES readme before committing or pushing the code**: Review this document thoroughly before performing any commit or push operations to ensure compliance.

## 1. Scope and Focus
- **Market Focus**: The bot exclusively analyzes Indian companies listed on the National Stock Exchange (NSE) or Bombay Stock Exchange (BSE). Tickers must use .NS for NSE or .BO for BSE suffixes (e.g., RELIANCE.NS).
- **Data Sources**: All data is fetched from Yahoo Finance via yfinance. No other sources are used to ensure consistency.
- **Purpose**: Educational and demonstrative only. The bot does not provide financial advice; users should consult professionals.

## 2. Data Handling Rules
- **Fundamentals to Fetch**: Market cap, trailing P/E, forward P/E, return on equity (ROE), debt-to-equity, price-to-book, PEG ratio, beta, total revenue, net income, free cash flow, book value, current price.
- **Missing Data**: Drop rows with any missing values during data preparation. (Future: Implement imputation for robustness.)
- **Data Storage**: Training data saved as CSV in `data/fundamentals.csv`; models saved as pickle in `models/investment_model.pkl`.
- **Updates**: Data is fetched in real-time for evaluations; training data is static unless re-collected.

## 3. Labeling and Training Rules
- **Label Assignment**: For training data, assign label 1 (good) if ROE > 10% and trailing P/E < 20; otherwise, label 0 (bad).
- **Rationale for Labels**: ROE > 10% indicates strong profitability; P/E < 20 suggests potential undervaluation. These are heuristic thresholds tailored for Indian markets.
- **Model Algorithm**: Random Forest Classifier with 100 estimators, random_state=42 for reproducibility.
- **Training Split**: 80% training data, 20% testing data.
- **Evaluation Metric**: Accuracy score on test set; print to console.
- **Feature Selection**: Use all fetched fundamentals except 'ticker' and 'label' as features.

## 4. Evaluation and Prediction Rules
- **Input Validation**: Ticker must be a valid NSE/BSE symbol; fetch fundamentals before prediction.
- **Prediction Process**: Load trained model, preprocess input data (drop 'ticker'), predict binary outcome.
- **Output Format**: Return "Worth investing" for prediction 1, "Not worth investing" for 0.
- **Error Handling**: If model file missing, return None and print error message.
- **Real-Time Nature**: Evaluations use current data; no caching beyond the session.

## 5. Ethical and Operational Rules
- **No Guarantees**: Predictions are probabilistic and based on historical patterns; markets are unpredictable.
- **Bias Mitigation**: Training data includes diverse Indian sectors; avoid overfitting by using cross-validation in future versions.
- **Updates to Rules**: Rules can be modified via code changes, but must be documented and tested.
- **Security**: No user data stored; all operations are local.
- **Performance**: Aim for >80% accuracy on test data; retrain periodically with new data.

## 6. Future Rule Expansions
- **Additional Metrics**: Incorporate technical indicators (e.g., moving averages) or macroeconomic data.
- **Advanced Models**: Switch to neural networks or ensemble methods if accuracy improves.
- **Backtesting**: Implement historical simulation to validate rules.
- **User Customization**: Allow users to adjust thresholds via config files.

These rules ensure the AI bot operates consistently, transparently, and responsibly. For code changes, refer to main.py and update this document accordingly.
