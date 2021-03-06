import pandas as pd
import numpy as np
import yfinance as yf
import pandas_datareader as pdr
import datetime as dt
import matplotlib.pyplot as plt

import sys


ticker = 'btc-usd'

now = dt.datetime.now()
startyear = 2021
startmonth = 3
startday = 4
start = dt.datetime(startyear, startmonth, startday)
df = yf.download(ticker, period="2d", interval="15m")


ShortEMA = df.Close.ewm(span=10, adjust=False).mean()
# Calculate the Long Term Exponential Moving Average
LongEMA = df.Close.ewm(span=20, adjust=False).mean()
# Calculate the Moving Average Convergence/Divergence (MACD)
MACD = ShortEMA - LongEMA
# Calcualte the signal line
signal = MACD.ewm(span=15, adjust=False).mean()


ten_ema = df.Close.ewm(span=10, adjust=False).mean()
ten_sma = df.Close.rolling(window=10).mean()

# print(ten_ema)
# print(ten_sma)


# print(MACD[MACD.size-3])
# print(MACD[MACD.size-1])


print((ten_ema[ten_ema.size - 2] - ten_ema[ten_ema.size - 3]) / 15)
print((MACD[MACD.size - 2] - MACD[MACD.size - 3]) / 15)


fig, (ax1, ax2) = plt.subplots(2)


ax1.plot(df.index, ten_ema, label='FB MACD', color='blue')
ax1.plot(df.index, ten_sma, label='Signal Line', color='red')
ax1.legend(loc='upper left')

ax2.plot(df.index, MACD, label='FB MACD', color='blue')
ax2.plot(df.index, signal, label='Signal Line', color='red')
ax2.legend(loc='upper left')

plt.show()
