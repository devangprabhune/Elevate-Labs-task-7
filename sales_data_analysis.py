import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to SQLite database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Step 2: Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")
conn.commit()

# Step 3: Clear old data to prevent duplicates
cursor.execute("DELETE FROM sales")
conn.commit()

# Step 4: Insert fresh sample data
sample_data = [
    ('Pen', 10, 1.5),
    ('Notebook', 5, 3.0),
    ('Pen', 15, 1.5),
    ('Pencil', 20, 0.5),
    ('Notebook', 2, 3.0),
    ('Eraser', 8, 0.75),
    ('Marker', 6, 2.0),
    ('Pen', 12, 1.5),
    ('Pencil', 10, 0.5),
    ('Notebook', 4, 3.0),
    ('Ruler', 3, 1.25),
    ('Stapler', 1, 5.5),
    ('Pen', 9, 1.5),
    ('Highlighter', 7, 2.5),
    ('Pencil', 15, 0.5),
    ('Eraser', 12, 0.75),
    ('Notebook', 10, 3.0),
    ('Stapler', 2, 5.5),
    ('Marker', 9, 2.0),
    ('Highlighter', 4, 2.5)
]


cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
conn.commit()

# Step 5: Run SQL query to get summary
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""
df = pd.read_sql_query(query, conn)

# Step 6: Display and plot
print("Sales Summary:")
print(df)

df.plot(kind='bar', x='product', y='revenue', legend=False, color='skyblue')
plt.title("Revenue by Product")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

# Step 7: Close connection
conn.close()
