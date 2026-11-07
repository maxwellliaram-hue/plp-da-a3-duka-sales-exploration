# Duka Electronics - H1 2026 Sales Exploration

## Project summary
Exploratory analysis of Duka Electronics' January-June 2026 sales (1,000 orders, seed 2026) for the Head of Sales' half-year review. The notebook inspects and cleans the data, derives revenue and calendar/price-band columns, answers five business questions, and cross-checks the totals against an Excel workbook (SUMIFS, XLOOKUP and a PivotTable).

## Questions answered
1. How do branches rank by revenue and by number of orders, and why do the rankings differ?
2. Which three products lead by revenue and by units sold, and why do the lists differ?
3. How do weekend and weekday orders compare (orders, revenue, average order revenue)?
4. Which month is best and worst for revenue, and what is the percentage difference?
5. How many Premium online orders come from Nairobi and Mombasa, and what are they worth?
6. Do the Excel totals match pandas?

## Repository contents
| Path | Purpose |
|---|---|
| `generate_data.py` | Dataset generator (seed 2026); writes `duka_sales.csv` |
| `duka_sales_exploration.ipynb` | The analysis, run top to bottom with outputs |
| `outputs/premium_online_coast_capital.csv` | Premium online orders from Nairobi and Mombasa (`index=False`) |
| `excel/duka_branch_summary.xlsx` | SUMIFS branch table, XLOOKUP region column, PivotTable of revenue by branch and channel |
| `requirements.txt` | Python dependencies |

## How to regenerate the data and run the notebook
```bash
pip install -r requirements.txt
python generate_data.py          # writes duka_sales.csv
jupyter notebook duka_sales_exploration.ipynb   # Kernel > Restart & Run All
```
`duka_sales.csv` is not required in the repository because `generate_data.py` recreates it (the notebook also calls the generator if the CSV is missing).

## Assumptions
- `revenue = units x unit_price`.
- **Premium** means `unit_price >= KES 28,000`; everything else is **Value**.
- Weekend = Saturday and Sunday.
- Percentage difference between months = (best - worst) / worst.

## Executive Summary

- Duka Electronics earned **KES 30,755,900** from **1,000** orders in H1 2026 (average **KES 30,756** per order), and weekends contributed only **26.2%** of revenue.
- **Nairobi** is the top branch with **KES 9.80M** (31.9% of revenue), but the rankings differ: **Nakuru** takes **158** orders versus **139** for **Eldoret**, yet earns **KES 3.69M** against **KES 4.23M**.
- The top three products by revenue (Laptop 15in, Smartphone, Smart TV 55in) generate **68.4%** of revenue, while **Phone Charger** leads on volume with **707** units but only **KES 0.85M** in revenue.
- **2026-03** was the best month at **KES 6.41M** and **2026-02** the worst at **KES 4.65M**, a **37.6%** gap between them.
- Premium online orders from Nairobi and Mombasa total **33** orders worth **KES 2,586,000**, or **8.4%** of all revenue.
