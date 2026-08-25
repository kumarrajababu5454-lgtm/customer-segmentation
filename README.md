# 🎯 Customer Segmentation ML Application

An end-to-end Machine Learning application that segments customers based on **Age, Annual Income, and Spending Score** using **K-Means Clustering**.

This project demonstrates the complete Machine Learning application lifecycle:

**Data → EDA → Preprocessing → Model Training → Model Saving → FastAPI → Streamlit → GitHub → Cloud Deployment**

---

# 🚀 Live Application

## 🌐 Streamlit Frontend

https://customer-segmentation-mujwcevudnzo2y68ytcjuc.streamlit.app/

## ⚡ FastAPI Backend

https://customer-segmentation-1-ot3k.onrender.com

## 📚 FastAPI API Documentation

https://customer-segmentation-1-ot3k.onrender.com/docs

---

# 📌 Project Overview

Customer segmentation is the process of grouping customers with similar characteristics.

In this project, **K-Means Clustering** is used to divide customers into different groups based on:

- Age
- Annual Income
- Spending Score

The user enters customer information through the Streamlit frontend. The frontend sends the data to the FastAPI backend. The backend scales the input data and uses the trained K-Means model to predict the customer cluster.

---

# 🎯 Objective

The main objectives of this project are:

- Create a customer dataset
- Perform Exploratory Data Analysis
- Preprocess the data
- Select relevant features
- Scale numerical features
- Train a K-Means clustering model
- Save the trained model
- Build a FastAPI REST API
- Build an interactive Streamlit frontend
- Connect frontend and backend
- Deploy the backend on Render
- Deploy the frontend on Streamlit Cloud
- Manage the project using Git and GitHub

---

# 🧠 Machine Learning Algorithm

## K-Means Clustering

K-Means is an **unsupervised Machine Learning algorithm** used to group similar data points into clusters.

The model uses:

| Feature | Description |
|---|---|
| Age | Customer age |
| Annual Income | Customer annual income |
| Spending Score | Customer spending score |

---

# 🔄 Machine Learning Workflow

