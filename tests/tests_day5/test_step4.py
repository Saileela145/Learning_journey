import os

def test_pipeline_entry_exists():
    assert os.path.exists("programs/day5/run_pipeline.py")
