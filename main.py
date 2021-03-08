import datetime
import threading
from stock import ticker_analysis


def main():
    file = open('tickers.txt', 'w')
    for ticker in tickers:
        ticker_analysis(ticker, time_frame, file)
    file.close()

    print(datetime.datetime.now().strftime('%m/%d/%y - %H:%M'))
    threading.Timer(900, main).start()


tickers = ['dkng', 'penn', 'flux', 'gevo', 'mu', 'jmia', 'tigr', 'nndm', 'dm', 'csiq', 'lazr', 'idex', 'nio', 'riot', 'mara', 'mmm']
tickers = ['tan', 'icln', 'arkg', 'arkq', 'arkf', 'arkw', 'arkk', 'qqq', 'spyg', 'spy']
tickers = ['btc-usd', 'eth-usd']

time_frame = '30m'


main()
