import pandas as pd
import joblib
import matplotlib.pyplot as plt

df = pd.read_csv("programs/day5/data/cleaned_salary.csv")
model = joblib.load("programs/day5/model_salary.pkl")

X = df[["YearsExperience"]]
y = df["Salary"]

y_pred = model.predict(X)
residuals = y - y_pred

plt.scatter(X, residuals)
plt.axhline(0)
plt.xlabel("YearsExperience")
plt.ylabel("Residuals")
plt.show()
