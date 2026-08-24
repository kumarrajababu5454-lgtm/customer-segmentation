import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import joblib


# ============================================================
# 1. LOAD DATA
# ============================================================

df = pd.read_csv("data/raw/customers.csv")

print("\n===== DATASET =====")
print("Shape:", df.shape)
print(df.head())


# ============================================================
# 2. BASIC DATA CHECK
# ============================================================

print("\n===== DATA INFO =====")
print(df.info())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATES =====")
print(df.duplicated().sum())


# ============================================================
# 3. SELECT FEATURES
# ============================================================

features = [
    "Age",
    "Annual_Income",
    "Spending_Score"
]

X = df[features]


# ============================================================
# 4. SCALE FEATURES
# ============================================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


# ============================================================
# 5. FIND BEST K USING SILHOUETTE SCORE
# ============================================================

scores = {}

print("\n===== SILHOUETTE SCORES =====")

for k in range(2, 11):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(X_scaled)

    score = silhouette_score(X_scaled, labels)

    scores[k] = score

    print(f"K = {k}: {score:.4f}")


# ============================================================
# 6. SELECT BEST K
# ============================================================

best_k = max(scores, key=scores.get)

print("\n===== BEST K =====")
print("Best number of clusters:", best_k)
print("Best silhouette score:", round(scores[best_k], 4))


# ============================================================
# 7. TRAIN FINAL MODEL
# ============================================================

kmeans = KMeans(
    n_clusters=best_k,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(X_scaled)


# ============================================================
# 8. CUSTOMER SEGMENT PROFILE
# ============================================================

profile = df.groupby("Cluster")[
    ["Age", "Annual_Income", "Spending_Score"]
].mean()

print("\n===== CUSTOMER SEGMENTS =====")
print(profile.round(2))


# ============================================================
# 9. CUSTOMER COUNT PER CLUSTER
# ============================================================

print("\n===== CUSTOMERS PER CLUSTER =====")

print(
    df["Cluster"]
    .value_counts()
    .sort_index()
)


# ============================================================
# 10. SAVE PROCESSED DATA
# ============================================================

df.to_csv(
    "data/processed/customer_segments.csv",
    index=False
)


# ============================================================
# 11. SAVE MODEL
# ============================================================

joblib.dump(
    kmeans,
    "models/kmeans_model.joblib"
)

joblib.dump(
    scaler,
    "models/scaler.joblib"
)


# ============================================================
# 12. SAVE CLUSTER PROFILE
# ============================================================

profile.to_csv(
    "data/processed/cluster_profile.csv"
)


# ============================================================
# 13. CREATE CLUSTER VISUALIZATION
# ============================================================

plt.figure(figsize=(10, 6))

plt.scatter(
    df["Annual_Income"],
    df["Spending_Score"],
    c=df["Cluster"]
)

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")

plt.savefig(
    "data/processed/customer_segments.png"
)

plt.close()


# ============================================================
# COMPLETE
# ============================================================

print("\n===================================")
print("MODEL TRAINING COMPLETED")
print("===================================")

print("\nFiles created:")

print("✓ data/processed/customer_segments.csv")
print("✓ data/processed/cluster_profile.csv")
print("✓ data/processed/customer_segments.png")
print("✓ models/kmeans_model.joblib")
print("✓ models/scaler.joblib")