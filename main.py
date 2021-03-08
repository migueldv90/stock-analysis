import threading
from stock import ticker_analysis


def main():
    start_time = threading.Timer(5, main).start()

    file = open('tickers.txt', 'w')
    for ticker in tickers:
        ticker_analysis(ticker, file)
    file.close()


tickers = ['k', 'nio']
main()
