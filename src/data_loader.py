import yfinance as yf
import pandas as pd


def download_price_data(tickers, start_date, end_date):
    data = yf.download(
        tickers,
        start=start_date,
        end=end_date,
        progress=False,
        auto_adjust=True,
    )

    if isinstance(data.columns, pd.MultiIndex):
        prices = data["Close"]
    else:
        prices = data

    return prices


def load_and_prepare_data(tickers, start_date, end_date):
    prices = download_price_data(tickers, start_date, end_date)
    prices = prices.ffill()
    prices = prices.dropna()
    return prices