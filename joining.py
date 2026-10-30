import pandas as pd

def classify_sale(amount):
    if amount >= 100000:
        return "Large"
    elif amount >= 50000:
        return "Medium"
    else:
        return "Small"

orders = pd.DataFrame({
    "order_id": [101, 102, 103],
    "customer_id": [1, 2, 1],
    "amount_kes": [45000, 28000, 62000]
})

customers = pd.DataFrame({
    "customer_id": [1, 2, 3],
    "name": ["Kamau Stores", "Otieno Wholesale", "Hassan Traders"],
    "county": ["Nairobi", "Kisumu", "Mombasa"]
})

# Inner join: only customers who have orders
merged = pd.merge(orders, customers, on="customer_id", how="inner")
print(merged)

merged["sale_size"] = merged["amount_kes"].apply(classify_sale)
print(merged[["name", "amount_kes", "sale_size"]])
