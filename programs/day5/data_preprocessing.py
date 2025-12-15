import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os
DATA_PATH = r"D:\learning_journey\programs\day5\data\salary_data.csv"
OUTPUT_PATH = r"D:\learning_journey\programs\day5\data\cleaned_salary.csv"


df = pd.read_csv(DATA_PATH)

print("Shape:", df.shape)

print("Missing values:\n", df.isnull().sum())

df.fillna(df.mean(numeric_only=True), inplace=True)

scaler = MinMaxScaler()
df["YearsExperience"] = scaler.fit_transform(df[["YearsExperience"]])

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
df.to_csv(OUTPUT_PATH, index=False)

print("Cleaned data saved.")
