import yfinance


ticker = 'btc-usd'


data = yfinance.download(ticker, period="3d", interval="1h")


short_sma = data.Close.rolling(window=10).mean()
short_ema = data.Close.ewm(span=10, adjust=False).mean()
long_ema = data.Close.ewm(span=20, adjust=False).mean()


macd = short_ema - long_ema
signal = macd.ewm(span=15, adjust=False).mean()


print('Ticker:')
print(ticker)

print('Price:')
print(data.Close[data.Close.size - 1])

print('Macd:')
print(macd[macd.size - 1])

print('Velocity:')
print(macd[macd.size - 1] - macd[macd.size - 2])
