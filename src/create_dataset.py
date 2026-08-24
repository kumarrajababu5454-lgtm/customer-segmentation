import numpy as np
import pandas as pd

np.random.seed(42)

n_customers = 500

data = {
    "CustomerID": range(1, n_customers + 1),
    "Gender": np.random.choice(["Male", "Female"], n_customers),
    "Age": np.random.randint(18, 70, n_customers),
    "Annual_Income": np.random.randint(20000, 120000, n_customers),
    "Spending_Score": np.random.randint(1, 101, n_customers),
}

df = pd.DataFrame(data)

df.to_csv("data/raw/customers.csv", index=False)

print("Dataset created successfully!")
print(f"Number of customers: {len(df)}")
print(df.head())