from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="Customer Segmentation API")

# Load trained model and scaler
model = joblib.load("models/kmeans_model.joblib")
scaler = joblib.load("models/scaler.joblib")


class Customer(BaseModel):
    age: float
    annual_income: float
    spending_score: float


@app.get("/")
def home():
    return {"message": "Customer Segmentation API is running"}


@app.post("/predict")
def predict(customer: Customer):

    data = np.array([[
        customer.age,
        customer.annual_income,
        customer.spending_score
    ]])

    scaled_data = scaler.transform(data)

    cluster = model.predict(scaled_data)[0]

    return {
        "cluster": int(cluster)
    }