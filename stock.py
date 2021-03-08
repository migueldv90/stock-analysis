from datetime import datetime, timedelta
import yfinance as yf


ticker = 'btc-usd'


data = yf.download(ticker, period="1d", interval="1h")


short_sma = data.Close.rolling(window=10).mean()
short_ema = data.Close.ewm(span=10, adjust=False).mean()
long_ema = data.Close.ewm(span=20, adjust=False).mean()


macd = short_ema - long_ema
signal = macd.ewm(span=15, adjust=False).mean()


print(short_ema[short_ema.size - 2] - short_ema[short_ema.size - 3])
print(macd[macd.size - 2] - macd[macd.size - 3])
