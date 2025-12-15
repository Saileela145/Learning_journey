import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

df = pd.read_csv("programs/day5/data/cleaned_salary.csv")

X = df[["YearsExperience"]]
y = df["Salary"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Linear Model
lin = LinearRegression()
lin.fit(X_train, y_train)

train_r2_lin = r2_score(y_train, lin.predict(X_train))
test_r2_lin = r2_score(y_test, lin.predict(X_test))

print("Linear Regression")
print("Train R2:", train_r2_lin)
print("Test R2:", test_r2_lin)

# Polynomial Model (degree 3)
poly = PolynomialFeatures(degree=3)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

train_r2_poly = r2_score(y_train, poly_model.predict(X_train_poly))
test_r2_poly = r2_score(y_test, poly_model.predict(X_test_poly))

print("\nPolynomial Regression (degree=3)")
print("Train R2:", train_r2_poly)
print("Test R2:", test_r2_poly)