```text
Raw Customer Data
       ↓
Data Cleaning
       ↓
Exploratory Data Analysis
       ↓
Feature Selection
       ↓
Feature Scaling
       ↓
K-Means Clustering
       ↓
Model Training
       ↓
Model Saving
       ↓
FastAPI Backend
       ↓
Streamlit Frontend
       ↓
Customer Input
       ↓
Customer Cluster

USER
  ↓
STREAMLIT CLOUD 🌐
  ↓
Streamlit Frontend
  ↓
RENDER 🌐
  ↓
FastAPI
  ↓
Scaler
  ↓
K-Means Model 🤖
  ↓
Customer Cluster 🎯

                    👤 USER
                       │
                       ▼
             ┌─────────────────────┐
             │  STREAMLIT CLOUD 🌐  │
             │     Frontend        │
             └──────────┬──────────┘
                        │
                        │ HTTPS Request
                        ▼
             ┌─────────────────────┐
             │      RENDER 🌐      │
             │      FastAPI        │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │       Scaler        │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │   K-Means Model 🤖  │
             └──────────┬──────────┘
                        │
                        ▼
                 🎯 CUSTOMER
                    CLUSTER


                    🛠️ Technologies Used
Programming Language
Python
Machine Learning
Scikit-learn
K-Means Clustering
Feature Scaling
Data Processing
Pandas
NumPy
Backend
FastAPI
Uvicorn
Frontend
Streamlit
Model Serialization
Joblib
Development Tools
Jupyter Notebook
VS Code
Version Control
Git
GitHub
Deployment
Render
Streamlit Community Cloud
📂 Project Structure
customer-segmentation/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── kmeans_model.joblib
│   └── scaler.joblib
│
├── notebooks/
│   ├── 02_eda_and_preprocessing.ipynb
│   └── README.md
│
├── src/
│   ├── create_dataset.py
│   ├── predict.py
│   └── train_model.py
│
├── app/
│   └── frontend/
│       └── streamlit_app.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
⚙️ Local Installation
1. Clone Repository
git clone https://github.com/kumarrajababu5454-lgtm/customer-segmentation.git
2. Open Project
cd customer-segmentation
3. Create Virtual Environment
python -m venv .venv
4. Activate Virtual Environment
Windows
.venv\Scripts\activate
5. Install Dependencies
pip install -r requirements.txt
▶️ Run FastAPI Backend
uvicorn app:app --reload

Backend:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs
▶️ Run Streamlit Frontend
streamlit run app/frontend/streamlit_app.py

Frontend:

http://localhost:8501
🔌 API
Prediction Endpoint
POST /predict
Example Input
{
  "age": 30,
  "annual_income": 60000,
  "spending_score": 80
}
Example Output
{
  "cluster": 2,
  "segment": "Customer Segment 2"
}

The actual cluster depends on the trained K-Means model.

🎨 Streamlit Frontend

The Streamlit application allows users to enter:

Customer Age
Annual Income
Spending Score

Then the user clicks:

🚀 Predict Customer Segment

The application sends the information to the FastAPI backend.

The backend processes the input and returns the predicted customer cluster.

🤖 Machine Learning Model

Trained K-Means model:

models/kmeans_model.joblib

Trained scaler:

models/scaler.joblib

The FastAPI backend loads these files when the application starts.

🔄 Prediction Process
Customer Input
      ↓
Age
Annual Income
Spending Score
      ↓
Create Feature Array
      ↓
Scaler
      ↓
Scaled Features
      ↓
K-Means Model
      ↓
Cluster Prediction
      ↓
FastAPI Response
      ↓
Streamlit Result
🧪 Example
Input
Age: 30
Annual Income: 60000
Spending Score: 80
Processing
Age + Annual Income + Spending Score
              ↓
            Scaler
              ↓
        K-Means Model
              ↓
        Cluster Prediction
Output
🎯 Customer Segment 2
Cluster: 2

The cluster number is determined by the trained model.

🌐 Deployment
Backend

Deployed on Render.

Live Backend:

https://customer-segmentation-1-ot3k.onrender.com

API Documentation:

https://customer-segmentation-1-ot3k.onrender.com/docs

Frontend

Deployed on Streamlit Community Cloud.

Live Application:

https://customer-segmentation-mujwcevudnzo2y68ytcjuc.streamlit.app/

📦 Requirements
fastapi
uvicorn
streamlit
requests
scikit-learn
pandas
numpy
joblib
🛡️ Error Handling

The Streamlit application handles:

FastAPI connection errors
API errors
Request timeouts
Unexpected exceptions

The FastAPI backend validates incoming customer information using Pydantic.

📈 Future Improvements
Add meaningful names to customer clusters
Add detailed customer segment descriptions
Add interactive charts
Add cluster visualizations
Display cluster characteristics
Add prediction history
Add database integration
Add authentication
Add Docker support
Add CI/CD
Add automated testing
Add model monitoring
Add automatic model retraining
💡 Key Learning Outcomes
Machine Learning
Data preprocessing
Exploratory Data Analysis
Feature selection
Feature scaling
Unsupervised Learning
K-Means Clustering
Model persistence
Software Engineering
Python project structure
Virtual environments
REST APIs
FastAPI
Streamlit
API integration
Error handling
MLOps and Deployment
Git
GitHub
Requirements management
Backend deployment
Frontend deployment
Cloud deployment
🚀 Complete Project Flow
DATASET
   ↓
EDA
   ↓
PREPROCESSING
   ↓
FEATURE SCALING
   ↓
K-MEANS TRAINING
   ↓
MODEL SAVING
   ↓
FASTAPI
   ↓
STREAMLIT
   ↓
GITHUB
   ↓
RENDER
   ↓
STREAMLIT CLOUD
   ↓
LIVE ML APPLICATION 🚀
📌 Project Status
✅ Completed

This project has been successfully developed and deployed as an end-to-end Machine Learning application.

✅ Dataset creation
✅ Data preprocessing
✅ Exploratory Data Analysis
✅ Feature scaling
✅ K-Means clustering
✅ Model training
✅ Model saving
✅ FastAPI backend
✅ Streamlit frontend
✅ API integration
✅ Git version control
✅ GitHub repository
✅ Render deployment
✅ Streamlit Cloud deployment
👨‍💻 Author

Rajababu Kumar

GitHub:

https://github.com/kumarrajababu5454-lgtm

⭐ GitHub Repository

https://github.com/kumarrajababu5454-lgtm/customer-segmentation

📄 License

This project is created for educational and portfolio purposes.


Then **Save (`Ctrl + S`)**.

Finally, in your VS Code terminal:

```powershell
git add README.md
git commit -m "Add complete project README"
git push origin main