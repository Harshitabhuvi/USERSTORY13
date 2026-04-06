import csv
from datetime import datetime

def load_products(path):
    products = {}
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products[row['product_id']] = {
                "name": row['product_name'],
                "stock": int(row['available_stock']),
                "price": float(row['price'])
            }
    return products


def load_orders(path):
    orders = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                # validate quantity
                row['quantity'] = int(row['quantity'])

                # validate date
                datetime.strptime(row['order_date'], "%Y-%m-%d")

                row['valid'] = True
            except Exception:
                # mark invalid order instead of crashing
                row['valid'] = False

            orders.append(row)

    return orders