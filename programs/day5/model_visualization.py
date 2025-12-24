import pandas as pd
import joblib
import matplotlib.pyplot as plt

df = pd.read_csv("programs/day5/data/cleaned_salary.csv")
model = joblib.load("programs/day5/model_salary.pkl")

X = df[["YearsExperience"]]
y = df["Salary"]

y_pred = model.predict(X)

plt.scatter(X, y)
plt.plot(X, y_pred)
plt.xlabel("YearsExperience")
plt.ylabel("Salary")
plt.show()
