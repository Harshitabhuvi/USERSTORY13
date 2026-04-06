def process_orders(products, orders):
    report = []

    for order in orders:
        pid = order['product_id']
        qty = order['quantity']

        # Case 1: Invalid date or invalid quantity (from utils.py validation)
        if not order.get('valid', True):
            status = "REJECTED"

        # Case 2: Product does not exist or quantity <= 0
        elif pid not in products or qty <= 0:
            status = "REJECTED"

        # Case 3: Valid product and quantity
        else:
            stock = products[pid]['stock']

            # Full fulfillment
            if qty <= stock:
                products[pid]['stock'] -= qty
                status = "FULFILLED"

            # Partial fulfillment
            elif stock > 0:
                products[pid]['stock'] = 0
                status = "PARTIAL"

            # No stock available
            else:
                status = "REJECTED"

        report.append({
            "order_id": order['order_id'],
            "product_id": pid,
            "quantity": qty,
            "status": status
        })

    return report, products