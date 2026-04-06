# 📦 Warehouse Order Fulfillment & Stock Management Engine

## 📌 Objective

Build a Python application to process product inventory and customer orders, validate orders, update stock, and generate fulfillment reports.

---

## ⚙️ Features

* ✅ Product validation (must exist)
* ✅ Quantity validation (must be > 0)
* ✅ Order date validation
* ✅ Order processing:

  * **FULFILLED** → when quantity ≤ available stock
  * **PARTIAL** → when quantity > stock but stock > 0
  * **REJECTED** → invalid product, invalid quantity, invalid date, or no stock
* ✅ Automatic stock updates
* ✅ CSV input/output handling
* ✅ Unit testing with coverage support

---

## 📁 Project Structure

```
project-root/
│
├── src/
│   ├── processor.py        # Core order processing logic
│   ├── utils.py            # CSV loading & validation
│
├── data/
│   ├── products.csv
│   ├── warehouse_orders.csv
│
├── tests/
│   ├── test_processor.py   # Unit tests
│
├── output/
│   ├── fulfillment_report.csv
│   ├── stock_remaining.csv
│
├── app.py                  # Main application
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ How to Run

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 2️⃣ Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Unit Tests

```bash
python -m unittest discover tests
```

---

### 5️⃣ Run Application

```bash
python app.py
```

---

## 📊 Coverage

Run test coverage:

```bash
coverage run -m unittest discover tests
coverage report
```

Generate HTML report:

```bash
coverage html
```

Open:

```
htmlcov/index.html
```

---

## 📤 Outputs

After running the application, the following files are generated:

* 📄 `output/fulfillment_report.csv`

  * Contains order status (FULFILLED / PARTIAL / REJECTED)

* 📄 `output/stock_remaining.csv`

  * Contains updated stock after processing

---

## 🧪 Unit Tests

Covered scenarios:

* Invalid product → REJECTED
* Negative quantity → REJECTED
* Stock deduction validation
* Partial fulfillment
* Full fulfillment

---

## 🚀 Future Improvements

* Add REST API (Flask / FastAPI)
* Add logging system
* Add CLI arguments support
* Improve test coverage for utils module
* Add CI/CD pipeline (GitHub Actions)

---



## ⭐ Notes

This project demonstrates clean architecture, validation logic, unit testing, and real-world order processing scenarios suitable for backend/full-stack development roles.
