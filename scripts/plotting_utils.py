
import matplotlib.pyplot as plt

def plot_prices(df, symbol, show_sma=None, show_ema=None):
    ## Different plotting figured, addition of adjacent closures. 
    plt.figure(figsize=(12,6))
    plt.plot(df['Adj Close'], label='Adj Close', linewidth=2)
    
    if show_sma:
        for w in show_sma:
            sma_col = f"SMA_{w}"
            if sma_col in df.columns:
                plt.plot(df[sma_col], label=f"SMA {w}")
    
    if show_ema:
        for e in show_ema:
            ema_col = f"EMA_{e}"
            if ema_col in df.columns:
                plt.plot(df[ema_col], label=f"EMA {e}")
    
    plt.title(f"{symbol} Price Over Time")
    plt.xlabel("Date")
    plt.ylabel("Adjusted Close Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.show()
