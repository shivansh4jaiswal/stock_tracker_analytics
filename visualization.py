import plotly.graph_objects as go
from analysis import fetch_from_db, moving_average, rsi

symbol = "AAPL"
df = fetch_from_db(symbol)
df = moving_average(df, 5)
df = rsi(df, 14)

fig = go.Figure(data=[go.Candlestick(
    x=df['date'],
    open=df['close'],
    high=df['close'],
    low=df['close'],
    close=df['close'],
    name="Price"
)])

fig.add_trace(go.Scatter(x=df['date'], y=df['MA'], mode='lines', name='Moving Average'))
fig.show()

fig2 = go.Figure(data=[go.Scatter(x=df['date'], y=df['RSI'], mode='lines', name='RSI')])
fig2.show()
