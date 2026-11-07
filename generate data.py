
Duka Electronics dataset generator  (seed 2026)  ->  duka_sales.csv

!!! STAND-IN VERSION !!!
This file was written as a placeholder because the original Practicals script
was not available. BEFORE SUBMITTING, replace the contents of this file with
the exact generate_data.py from this week's Practicals (unchanged, seed 2026),
then run `python build_deliverables.py` to refresh every number, the notebook
and the Excel file.
"""
import numpy as np
import pandas as pd

SEED = 2026
N_ORDERS = 1000

rng = np.random.default_rng(SEED)

branches = ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret"]
branch_p = [0.34, 0.22, 0.17, 0.15, 0.12]

 product: (unit_price_KES, mean_units)
products = {
    "Smart TV 55in":      (48000, 1.0),
    "Laptop 15in":        (62000, 1.0),
    "Smartphone":         (22000, 1.2),
    "Tablet":             (18000, 1.2),
    "Microwave":          (15000, 1.1),
    "Bluetooth Speaker":  (9500,  1.6),
    "Wireless Earbuds":   (6500,  2.0),
    "Phone Charger":      (1200,  3.5),
}
prod_names = list(products)
prod_p = [0.10, 0.08, 0.17, 0.10, 0.09, 0.12, 0.14, 0.20]

dates = pd.date_range("2026-01-01", "2026-06-30", freq="D")
order_dates = rng.choice(dates, size=N_ORDERS)

df = pd.DataFrame({
    "order_id": [f"DK{i:04d}" for i in range(1, N_ORDERS + 1)],
    "order_date": pd.to_datetime(order_dates).strftime("%Y-%m-%d"),
    "branch": rng.choice(branches, size=N_ORDERS, p=branch_p),
    "product": rng.choice(prod_names, size=N_ORDERS, p=prod_p),
    "channel": rng.choice(["In-store", "Online"], size=N_ORDERS, p=[0.62, 0.38]),
})
df["unit_price"] = df["product"].map(lambda p: products[p][0])
df["units"] = [max(1, int(rng.poisson(products[p][1]))) for p in df["product"]]
df = df.sort_values("order_date").reset_index(drop=True)
df["order_id"] = [f"DK{i:04d}" for i in range(1, N_ORDERS + 1)]
df = df[["order_id", "order_date", "branch", "product", "channel", "units", "unit_price"]]

df.to_csv("duka_sales.csv", index=False)
print(f"Wrote duka_sales.csv: {df.shape[0]} rows, {df.shape[1]} columns")
