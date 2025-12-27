import numpy as np
import pandas as pd


def classify_regimes(metric, low_quantile=0.3, high_quantile=0.7):
    low_threshold = metric.quantile(low_quantile)
    high_threshold = metric.quantile(high_quantile)

    regimes = pd.Series(index=metric.index, dtype="object")

    regimes[metric <= low_threshold] = "low"
    regimes[(metric > low_threshold) & (metric <= high_threshold)] = "medium"
    regimes[metric > high_threshold] = "high"

    return regimes


def encode_regimes(regimes):
    mapping = {"low": 0, "medium": 1, "high": 2}
    return regimes.map(mapping)