import numpy as np
import pandas as pd


def volatility(returns, periods_per_year=252):
    return returns.std() * np.sqrt(periods_per_year)


def max_drawdown(returns):
    cumulative = (1 + returns).cumprod()
    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak
    return drawdown.min()


def sharpe_ratio(returns, risk_free_rate=0.0, periods_per_year=252):
    excess = returns - risk_free_rate / periods_per_year
    return excess.mean() / excess.std() * np.sqrt(periods_per_year)


def turnover(weights):
    return weights.diff().abs().sum(axis=1)


def risk_contribution(weights, cov):
    portfolio_vol = np.sqrt(weights.T @ cov @ weights)
    marginal = cov @ weights
    return weights * marginal / portfolio_vol