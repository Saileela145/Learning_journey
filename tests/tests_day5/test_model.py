import os
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

def test_model_file_created():
    assert os.path.exists("programs/day5/model_salary.pkl")

def test_model_loads():
    model = joblib.load("programs/day5/model_salary.pkl")
    assert isinstance(model, LinearRegression)

def test_model_predicts():
    model = joblib.load("programs/day5/model_salary.pkl")
    df = pd.read_csv("programs/day5/data/cleaned_salary.csv")
    preds = model.predict(df[["YearsExperience"]])
    assert len(preds) == len(df)
