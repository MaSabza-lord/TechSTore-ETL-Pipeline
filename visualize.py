import pyodbc
import pandas as pd
import matplotlib.pyplot as plt

# 1. Connect to SQL Server
connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=TechStore;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

conn = pyodbc.connect(connection_string)

# 2. Get the data using SQL (The same query you wrote earlier!)
query = """
SELECT Category, SUM(Price) as TotalValue
FROM Products
GROUP BY Category
ORDER BY TotalValue DESC
"""

# 3. Load into Pandas (Make it a table)
df = pd.read_sql(query, conn)

# 4. Draw the Chart
plt.figure(figsize=(10, 6))
bars = plt.bar(df['Category'], df['TotalValue'], color='#4CAF50')

# Add some style
plt.title('Total Inventory Value by Category', fontsize=16)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Value (Rand)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the money on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'R{int(height)}',
             ha='center', va='bottom')

print("📊 Generating chart...")
plt.show()

conn.close()