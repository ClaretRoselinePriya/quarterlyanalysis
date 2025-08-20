# analysis.py
# Senior Data Analyst: SaaS MRR Performance (2024)
# Contact: 23f3000663@ds.study.iitm.ac.in
#
# Loads quarterly MRR growth, computes summary metrics,
# prints insights, and generates a trend vs target figure.

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA = Path("data/mrr_2024.csv")
TARGET = 15.0

def main():
    df = pd.read_csv(DATA)
    avg = df["mrr_growth"].mean().round(2)
    print(f"Quarterly data:\n{df.to_string(index=False)}\n")
    print(f"Average MRR growth (2024): {avg}")
    print(f"Industry target: {TARGET}")
    gap = round(TARGET - avg, 2)
    print(f"Gap to target: {gap}")

    # Figure
    plt.figure(figsize=(8, 5))
    plt.plot(df["quarter"], df["mrr_growth"], marker="o")
    plt.axhline(TARGET, linestyle="--")
    plt.title("2024 MRR Growth by Quarter vs. Industry Target")
    plt.xlabel("Quarter")
    plt.ylabel("MRR Growth")
    for q, v in zip(df["quarter"], df["mrr_growth"]):
        plt.annotate(f"{v:.2f}", (q, v), textcoords="offset points", xytext=(0,7), ha="center")
    Path("figures").mkdir(exist_ok=True, parents=True)
    out = Path("figures/mrr_trend_vs_target.png")
    plt.tight_layout()
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved figure: {out}")

if __name__ == "__main__":
    main()# minor edit to trigger PR
