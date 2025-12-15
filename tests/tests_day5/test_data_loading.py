import pandas as pd

def test_csv_loads():
    df = pd.read_csv("programs/day5/data/salary_data.csv")
    assert not df.empty
