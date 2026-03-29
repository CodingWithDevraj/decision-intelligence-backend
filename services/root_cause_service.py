from config.db import db
import pandas as pd

def root_cause_analysis():
    data = list(db.sales.find({}, {"_id": 0}))
    df = pd.DataFrame(data)

    df["revenue"] = df["price"] * df["quantity"]

    insights = []

    # Region impact
    region_rev = df.groupby("region")["revenue"].sum()
    worst_region = region_rev.idxmin()

    insights.append(f"Revenue is lowest in {worst_region} region")

    # Product impact
    product_rev = df.groupby("product")["revenue"].sum()
    worst_product = product_rev.idxmin()

    insights.append(f"Product {worst_product} is underperforming")

    return {"root_causes": insights}