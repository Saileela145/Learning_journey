import pandas as pd
import os

def test_cleaned_file_exists():
    assert os.path.exists("programs/day5/data/cleaned_salary.csv")

def test_no_missing_values():
    df = pd.read_csv("programs/day5/data/cleaned_salary.csv")
    assert df.isnull().sum().sum() == 0
