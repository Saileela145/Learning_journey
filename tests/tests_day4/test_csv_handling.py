import pandas as pd

def test_csv_write_and_read(tmp_path):
    # Create a temporary CSV file path
    file = tmp_path / "sample.csv"

    # Create a dataframe
    df = pd.DataFrame({
        "name": ["ram", "sai"],
        "age": [20, 22]
    })

    # Write to CSV
    df.to_csv(file, index=False)

    # Read back
    df_read = pd.read_csv(file)

    # Check same columns
    assert list(df_read.columns) == ["name", "age"]

    # Check values
    assert df_read["age"].sum() == 42
