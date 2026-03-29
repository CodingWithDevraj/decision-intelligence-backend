from config.db import db
import pandas as pd

def find_best_strategy():
    data = list(db.sales.find({}, {"_id": 0}))

    if not data:
        return {"error": "No data found"}

    df = pd.DataFrame(data)

    best_profit = float("-inf")
    best_strategy = {}

    elasticity = 0.5

    # Try different combinations
    for price_change in range(-10, 31, 5):     # -10% to +30%
        for demand_change in range(0, 41, 5):  # 0% to +40%

            temp_df = df.copy()

            # Apply price change
            temp_df["price"] = temp_df["price"] * (1 + price_change / 100)

            # Demand affected by price (elasticity)
            temp_df["quantity"] = temp_df["quantity"] * (
                1 + demand_change / 100 - elasticity * price_change / 100
            )

            temp_df["quantity"] = temp_df["quantity"].clip(lower=0)

            # Revenue
            temp_df["revenue"] = temp_df["price"] * temp_df["quantity"]

            # Cost
            temp_df["total_cost"] = temp_df["cost"] * temp_df["quantity"]

            # Profit
            temp_df["profit"] = temp_df["revenue"] - temp_df["total_cost"]

            total_profit = temp_df["profit"].sum()

            # Find best profit
            if total_profit > best_profit:
                best_profit = total_profit
                best_strategy = {
                    "price_change_percent": price_change,
                    "demand_change_percent": demand_change,
                    "expected_profit": int(total_profit),
                    "expected_revenue": int(temp_df["revenue"].sum())
                }

    return best_strategy