# Task 7 - Sales Summary using Python and SQLite

## 📌 Objective
Analyze basic sales data using SQLite within Python and visualize the results.

## 🧰 Tools Used
- Python (Standard Library)
- SQLite (via `sqlite3`, built into Python)
- Pandas
- Matplotlib

## 🗃 Dataset
Created a local SQLite database (`sales_data.db`) with one table:

**Table: sales**
- `id` (this is an auto-incremented primary key)
- `product` (text)
- `quantity` (integer)
- `price` (real)

## 🧪 Sample Data
Example entries include:
- Pens, Pencils, Notebooks, Erasers
- Various quantities and prices

## 🧠 SQL + Python Concepts Used
- `sqlite3.connect()` to create/load the database
- SQL: `SUM(quantity)` and `SUM(quantity * price)` with `GROUP BY`
- `pandas.read_sql_query()` to load SQL results into a DataFrame
- `print()` to display summary
- `matplotlib.pyplot` to draw a bar chart

## 📊 Output
- Console output showing product-wise total quantity and revenue
- Bar chart saved as `sales_chart.png`

## 🧼 Notes
- Script automatically deletes old data to avoid duplicates on re-run
- The database is created and updated locally by input of your choice (no internet or server needed)

## 🧾 Deliverables
- `task7_sales_summary.py`
- `sales_chart.png`
- `sales_data.db` (auto-created)
- This `README.md`

## ✅ Outcome
Learned to:
- Use SQL inside Python
- Connect to SQLite
- Perform aggregations
- Visualize data using `matplotlib`
