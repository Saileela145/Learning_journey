import os

def test_final_model_exists():
    assert os.path.exists("programs/day5/final_model.pkl")

def test_pipeline_file_exists():
    assert os.path.exists("programs/day5/final_pipeline.py")
