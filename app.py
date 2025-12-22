import pandas as pd
import random
from datetime import datetime, timedelta

# Configuration
NUM_RECORDS = 200
START_DATE = datetime(2024, 1, 1)

categories = {
    "Food": (50, 300),
    "Transport": (20, 150),
    "Entertainment": (100, 600),
    "Utilities": (200, 800),
    "Shopping": (100, 1500),
    "Health": (50, 500)
}

descriptions = {
    "Food": ["Mess", "Snacks", "Dinner", "Lunch", "Cafe"],
    "Transport": ["Bus", "Auto", "Taxi", "Metro"],
    "Entertainment": ["Movie", "Concert", "Subscription", "Game"],
    "Utilities": ["Electricity", "Internet", "Water", "Mobile Bill"],
    "Shopping": ["Clothes", "Books", "Online Order", "Shoes"],
    "Health": ["Medicine", "Doctor Visit", "Gym"]
}

data = []

for i in range(NUM_RECORDS):
    category = random.choice(list(categories.keys()))
    amount = random.randint(*categories[category])
    date = START_DATE + timedelta(days=random.randint(0, 180))
    description = random.choice(descriptions[category])

    data.append([
        date.strftime("%Y-%m-%d"),
        category,
        amount,
        description
    ])

df = pd.DataFrame(data, columns=["date", "category", "amount", "description"])

df.to_csv("data/expenses.csv", index=False)

print("CSV file generated successfully with", NUM_RECORDS, "records.")
