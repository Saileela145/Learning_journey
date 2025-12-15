import pandas as pd
import joblib
import math
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load data
df = pd.read_csv("programs/day5/data/salary_data.csv")

# Clean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Scale
scaler = MinMaxScaler()
df["YearsExperience"] = scaler.fit_transform(df[["YearsExperience"]])

X = df[["YearsExperience"]]
y = df["Salary"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = math.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2:", r2)

# Cross-validation
cv_scores = cross_val_score(model, X, y, cv=5, scoring="r2")
print("CV R2 scores:", cv_scores)
print("CV Mean R2:", cv_scores.mean())

# Save model
joblib.dump(model, "programs/day5/final_model.pkl")
print("Final model saved.")
