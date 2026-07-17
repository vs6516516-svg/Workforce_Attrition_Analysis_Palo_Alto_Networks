import streamlit as st
import pandas as pd

st.set_page_config(page_title="Workforce Attrition Analysis", layout="wide")

st.title("Workforce Attrition Analysis at Palo Alto Networks")
st.write("Business Analytics | HR Analytics | Machine Learning")

# Load Dataset
df = pd.read_csv("Palo_Alto_Networks.csv")

st.header("Dataset Preview")
st.dataframe(df.head())

st.header("Dataset Overview")
st.write(f"Number of Employees: {df.shape[0]}")
st.write(f"Number of Features: {df.shape[1]}")

st.header("Overall Attrition")

attrition = df["Attrition"].value_counts()

st.bar_chart(attrition)

st.header("Department-wise Attrition")

dept = pd.crosstab(df["Department"], df["Attrition"])

st.bar_chart(dept)

st.header("Job Role-wise Attrition")

job = pd.crosstab(df["JobRole"], df["Attrition"])

st.bar_chart(job)

st.header("Overtime Analysis")

overtime = pd.crosstab(df["OverTime"], df["Attrition"])

st.bar_chart(overtime)

st.header("Business Insights")

st.markdown("""
- Departments and job roles exhibit different attrition patterns.
- Overtime is associated with increased employee attrition.
- HR Analytics can support data-driven retention strategies.
- Machine learning helps identify employees who may be at higher risk of leaving.
""")

st.header("Conclusion")

st.success("This dashboard demonstrates how HR Analytics can be used to understand workforce attrition and support informed HR decision-making.")
