import pandas as pd


def engineer_features(df):

    df['oil_ma_5'] = df['oil'].rolling(5).mean()
    df['oil_ma_20'] = df['oil'].rolling(20).mean()
    df['oil_lag_1'] = df['oil'].shift(1)
    df['oil_lag_5'] = df['oil'].shift(5)

    df['spy_ma_5'] = df['spy'].rolling(5).mean()
    df['spy_ma_20'] = df['spy'].rolling(20).mean()
    df['spy_lag_1'] = df['spy'].shift(1)
    df['spy_lag_5'] = df['spy'].shift(5)

    df['vix_ma_5'] = df['vix'].rolling(5).mean()
    df['vix_ma_20'] = df['vix'].rolling(20).mean()
    df['vix_lag_1'] = df['vix'].shift(1)
    df['vix_lag_5'] = df['vix'].shift(5)

    df['target'] = (df['oil'].shift(-1) - df['oil'] > 0).astype(int)

    df = df.dropna()
    df = df.sort_values("Date")
    df = df.reset_index(drop=True)

    return df


def organize_data():

    print('Engineering features...')

    crisis = pd.read_csv('raw/raw_crisis.csv')
    medium = pd.read_csv('raw/raw_medium.csv')
    peaceful = pd.read_csv('raw/raw_peaceful.csv')

    crisis = engineer_features(crisis)
    medium = engineer_features(medium)
    peaceful = engineer_features(peaceful)

    crisis.to_csv('processed/crisis_features.csv')
    medium.to_csv('processed/medium_features.csv')
    peaceful.to_csv('processed/peaceful_features.csv')

    print('Success!')


organize_data()
