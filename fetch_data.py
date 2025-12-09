import requests
import pandas as pd
from db_config import get_connection

API_KEY = "DH0X57JCH9WH0VBR"
SYMBOL = "AAPL"  # Example stock

def fetch_stock_data(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}&outputsize=compact"
    response = requests.get(url)
    data = response.json()

    if "Time Series (Daily)" not in data:
        print("Error fetching data:", data)
        return None

    df = pd.DataFrame(data["Time Series (Daily)"]).T
    df.columns = ["open", "high", "low", "close", "volume"]
    df.index.name = "date"
    df.reset_index(inplace=True)
    df = df.astype({"open": float, "high": float, "low": float, "close": float, "volume": int})
    return df

def store_data(df, symbol):
    conn = get_connection()
    cur = conn.cursor()
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO stock_prices (symbol, date, open, high, low, close, volume)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE 
                open=VALUES(open),
                high=VALUES(high),
                low=VALUES(low),
                close=VALUES(close),
                volume=VALUES(volume);
        """, (symbol, row["date"], row["open"], row["high"], row["low"], row["close"], row["volume"]))
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    df = fetch_stock_data(SYMBOL)
    if df is not None:
        store_data(df, SYMBOL)
        print("Data stored successfully.")
