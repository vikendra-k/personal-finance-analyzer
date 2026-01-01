# ---------- IMPORTS ----------
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Personal Finance Analyzer",
    layout="wide"
)

st.title("📊 Personal Finance Analyzer")
st.caption("Analyze your expenses smartly")

# ---------- LOAD DATA ----------
@st.cache_data
def load_data():
    df = pd.read_csv("data/expenses.csv")
    df["date"] = pd.to_datetime(df["date"])
    df["category"] = df["category"].str.strip().str.title()
    df = df[df["amount"] > 0]
    return df

df = load_data()

# ---------- SIDEBAR ----------
st.sidebar.header("Controls")

view = st.sidebar.selectbox(
    "Select View",
    ["Overview", "Category Analysis", "Monthly Analysis"]
)

# ---------- ANALYSIS ----------
total_spent = df["amount"].sum()

category_spending = (
    df.groupby("category")["amount"]
    .sum()
    .sort_values(ascending=False)
)

category_percentage = (category_spending / total_spent) * 100

df["month"] = df["date"].dt.to_period("M")
monthly_spending = df.groupby("month")["amount"].sum()

max_expense = df.loc[df["amount"].idxmax()]

# ---------- OVERVIEW ----------
if view == "Overview":
    st.subheader("💰 Expense Summary")

    col1, col2 = st.columns(2)
    col1.metric("Total Spent (INR)", f"₹ {total_spent:,.0f}")
    col2.metric("Highest Single Expense", f"₹ {max_expense['amount']:,.0f}")

    st.subheader("📌 Highest Expense Details")
    st.write(max_expense)

# ---------- CATEGORY ANALYSIS ----------
elif view == "Category Analysis":
    st.subheader("📊 Spending by Category")

    col1, col2 = st.columns(2)

    with col1:
        st.dataframe(category_spending.rename("Amount"))

    with col2:
        st.dataframe(category_percentage.round(2).rename("Percentage (%)"))

    plt.figure(figsize=(8, 5))
    category_spending.plot(kind="bar")
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.xticks(rotation=0)
    plt.tight_layout()

    st.pyplot(plt)

# ---------- MONTHLY ANALYSIS ----------
elif view == "Monthly Analysis":
    st.subheader("📅 Monthly Spending Trend")

    st.dataframe(monthly_spending.rename("Amount"))

    plt.figure(figsize=(8, 5))
    monthly_spending.plot(kind="line", marker="o")
    plt.title("Monthly Spending")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.tight_layout()

    st.pyplot(plt)

# ---------- RAW DATA ----------
with st.expander("📂 View Raw Data"):
    st.dataframe(df)

# ---------- FOOTER ----------
st.markdown("---")
st.caption("Built with Python, Pandas & Streamlit")



