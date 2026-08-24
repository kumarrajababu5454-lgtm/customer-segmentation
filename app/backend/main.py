from fastapi import FastAPI
from pydantic import BaseModel
import sys
from pathlib import Path


# Add project root to Python path
BASE_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.append(str(BASE_DIR))

from src.predict import predict_customer


app = FastAPI(
    title="Customer Segmentation API",
    description="ML API for customer segmentation",
    version="1.0.0"
)


class Customer(BaseModel):
    age: int
    annual_income: float
    spending_score: float


@app.get("/")
def home():

    return {
        "message": "Customer Segmentation API is running"
    }


@app.post("/predict")
def predict(customer: Customer):

    result = predict_customer(
        age=customer.age,
        annual_income=customer.annual_income,
        spending_score=customer.spending_score
    )

    return result