import sys
sys.stdout.reconfigure(encoding='utf-8')

import pandas as pd

# Load expense data
df = pd.read_csv("data/expenses.csv")

# Clean data
df['date'] = pd.to_datetime(df['date'])
df['category'] = df['category'].str.strip().str.title()
df = df[df['amount'] > 0]

# Total spending
total_spent = df['amount'].sum()
print(f"\nTotal money spent: ₹{total_spent}")

# Spending by category
category_spending = df.groupby('category')['amount'].sum().sort_values(ascending=False)
print("\nSpending by category:")
print(category_spending)

# Percentage contribution
category_percentage = (category_spending / total_spent) * 100
print("\nCategory-wise percentage contribution:")
print(category_percentage.round(2))

# Monthly spending
df['month'] = df['date'].dt.to_period('M')
monthly_spending = df.groupby('month')['amount'].sum()
print("\nMonthly spending:")
print(monthly_spending)

# Highest single expense
max_expense = df.loc[df['amount'].idxmax()]
print("\nHighest single expense:")
print(max_expense)

# Observations (fill after running):
# - Highest spending category:
# - Month with highest spending:
# - Largest single expense:
