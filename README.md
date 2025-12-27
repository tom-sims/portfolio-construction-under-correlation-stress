# Portfolio Construction Under Correlation Stress

This project looks at how different portfolio construction methods behave when correlations between assets change, particularly during periods of market stress when diversification tends to break down.

Using historical ETF data covering equities, bonds, commodities, and inflation-linked assets, the project analyses how correlations evolve over time and how this affects portfolio risk and performance. The main focus is on understanding what happens to common portfolio strategies when correlations rise.

## Project Overview

The main aims of this project are:
- To analyse how average pairwise correlations change over time
- To classify different correlation regimes (low, medium, high)
- To construct portfolios using a range of allocation methods
- To compare portfolio performance under different correlation conditions
- To explore weaknesses in risk-based strategies during stressed markets

## Portfolio Construction Methods

The following portfolio allocation methods are implemented and compared:

- Equal Weight  
- Mean–Variance Optimisation  
- Risk Parity  
- Volatility Targeting (with correlation awareness)  

Portfolio performance is evaluated using:
- Annualised return  
- Volatility  
- Sharpe ratio  
- Maximum drawdown  

## Repository Structure
```
portfolio-construction-under-correlation-stress/
│
├── src/
│   ├── config.py
│   ├── data_loader.py
│   ├── returns.py
│   ├── correlation.py
│   ├── regimes.py
│   ├── portfolios.py
│   └── risk.py
│
├── notebooks/
│   ├── 00_run_full_analysis.ipynb
│   ├── data_and_returns.ipynb
│   ├── correlation_and_regimes.ipynb
│   ├── portfolio_construction.ipynb
│   └── stress_testing_and_results.ipynb
│
├── data/
│   └── prices.csv
│
├── main.py
├── requirements.txt
└── README.md
```
## How to Run the Project

### Set up the environment

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Data
The project expects a CSV file containing historical adjusted close prices:
data/prices.csv
This file is not included in the repository and should be generated locally (e.g. via yfinance).
### Run the full analysis
Open and run:
notebooks/run_full_analysis.ipynb
This notebook:
- Loads the data
- Computes returns
- Estimates correlation regimes
- Constructs portfolios
- Evaluates performance
- Produces all plots and summary tables

## Notes on the Notebooks
run_full_analysis.ipynb is the main entry point and runs the full analysis
The other notebooks are exploratory and were used during development
Exploratory notebooks may rely on variables created by the full pipeline

## Key Takeaways
- Portfolio diversification weakens significantly during high-correlation periods
- Risk-based allocation methods can become unstable under market stress
- Volatility targeting without accounting for correlation can lead to excessive risk
- Correlation structure is an important factor in robust portfolio construction

## Disclaimer
This project was completed for educational and research purposes only and does not constitute financial advice.


