import pandas as pd
from programs.day4.mini_project.student_marks_analysis import compute_statistics

def test_compute_statistics():
    # Create a small artificial dataframe
    df = pd.DataFrame({
        "student": ["a", "b", "c"],
        "marks": [10, 20, 30]
    })

    stats = compute_statistics(df)

    # Check mean
    assert stats["mean"] == 20

    # Check median
    assert stats["median"] == 20

    # Check max
    assert stats["max"] == 30

    # Check min
    assert stats["min"] == 10
