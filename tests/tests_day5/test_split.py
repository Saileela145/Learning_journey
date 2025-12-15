import pandas as pd
from sklearn.model_selection import train_test_split

def test_train_test_split_sizes():
    df = pd.read_csv("programs/day5/data/cleaned_salary.csv")
    X = df[["YearsExperience"]]
    y = df["Salary"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    assert len(X_train) == 16
    assert len(X_test) == 4
