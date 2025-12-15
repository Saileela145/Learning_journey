import os

def test_step2_files_exist():
    assert os.path.exists("programs/day5/visualize_model.py")
    assert os.path.exists("programs/day5/polynomial_regression.py")
    assert os.path.exists("programs/day5/residual_analysis.py")
