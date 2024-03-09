import numpy as np
import pandas as pd
import datetime
from pathlib import Path

validation_split = datetime.datetime(2022, 8, 31)

def load_data():
    df = (pd.read_csv(Path('data') / 'data.csv', parse_dates=['date'], index_col='date')
          .asfreq('B')
          .sort_index())
    
    y = df['Close_BTC']
    X = df.drop(columns=['Close_BTC'])
    
    # Offset features by one day.
    # This transformation is quite important as we don't have exog(t) when trying to predict y(t).
    # We need to match exog(t-1) with y(t) in order to fit model.
    # This data preparation step is illustrated here : https://joaquinamatrodrigo.github.io/skforecast/0.11.0/user_guides/exogenous-variables.html
    X = X.shift(1)
    X = X.iloc[1:]
    y = y.iloc[1:]

    return X, y

if __name__ == '__main__':
    pass