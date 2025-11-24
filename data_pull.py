import pyodbc

# # 1. Define the Connection String
connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"                       # Added semicolon here!
    "DATABASE=TechStore;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"             # Added this required setting
)

print("🔌 Attempting to connect to SQL Server...")

try:
    # 2. Open the Connection
    conn = pyodbc.connect(connection_string)
    print("✅ Connection Successful! We are in.")

    # 3. Create a "Cursor" (This is like a robot arm that fetches data)
    cursor = conn.cursor()

    # 4. Execute a Query (The same SQL you wrote yesterday)
    print("🔍 Reading data from the Products table...")
    cursor.execute("SELECT * FROM Products")

    # 5. Fetch and Print the results
    rows = cursor.fetchall()
    
    print("-" * 30)
    print(f"Found {len(rows)} products:")
    print("-" * 30)

    for row in rows:
        # row[1] is the Product Name, row[2] is the Price
        print(f"📦 {row[1]} - R{row[2]}")

    # 6. Close the door behind you
    conn.close()

except Exception as e:
    print("❌ Error: Could not connect.")
    print("Details:", e)