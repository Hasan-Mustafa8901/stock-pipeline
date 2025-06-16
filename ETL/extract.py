import pandas as pd
import yfinance as yf
import os

def data_extractor():

    TICKERS = ['TATASTEEL.NS','RELIANCE.NS','ADANIPORTS.NS']
    start_date = '2020-01-01'
    end_date = '2024-12-31'

    if os.path.exists('data/raw'):
        os.makedirs('data/raw')


    for ticker in TICKERS:
        try:
            print(f'Downloading {ticker} data....')
            data = yf.download(ticker, start=start_date, end=end_date,auto_adjust=True)
            
            if not data.empty:
                data['Ticker'] = ticker
                data.to_csv(f'data/raw/{ticker}.csv')
                print(f'Saved at data/raw/{ticker}.csv')
            else:
                print(f'No Data from {ticker}.')

        except Exception as e:
            print(f'Error while fetching data for {ticker}: {e}')

if __name__ == '__main__':
    data_extractor()
            

