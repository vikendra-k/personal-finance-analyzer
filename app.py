# ---------- FORCE GUI BACKEND (WINDOWS FIX) ----------
import matplotlib
matplotlib.use("TkAgg")

# ---------- IMPORTS ----------
import sys
import pandas as pd
import matplotlib.pyplot as plt

# ---------- OPTIONAL: FIX CONSOLE ENCODING ----------
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# ---------- LOAD DATA ----------
df = pd.read_csv("data/expenses.csv")

# ---------- CLEAN DATA ----------
df["date"] = pd.to_datetime(df["date"])
df["category"] = df["category"].str.strip().str.title()
df = df[df["amount"] > 0]

# ---------- ANALYSIS ----------
total_spent = df["amount"].sum()
print("\nTotal money spent (INR):", total_spent)

category_spending = (
    df.groupby("category")["amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSpending by category:")
print(category_spending)

category_percentage = (category_spending / total_spent) * 100
print("\nCategory-wise percentage contribution:")
print(category_percentage.round(2))

df["month"] = df["date"].dt.to_period("M")
monthly_spending = df.groupby("month")["amount"].sum()

print("\nMonthly spending:")
print(monthly_spending)

max_expense = df.loc[df["amount"].idxmax()]
print("\nHighest single expense:")
print(max_expense)

# ---------- VISUALIZATION ----------
plt.figure(figsize=(8, 5))
category_spending.plot(kind="bar")
plt.title("Spending by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()


