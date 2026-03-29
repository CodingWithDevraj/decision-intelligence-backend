from config.db import db
import pandas as pd

def get_insights():
    # Fetch data from MongoDB
    data = list(db.sales.find({}, {"_id": 0}))

    if not data:
        return {"error": "No data found"}

    df = pd.DataFrame(data)

    # Calculate revenue
    df["revenue"] = df["price"] * df["quantity"]

    # Total revenue
    total_revenue = df["revenue"].sum()

    # Top product
    top_product = df.groupby("product")["revenue"].sum().idxmax()

    # Best region
    best_region = df.groupby("region")["revenue"].sum().idxmax()

    return {
        "total_revenue": int(total_revenue),
        "top_product": top_product,
        "best_region": best_region
    }