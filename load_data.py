import pandas as pd
import sqlite3


# first install openpyxl- library that reads excel files

# load excel file

df= pd.read_excel("Sales_Data.xlsx")

# Connectign to SQLite

conn = sqlite3.connect("Sales_Data.db")

# Writing to SQL Tables

df.to_sql("Sales_Data", conn, if_exists="replace", index=False)

print("Data loaded succsefully")

conn.close