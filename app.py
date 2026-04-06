import csv
from src.utils import load_products, load_orders
from src.processor import process_orders

products = load_products("data/products.csv")
orders = load_orders("data/warehouse_orders.csv")

report, updated_products = process_orders(products, orders)

with open("output/fulfillment_report.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=report[0].keys())
    writer.writeheader()
    writer.writerows(report)

with open("output/stock_remaining.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["product_id", "remaining_stock"])
    for pid, data in updated_products.items():
        writer.writerow([pid, data["stock"]])