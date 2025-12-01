# Building-a-Beginner-Analytics-Dashboard-Python-SQL-CSV

This project is a beginner-friendly end-to-end data pipeline that demonstrates how to load data from a CSV file, clean it, store it in a SQL database, and build a simple analytics dashboard in streamlit using Python .

It is designed as an introductory project for anyone learning data engineering, data analytics, or Python-based ETL pipelines.

### 📁 Project Structure

📦 Beginner_Data_Pipeline_Python_SQL_CSV_file

 ┣ 📄 README.md
 
 ┣ 📄 pipeline.py
 
 ┣ 📄 dashboard.py
 
 ┣ 📄 sales_data.xlsx
 


 ## Data Architechture Diagram 

 ![Beginner_Pi](https://github.com/user-attachments/assets/2e69579f-6eee-4b58-9915-fc6df4272f9c)


## 🚀 Features

- Import data from a CSV file

- Clean and preprocess the dataset using Pandas

- Store cleaned data into a SQLite database

- Use SQL queries to aggregate and analyze the data

- Create a simple analytics dashboard (tables + charts) in Streamlit (Web based visualization platform)

- Beginner-friendly, fully documented Python code

## 🛠 Technologies Used

 - Python 3.x

 - Pandas

 - SQLite

 - SQLAlchemy

- Altair (statistical visualization library)

## 📊 Example Insights Generated

- Total sales

- Sales by product category

- Monthly sales trends

- Top-performing products

- Summary statistics

## ▶️ How to Run the Project

1. Clone the Repository
git clone https://github.com/Kindoli/Building-a-Beginner-Analytics-Dashboard-Python-SQL-CSV-.git
cd Building-a-Beginner-Analytics-Dashboard-Python-SQL-CSV-

2. Install Dependencies
pip install -r requirements.txt

3. Run the Pipeline
python pipeline.py


This will:

Load the CSV

Clean the data

Insert it into the SQL database (sales.db)

4. Run the Dashboard Script
python dashboard.py


This will generate charts and summary tables.

## Streamlit Dashboard snapshot
<img width="602" height="379" alt="dasbboard_image" src="https://github.com/user-attachments/assets/9592be29-4de9-45f3-afa4-e0cc3bbaec02" />


## 📂 Sample Code Snippet

df = pd.read_excel("sales_data.xlsx")

df_clean = df.dropna()

df_clean.to_sql("Sales_data", conn, if_exists="replace", index=False)

## 📘 Learning Objectives

This project helps beginners learn:

- Reading CSV files in Python

- Basic data cleaning

- SQL operations using Python

- Building a simple analytics dashboard using Streamlit

- Structuring a real-world mini data pipeline

## 🤝 Contributing

Pull requests are welcome!
Feel free to submit improvements or additional analytics steps.
