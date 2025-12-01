# Building Dashboard in Streamlit
# You need to first intall pip install streamlit

import streamlit as st
import sqlite3
import pandas as pd
import altair as alt # statistical visualization library

# Connect to the sales_data db

conn = sqlite3.connect("Sales_Data.db")

# Defining a helper function
def query(Eddie):
    return pd.read_sql_query(Eddie,conn)

st.title("Sales Analytics Dashboard")

# Summary metrics

Total_revenue = query("Select sum(Amount * Boxes) as " \
"Total_sales from Sales_Data;")["Total_sales"][0]

st.metric("Total Revenue", f"${Total_revenue:,.2f}")

# Creating a filter

st.subheader("Filter by Region and Product")

filter_df = query("Select Geography, Product from Sales_Data")

# Unique lists
regions = sorted(filter_df["Geography"].dropna().unique().tolist())
products = sorted(filter_df["Product"].dropna().unique().tolist())

selected_regions = st.multiselect(
    "Select Region(s)",
    options=regions
)

selected_products = st.multiselect(
    "Select Product(s)",
    options=products
)

# Revenue by Region

st.subheader("Revenue by Region")

region_df = query("Select Distinct Geography, sum(Amount * Boxes) as Regional_sales from " \
"Sales_Data Group by Geography order by Regional_sales desc;")

st.bar_chart(region_df.set_index("Geography")) 
# Geography column will be used as the index (Row labels)

# Daily Revenue Trend
st.subheader("Daily Revenue Trend")

daily_df = query("select Product, date(Date) as Daily_trends, sum(Amount * Boxes) as " \
"revenue from " \
"Sales_Data Group by Product order by Daily_trends asc;")

chart = alt.Chart(daily_df).mark_line().encode(x="Daily_trends:T", y="revenue:Q")

st.altair_chart(chart, use_container_width=True)

# Top Products

top_df = query("Select Product, Geography, sum(Amount * Boxes) as sales from " \
"Sales_Data group by Product, Geography order by sales desc limit 50;")

st.table(top_df)

conn.close()








