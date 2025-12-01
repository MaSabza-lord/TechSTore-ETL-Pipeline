import pyodbc
import csv
import os

# 1. Connect to Azure SQL Database
connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=tcp:techstore-server-sabelo.database.windows.net,1433;"  # Added ,1433;
    "DATABASE=TechStore-DB;"
    "UID=sqladmin;"
    "PWD=#Ma'Sabza2003#;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    print("✅ Connected!")

    # 2. Open the CSV file
    file_path = 'products.csv'
    
    print(f"📂 Opening {file_path}...")
    
    with open(file_path, 'r') as file:
        # Create a CSV reader tool
        csv_reader = csv.reader(file)
        
        # SKIP the first row (Header) so we don't import the word "Price" as a price!
        next(csv_reader)
        
        # 3. Loop through every row and insert it
        count = 0
        for row in csv_reader:
            # row[0] is ID, row[1] is Name, etc.
            cursor.execute("INSERT INTO Products VALUES (?, ?, ?, ?)", row)
            count += 1
            
        # 4. The most important step: COMMIT (Save)
        conn.commit()
        print(f"🎉 Success! Uploaded {count} new products to the database.")

    conn.close()

except Exception as e:
    print(f"❌ Error: {e}")