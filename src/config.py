def get_config():
    return {
        "tickers": ["SPY", "EFA", "EEM", "IEF", "TIP", "DBC", "GLD"],
        "start_date": "2006-01-01",
        "end_date": "2024-12-31",
        "trading_days": 252,
        "rolling_window": 60,
        "vol_target": 0.10,
        "risk_aversion": 1.0,
        "low_regime_quantile": 0.3,
        "high_regime_quantile": 0.7,
    }