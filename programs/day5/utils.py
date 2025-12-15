import pandas as pd
import math
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def load_and_clean(path):
    df = pd.read_csv(path)
    df.fillna(df.mean(numeric_only=True), inplace=True)
    return df


def scale_features(df, column="YearsExperience"):
    scaler = MinMaxScaler()
    df[column] = scaler.fit_transform(df[[column]])
    return df


def train_linear_model(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model


def evaluate_model(model, X, y):
    preds = model.predict(X)
    return {
        "mae": mean_absolute_error(y, preds),
        "rmse": math.sqrt(mean_squared_error(y, preds)),
        "r2": r2_score(y, preds),
    }


def cross_validate(model, X, y, cv=5):
    return cross_val_score(model, X, y, cv=cv, scoring="r2").mean()


def polynomial_r2(X, y, degree=3):
    poly = PolynomialFeatures(degree=degree)
    X_poly = poly.fit_transform(X)
    model = LinearRegression()
    model.fit(X_poly, y)
    return r2_score(y, model.predict(X_poly))
