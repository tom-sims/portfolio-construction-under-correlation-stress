from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
CACHE_FILE = DATA_DIR / "prices.csv"


def download_price_data(tickers, start_date, end_date):
    if not CACHE_FILE.exists():
        raise FileNotFoundError(
            "prices.csv not found. Please place it in the data/ directory."
        )

    prices = pd.read_csv(
        CACHE_FILE,
        index_col=0,
        parse_dates=True
    )

    return prices


def load_and_prepare_data(tickers, start_date, end_date):
    prices = download_price_data(tickers, start_date, end_date)
    return prices.ffill()