

import pandas as pd
import numpy as np

def moving_average(df: pd.DataFrame, window: int = 20, price_col: str = "Adj Close") -> pd.DataFrame:
   ## SMA in columns added
    df[f"SMA_{window}"] = df[price_col].rolling(window=window).mean()
    return df

def exponential_moving_average(df: pd.DataFrame, span: int = 20, price_col: str = "Adj Close") -> pd.DataFrame:
    """
    Compute an exponential moving average (EMA) and add it as a column to the DataFrame.
    """
    df[f"EMA_{span}"] = df[price_col].ewm(span=span, adjust=False).mean()
    return df

def relative_strength_index(df: pd.DataFrame, window: int = 14, price_col: str = "Adj Close") -> pd.DataFrame:
    """
    Compute RSI (Relative Strength Index).

    RSI measures the magnitude of recent price changes to evaluate overbought or oversold conditions.
    """
    delta = df[price_col].diff()
    gain = (delta.where(delta > 0, 0))
    loss = (-delta.where(delta < 0, 0))
    avg_gain = gain.rolling(window).mean()
    avg_loss = loss.rolling(window).mean()
    
    rs = avg_gain / avg_loss
    df["RSI"] = 100 - (100 / (1 + rs))
    return df
