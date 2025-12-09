import pandas as pd
import sys
from db_config import get_connection

def fetch_from_db(symbol):
    conn = get_connection()
    query = "SELECT date, close FROM stock_prices WHERE symbol=%s ORDER BY date;"
    df = pd.read_sql(query, conn, params=(symbol,))
    conn.close()
    return df

def moving_average(df, window=5):
    df["MA"] = df["close"].rolling(window=window).mean()
    return df

def rsi(df, periods=14):
    delta = df["close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=periods).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=periods).mean()
    rs = gain / loss
    df["RSI"] = 100 - (100 / (1 + rs))
    return df

if __name__ == "__main__":
    # Get symbol from command line or use default
    symbol = sys.argv[1] if len(sys.argv) > 1 else "AAPL"
    
    df = fetch_from_db(symbol)
    
    if df.empty:
        print(f"No data found for symbol: {symbol}")
    else:
        df = moving_average(df, 5)
        df = rsi(df, 14)
        print(df.tail())
