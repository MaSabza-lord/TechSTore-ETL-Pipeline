# TechStore ETL Pipeline

## 📌 Project Overview
This project is an automated Data Engineering pipeline that extracts sales data from CSV files, transforms it using Python, and loads it into a Microsoft SQL Server database. It also includes SQL scripts for business intelligence analysis.

## 🛠️ Tech Stack
* **Language:** Python 3.12 (Pandas, PyODBC)
* **Database:** Microsoft SQL Server (Express Edition)
* **Tools:** Visual Studio Code, Git, GitHub
* **Techniques:** ETL (Extract, Transform, Load), Database Normalization

## 📂 Project Structure
* `upload_data.py`: The main ETL script that moves data from CSV to SQL.
* `data_pull.py`: A test script to verify database connectivity.
* `analysis.sql`: Business questions answered using SQL queries (Aggregations).
* `products.csv`: Raw source data.

## 📊 Key Insights
Running the SQL analysis revealed that **Computers** are the highest-value category in our inventory, outperforming Accessories and Peripherals.

## 🚀 How to Run
1.  Clone the repository.
2.  Install dependencies: `pip install pyodbc`
3.  Run the ETL script: `python upload_data.py`