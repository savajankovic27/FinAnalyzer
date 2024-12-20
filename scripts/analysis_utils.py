"""
analysis_utils.py

General utility functions for data analysis, such as outlier removal, normalization, and summary statistics.
"""

import pandas as pd

def compute_summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
    ##Stats analyzed. 
    stats = df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']].describe()
    return stats

def add_returns(df: pd.DataFrame) -> pd.DataFrame:
    ## daily returns
    df['Daily_Return'] = df['Adj Close'].pct_change()
    return df
