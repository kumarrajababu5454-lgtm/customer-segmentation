import joblib
import numpy as np
from pathlib import Path


# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Load trained model
model = joblib.load(BASE_DIR / "models" / "kmeans_model.joblib")
scaler = joblib.load(BASE_DIR / "models" / "scaler.joblib")


# Business meaning of each cluster
SEGMENT_NAMES = {
    0: "Affluent Moderate Spenders",
    1: "Older High Spenders",
    2: "Affluent Low Spenders",
    3: "Young High Spenders",
    4: "Low Value Customers",
    5: "VIP Customers",
}


def predict_customer(age, annual_income, spending_score):

    customer = np.array([
        [age, annual_income, spending_score]
    ])

    customer_scaled = scaler.transform(customer)

    cluster = int(model.predict(customer_scaled)[0])

    segment = SEGMENT_NAMES[cluster]

    return {
        "cluster": cluster,
        "segment": segment
    }


if __name__ == "__main__":

    result = predict_customer(
        age=30,
        annual_income=60000,
        spending_score=80
    )

    print(result)