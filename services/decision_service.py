from config.db import db
import pandas as pd

def get_decisions():
    data = list(db.sales.find({}, {"_id": 0}))

    if not data:
        return {"error": "No data found"}

    df = pd.DataFrame(data)

    # Create revenue column
    df["revenue"] = df["price"] * df["quantity"]

    # Aggregations
    product_revenue = df.groupby("product")["revenue"].sum()
    region_revenue = df.groupby("region")["revenue"].sum()

    # Best product & region
    top_product = product_revenue.idxmax()
    best_region = region_revenue.idxmax()

    # Decision logic
    decisions = []

    decisions.append(f"Focus on product {top_product} as it generates highest revenue")

    decisions.append(f"Increase marketing in {best_region} region for better growth")

    # Detect low performing products
    low_product = product_revenue.idxmin()
    decisions.append(f"Improve or replace product {low_product} due to low performance")

    return {
        "decisions": decisions
    }