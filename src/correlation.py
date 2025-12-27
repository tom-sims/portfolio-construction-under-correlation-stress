import numpy as np
import pandas as pd


def rolling_correlation(returns, window):
    return returns.rolling(window).corr()


def rolling_covariance(returns, window):
    return returns.rolling(window).cov()


def average_pairwise_correlation(returns, window):
    corr = returns.rolling(window).corr()
    assets = returns.columns
    avg_corr = []

    for date in corr.index.levels[0]:
        matrix = corr.loc[date]
        if matrix.isnull().values.any():
            avg_corr.append(np.nan)
            continue
        values = matrix.values
        n = len(assets)
        avg = (np.sum(values) - n) / (n * (n - 1))
        avg_corr.append(avg)

    return pd.Series(avg_corr, index=returns.index)


def pca_eigenvalue_share(returns, window):
    cov = returns.rolling(window).cov()
    assets = returns.columns
    share = []

    for date in cov.index.levels[0]:
        matrix = cov.loc[date]
        if matrix.isnull().values.any():
            share.append(np.nan)
            continue
        eigenvalues = np.linalg.eigvalsh(matrix.values)
        largest = np.max(eigenvalues)
        total = np.sum(eigenvalues)
        share.append(largest / total)

    return pd.Series(share, index=returns.index)