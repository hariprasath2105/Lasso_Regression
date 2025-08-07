
import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle

df = pd.read_csv("ad_spend_dataset.csv")

features = ["TV", "Radio", "Social Media"]
X = df[features]
y = df["Revenue"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)

with open("lasso_model.pkl", "wb") as f:
    pickle.dump(lasso, f)

with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)
