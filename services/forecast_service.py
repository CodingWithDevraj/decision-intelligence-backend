from config.db import db
import pandas as pd

def forecast():
    data = list(db.sales.find({}, {"_id": 0}))
    df = pd.DataFrame(data)

    df["revenue"] = df["price"] * df["quantity"]

    avg_growth = 0.1  # assume 10% growth

    current_revenue = df["revenue"].sum()
    future_revenue = current_revenue * (1 + avg_growth)

    return {
        "current_revenue": int(current_revenue),
        "predicted_revenue": int(future_revenue)
    }