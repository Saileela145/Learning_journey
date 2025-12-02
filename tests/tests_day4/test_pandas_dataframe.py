import pandas as pd

def test_dataframe_creation():
    # Create a simple dataframe
    df = pd.DataFrame({
        "name": ["a", "b", "c"],
        "age": [10, 20, 30]
    })

    # Check columns
    assert list(df.columns) == ["name", "age"]
    # Check number of rows
    assert len(df) == 3


def test_dataframe_filtering():
    df = pd.DataFrame({
        "name": ["a", "b", "c"],
        "age": [10, 20, 30]
    })

    # Filter age > 10
    filtered = df[df["age"] > 10]

    # Should return rows with age 20 and 30
    assert len(filtered) == 2
    assert list(filtered["age"]) == [20, 30]
