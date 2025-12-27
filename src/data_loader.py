import os
import pandas as pd

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "prices.csv")

def download_price_data(tickers, start_date, end_date):
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(
            f"prices.csv not found at {DATA_PATH}. Please place it in the data/ directory."
        )

    prices = pd.read_csv(
        DATA_PATH,
        index_col=0,
        parse_dates=True
    )

    return prices

def load_and_prepare_data(tickers, start_date, end_date):
    prices = download_price_data(tickers, start_date, end_date)
    return prices.ffill()