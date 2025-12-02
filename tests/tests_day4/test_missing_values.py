import pandas as pd

def test_dropna():
    df = pd.DataFrame({
        "a": [1, None, 3]
    })

    # Drop missing values
    cleaned = df.dropna()

    # Only 2 values should remain
    assert len(cleaned) == 2
    assert list(cleaned["a"]) == [1, 3]


def test_fillna():
    df = pd.DataFrame({
        "a": [1, None, 3]
    })

    # Replace missing with 0
    filled = df.fillna(0)

    assert list(filled["a"]) == [1, 0, 3]
