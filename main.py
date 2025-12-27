from src.config import get_config
from src.data_loader import load_and_prepare_data
from src.returns import compute_log_returns
from src.correlation import average_pairwise_correlation
from src.regimes import classify_regimes
from src.portfolios import (
    equal_weight_portfolio,
    mean_variance_portfolio,
    risk_parity_portfolio,
    volatility_targeted_portfolio,
    portfolio_returns,
)
from src.risk import max_drawdown, sharpe_ratio


def run_pipeline(config):
    prices = load_and_prepare_data(
        config["tickers"],
        config["start_date"],
        config["end_date"],
    )

    returns = compute_log_returns(prices)

    avg_corr = average_pairwise_correlation(
        returns,
        config["rolling_window"],
    )

    regimes = classify_regimes(
        avg_corr,
        config["low_regime_quantile"],
        config["high_regime_quantile"],
    )

    ew_weights = equal_weight_portfolio(returns)
    mv_weights = mean_variance_portfolio(
        returns,
        config["risk_aversion"],
    )
    rp_weights = risk_parity_portfolio(returns)
    vt_weights = volatility_targeted_portfolio(
        returns,
        config["vol_target"],
        config["trading_days"],
    )

    ew_returns = portfolio_returns(returns, ew_weights)
    mv_returns = portfolio_returns(returns, mv_weights)
    rp_returns = portfolio_returns(returns, rp_weights)
    vt_returns = portfolio_returns(returns, vt_weights)

    results = {
        "equal_weight": {
            "sharpe": sharpe_ratio(ew_returns),
            "max_drawdown": max_drawdown(ew_returns),
        },
        "mean_variance": {
            "sharpe": sharpe_ratio(mv_returns),
            "max_drawdown": max_drawdown(mv_returns),
        },
        "risk_parity": {
            "sharpe": sharpe_ratio(rp_returns),
            "max_drawdown": max_drawdown(rp_returns),
        },
        "vol_targeted": {
            "sharpe": sharpe_ratio(vt_returns),
            "max_drawdown": max_drawdown(vt_returns),
        },
    }

    return results, regimes


if __name__ == "__main__":
    config = get_config()
    run_pipeline(config)