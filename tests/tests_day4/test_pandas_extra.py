import pandas as pd

def test_rename_columns():
    df = pd.DataFrame({
        "a": [1, 2],
        "b": [3, 4]
    })

    renamed = df.rename(columns={"a": "x", "b": "y"})
    assert list(renamed.columns) == ["x", "y"]


def test_describe_function():
    df = pd.DataFrame({
        "age": [10, 20, 30, 40]
    })

    stats = df.describe()

    # mean should be 25
    assert stats.loc["mean", "age"] == 25
