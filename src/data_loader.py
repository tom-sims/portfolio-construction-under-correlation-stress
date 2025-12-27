import pandas as pd
import os


def download_price_data(tickers, start_date, end_date):
    cache_file = "data/prices.csv"

    if not os.path.exists(cache_file):
        raise FileNotFoundError(
            "prices.csv not found. Please place it in the data/ directory."
        )

    prices = pd.read_csv(
        cache_file,
        index_col=0,
        parse_dates=True
    )

    return prices


def load_and_prepare_data(tickers, start_date, end_date):
    prices = download_price_data(tickers, start_date, end_date)
    return prices.ffill()