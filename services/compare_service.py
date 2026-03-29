from config.db import db
import pandas as pd

def compare(price_list, demand_list):
    data = list(db.sales.find({}, {"_id": 0}))
    df = pd.DataFrame(data)

    results = []

    for p, d in zip(price_list, demand_list):
        temp = df.copy()

        temp["price"] = temp["price"] * (1 + p/100)
        temp["quantity"] = temp["quantity"] * (1 + d/100)

        temp["revenue"] = temp["price"] * temp["quantity"]
        temp["profit"] = temp["revenue"] - (temp["cost"] * temp["quantity"])

        results.append({
            "price": p,
            "demand": d,
            "profit": int(temp["profit"].sum())
        })

    return results