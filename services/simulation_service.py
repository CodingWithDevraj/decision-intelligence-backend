from config.db import db
import pandas as pd

def simulate(price_change=0, demand_change=0):
    data = list(db.sales.find({}, {"_id": 0}))

    if not data:
        return {"error": "No data found"}

    df = pd.DataFrame(data)

    # Elasticity factor (you can tune this)
    elasticity = 0.5  

    # Apply price change
    df["price"] = df["price"] * (1 + price_change / 100)

    # Demand decreases when price increases
    df["quantity"] = df["quantity"] * (
        1 + demand_change / 100 - elasticity * price_change / 100
    )

    # Ensure demand doesn't go negative
    df["quantity"] = df["quantity"].clip(lower=0)

    # Revenue
    df["revenue"] = df["price"] * df["quantity"]

    # Cost
    df["total_cost"] = df["cost"] * df["quantity"]

    # Profit
    df["profit"] = df["revenue"] - df["total_cost"]

    return {
        "simulated_revenue": int(df["revenue"].sum()),
        "simulated_profit": int(df["profit"].sum()),
        "price_change_percent": price_change,
        "demand_change_percent": demand_change
    }