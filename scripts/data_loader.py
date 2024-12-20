"""
data_loader.py

This script provides functionality to load and preprocess stock data from CSV files.
"""

import os
import pandas as pd

def load_stock_data(symbol: str, data_dir: str = "../Data") -> pd.DataFrame:
    """
    Load stock data for a given symbol from a CSV file and return a cleaned DataFrame.

    Parameters
    ----------
    symbol : str
        Stock ticker symbol (e.g. 'AAPL').
    data_dir : str, optional
        Directory where CSV files are stored, by default "../Data".

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the stock data with datetime as an index.
    """
    file_path = os.path.join(data_dir, f"{symbol}.csv")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No CSV found for symbol: {symbol}")
    
    df = pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")
    # Optional: Ensure data is sorted by date
    df.sort_index(inplace=True)
    return df
