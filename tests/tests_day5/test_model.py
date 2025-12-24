import subprocess

def test_pipeline_runs():
    result = subprocess.run(
        ["python", "programs/day5/run_pipeline.py"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
