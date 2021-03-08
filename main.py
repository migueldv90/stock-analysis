import threading
from stock import ticker_analysis


tickers = ['k']


def main():
    start_time = threading.Timer(5, main).start()
    for ticker in tickers:
        ticker_analysis(ticker)


main()
