import os
import pandas as pd
import streamlit as st
import pandasql as psql  # For SQL-like queries on DataFrame

# Data Loading
try:
    data = pd.read_csv("zomato.csv")
    print("Data loaded successfully:")
    print(data.head())
except FileNotFoundError:
    print("Error: zomato.csv not found. Using sample data.")
    data = pd.DataFrame({'product': ['A', 'B', 'C'], 'sales': [100, 200, 150]})
    print("Sample data used:")
    print(data)

# Local Query Execution

def execute_query(df, query):
    try:
        result = psql.sqldf(query, locals())
        return result
    except Exception as e:
        st.error(f"An error occurred while processing the query: {e}")
        print(f"Query Execution Error: {e}")
        return None

# Streamlit App
st.title("DataQueryAI (Local Version)")
query = st.text_area("Enter your SQL query:")

if st.button("Submit"):
    if query:
        print("User submitted query:", query)
        with st.spinner("Processing..."):
            results = execute_query(data, query)
        
        if results is not None:
            st.dataframe(results)
        else:
            st.error("No results returned. Please check your query syntax.")
