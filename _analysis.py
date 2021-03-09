import datetime
import threading
from ticker.analysis import ticker_analysis

from tickers.robinhood import tickers
from tickers.watchlist import tickers
from tickers.etfs import tickers
from tickers.qqq import tickers


def main():
    file = open('tickers.txt', 'w')
    for ticker in tickers:
        ticker_analysis(ticker, time_period, time_interval, file)
    file.close()

    print(datetime.datetime.now().strftime('%m/%d/%y - %H:%M'))
    threading.Timer(1800, main).start()


time_period = '30d'
time_interval = '1d'


main()
