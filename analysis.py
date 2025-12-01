# Python Script to Run SQL Queries

import sqlite3
import pandas as pd

# Connecting to SQL lite 
Conn = sqlite3.connect("Sales_Data.db")

# Function to fetch the sales data into the pandas dataframe for analysis

def run_query(query):
    return pd.read_sql_query(query, Conn)

# Generates information about the table
print(run_query("PRAGMA table_info(Sales_Data)"))

# Queries the first five products

print(run_query("SELECT * FROM Sales_Data LIMIT 5;"))

# Total Revenue
print(run_query("Select sum(Amount * Boxes) as Total_Amount from Sales_Data"))

# Revenue by Region

print(run_query("select Geography, sum(Amount * Boxes) as" \
" Unit_sales from Sales_Data Group by Geography order by Unit_sales desc limit 10;"))

# Top Products

print(run_query("select Product, sum(Amount * Boxes) as " \
"Top_Product from Sales_Data Group by Product order by Top_Product desc limit 5;"))

# Daily Sales Trend by products

print(run_query("Select date(Date) as Trend_date, Product, sum(Amount * Boxes) as Sales_unit " \
"from Sales_Data Group by Product order by Trend_date asc limit 5;"))

