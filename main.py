import datetime
import threading
from ticker.analysis import ticker_analysis
from tickers.robinhood import tickers


def main():
    file = open('tickers.txt', 'w')
    for ticker in tickers:
        ticker_analysis(ticker, time_frame, file)
    file.close()

    print(datetime.datetime.now().strftime('%m/%d/%y - %H:%M'))
    threading.Timer(1800, main).start()


time_frame = '1d'


main()
