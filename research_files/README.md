# Oil Feature Importance in Price Prediction

## Overview

This project analyzes feature importance in predicting oil price movements using financial market indicators. The goal is to understand which variables contribute most to predictive signals in a machine learning model.

The features include market and volatility indicators such as SPY, VIX, and lagged oil price values.

---

## Objective

To evaluate the relative importance of different financial indicators in forecasting oil price movement using a machine learning-based approach.

---

## Methods

- Feature engineering using lagged variables and moving averages
- Integration of market indicators (SPY, VIX, oil-related features)
- Machine learning model used for predictive analysis
- Feature importance extraction from trained model
- Performance evaluation on historical data

---

## Key Findings

- Lagged oil features contribute significantly to predictive performance in medium volatility regimes.
- Volatility indicators (e.g., VIX) show meaningful influence on model output, but do not dominate.
- Equity market signals (e.g., SPY) provide dominant predictive signal in stable and crisis regimes.

---

## Limitations

- Limited dataset range
- No incorporation of macroeconomic or geopolitical variables
- Model performance may vary across different market regimes
- Results are not intended as financial advice

---

## Files

- `paper.pdf` → Full research paper

---

## Notes

This is an independent student research project exploring machine learning applications in financial time series analysis.
