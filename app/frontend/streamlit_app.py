import streamlit as st
import requests


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="🎯",
    layout="centered"
)


# ============================================================
# TITLE
# ============================================================

st.title("🎯 Customer Segmentation")

st.write(
    "Enter customer information to identify the customer segment."
)


# ============================================================
# INPUTS
# ============================================================

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

annual_income = st.number_input(
    "Annual Income",
    min_value=0.0,
    value=60000.0,
    step=1000.0
)

spending_score = st.slider(
    "Spending Score",
    min_value=1,
    max_value=100,
    value=80
)


# ============================================================
# PREDICTION
# ============================================================

if st.button("🚀 Predict Customer Segment"):

    payload = {
        "age": age,
        "annual_income": annual_income,
        "spending_score": spending_score
    }

    try:

        response = requests.post(
            "https://customer-segmentation-1-ot3k.onrender.com/predict",
            json=payload,
            timeout=10
        )

        if response.status_code == 200:

            result = response.json()

            st.success("Prediction completed!")

            st.subheader("Customer Segment")

            st.info(
                f"🎯 Cluster {result['cluster']}"
            )

            st.write(
                f"Predicted Cluster: {result['cluster']}"
            )

        else:

            st.error(
                f"API Error: {response.status_code}"
            )

    except requests.exceptions.ConnectionError:

        st.error(
            "Could not connect to the FastAPI backend. "
            "Make sure the backend is running."
        )

    except requests.exceptions.Timeout:

        st.error(
            "The request timed out. "
            "Please check that the FastAPI backend is running."
        )

    except Exception as e:

        st.error(
            f"Something went wrong: {e}"
        )