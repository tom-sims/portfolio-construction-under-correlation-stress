import numpy as np
import pandas as pd


def compute_log_returns(prices):
    log_prices = np.log(prices)
    log_returns = log_prices.diff()
    log_returns = log_returns.dropna()
    return log_returns


def compute_simple_returns(prices):
    simple_returns = prices.pct_change()
    simple_returns = simple_returns.dropna()
    return simple_returns


def annualise_return(returns, periods_per_year=252):
    mean_returns = returns.mean()
    annualised_returns = mean_returns * periods_per_year
    return annualised_returns


def annualise_volatility(returns, periods_per_year=252):
    volatility = returns.std()
    annualised_volatility = volatility * np.sqrt(periods_per_year)
    return annualised_volatility