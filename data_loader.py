import pandas as pd
import yfinance as yf


def load_raw_data():

    print("Loading raw data...")

    tickers = ['CL=F', '^VIX', '^GSPC']
    crisis_data = yf.download(
        tickers, start='2020-02-01', end='2020-06-01', progress=False)['Close']
    normal_data = yf.download(
        tickers, start='2018-01-01', end='2019-12-01', progress=False)['Close']
    peace_data = yf.download(
        tickers, start='2015-01-01', end='2017-12-01', progress=False)['Close']

    crisis_data = crisis_data.rename(
        columns={'CL=F': 'oil', '^VIX': 'vix', '^GSPC': 'spy'})
    normal_data = normal_data.rename(
        columns={'CL=F': 'oil', '^VIX': 'vix', '^GSPC': 'spy'})
    peace_data = peace_data.rename(
        columns={'CL=F': 'oil', '^VIX': 'vix', '^GSPC': 'spy'})

    crisis_data.to_csv('raw/raw_crisis.csv')
    normal_data.to_csv('raw/raw_medium.csv')
    peace_data.to_csv('raw/raw_peaceful.csv')

    print("Success!")


load_raw_data()
