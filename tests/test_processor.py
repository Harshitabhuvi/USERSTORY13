import unittest
from src.processor import process_orders

class TestProcessor(unittest.TestCase):

    def setUp(self):
        self.products = {
            "P001": {"name": "Item", "stock": 10, "price": 100}
        }

    def test_invalid_product_rejected(self):
        orders = [{"order_id": "O1", "product_id": "PX", "quantity": 1}]
        result, _ = process_orders(self.products, orders)
        self.assertEqual(result[0]["status"], "REJECTED")

    def test_negative_quantity_rejected(self):
        orders = [{"order_id": "O2", "product_id": "P001", "quantity": -5}]
        result, _ = process_orders(self.products, orders)
        self.assertEqual(result[0]["status"], "REJECTED")

    def test_stock_deduction(self):
        orders = [{"order_id": "O3", "product_id": "P001", "quantity": 5}]
        _, updated = process_orders(self.products, orders)
        self.assertEqual(updated["P001"]["stock"], 5)

    def test_partial_fulfillment(self):
        orders = [{"order_id": "O4", "product_id": "P001", "quantity": 20}]
        result, _ = process_orders(self.products, orders)
        self.assertEqual(result[0]["status"], "PARTIAL")

    def test_full_fulfillment(self):
        orders = [{"order_id": "O5", "product_id": "P001", "quantity": 5}]
        result, _ = process_orders(self.products, orders)
        self.assertEqual(result[0]["status"], "FULFILLED")


if __name__ == "__main__":
    unittest.main()