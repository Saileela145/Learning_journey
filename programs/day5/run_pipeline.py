"""
Single entry-point ML pipeline.
Run once to reproduce Day 5 results.
"""

from pathlib import Path
import joblib

from utils import (
    load_and_clean,
    scale_features,
    train_linear_model,
    evaluate_model,
    cross_validate,
    polynomial_r2,
)

DATA_PATH = "programs/day5/data/salary_data.csv"
MODEL_DIR = Path("programs/day5/models")
MODEL_DIR.mkdir(exist_ok=True)


def main():
    df = load_and_clean(DATA_PATH)
    df = scale_features(df)

    X = df[["YearsExperience"]]
    y = df["Salary"]

    model = train_linear_model(X, y)

    metrics = evaluate_model(model, X, y)
    cv_r2 = cross_validate(model, X, y)
    poly_r2 = polynomial_r2(X, y)

    print("Metrics:", metrics)
    print("CV R2:", cv_r2)
    print("Polynomial R2:", poly_r2)

    joblib.dump(model, MODEL_DIR / "linear_model.pkl")
    print("Model saved via pipeline.")


if __name__ == "__main__":
    main()
