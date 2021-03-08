import yfinance as yf
import datetime as dt


ticker = 'btc-usd'

now = dt.datetime.now()
startyear = 2021
startmonth = 3
startday = 4
start = dt.datetime(startyear, startmonth, startday)
df = yf.download(ticker, period="2d", interval="15m")


short_sma = df.Close.rolling(window=10).mean()
short_ema = df.Close.ewm(span=10, adjust=False).mean()
long_ema = df.Close.ewm(span=20, adjust=False).mean()


macd = short_ema - long_ema
signal = macd.ewm(span=15, adjust=False).mean()


print(short_ema[short_ema.size - 2] - short_ema[short_ema.size - 3])
print(macd[macd.size - 2] - macd[macd.size - 3])
