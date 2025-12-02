import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def read_csv_file(path):
    return pd.read_csv(path)
def compute_statistics(df):
    marks=df["marks"].values
    stats={
        "mean":np.mean(marks),
        "median":np.median(marks),
        "max":np.max(marks),
        "min":np.min(marks)
        }
    return stats
def plot_marks(df,output_path):
    plt.figure(figsize=(10,4))
    plt.bar(df["students"],df["marks"])
    plt.xlabel("Student")
    plt.ylabel("Marks")
    plt.title("Student Marks Analysis")
    plt.savefig(output_path)
    plt.close()
if __name__=="__main__":
    df=read_csv_file("students.csv")
    stats=compute_statistics(df)
    print("Statistics:",stats)
    plot_marks(df,"marks_chart.png")
    print("chart saved as marks_chart.png")
