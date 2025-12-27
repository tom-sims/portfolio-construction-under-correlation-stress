import numpy as np
import pandas as pd
from scipy.optimize import minimize


def equal_weight_portfolio(returns):
    n = returns.shape[1]
    weights = np.repeat(1 / n, n)
    return pd.Series(weights, index=returns.columns)


def mean_variance_portfolio(returns, risk_aversion=1.0):
    mu = returns.mean().values
    cov = returns.cov().values
    n = len(mu)

    def objective(w):
        return -w @ mu + risk_aversion * w @ cov @ w

    constraints = [{"type": "eq", "fun": lambda w: np.sum(w) - 1}]
    bounds = [(0, 1) for _ in range(n)]
    w0 = np.repeat(1 / n, n)

    result = minimize(objective, w0, bounds=bounds, constraints=constraints)

    return pd.Series(result.x, index=returns.columns)


def risk_parity_portfolio(returns):
    cov = returns.cov().values
    n = cov.shape[0]

    def portfolio_risk(w):
        return np.sqrt(w @ cov @ w)

    def risk_contribution(w):
        total_risk = portfolio_risk(w)
        marginal = cov @ w
        return w * marginal / total_risk

    def objective(w):
        rc = risk_contribution(w)
        return np.sum((rc - rc.mean()) ** 2)

    constraints = [{"type": "eq", "fun": lambda w: np.sum(w) - 1}]
    bounds = [(0, 1) for _ in range(n)]
    w0 = np.repeat(1 / n, n)

    result = minimize(objective, w0, bounds=bounds, constraints=constraints)

    return pd.Series(result.x, index=returns.columns)

def volatility_targeted_portfolio(returns, vol_target, trading_days, avg_corr):
    vol = returns.std() * (trading_days ** 0.5)
    vol = vol.clip(lower=1e-4)

    stress_multiplier = 1 - avg_corr.mean()
    stress_multiplier = max(stress_multiplier, 0.3)

    effective_vol_target = vol_target * stress_multiplier

    weights = effective_vol_target / vol
    weights = weights / weights.sum()

    return weights

def portfolio_returns(returns, weights):
    return returns @ weights