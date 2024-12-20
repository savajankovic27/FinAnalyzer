
import os
import pandas as pd

def load_stock_data(symbol: str, data_dir: str = "../Data") -> pd.DataFrame:
    ## Importing the data from the AAPL Csv (or any other)
    file_path = os.path.join(data_dir, f"{symbol}.csv")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No CSV found for symbol: {symbol}")
    
    df = pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")
    # Optional: Ensure data is sorted by date
    df.sort_index(inplace=True)
    return df
