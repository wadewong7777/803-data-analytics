from pathlib import Path
import os

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "Data_set_w1A1.xlsx"
CHART_FILE = BASE_DIR / "category_sales_bar.png"
SUMMARY_FILE = BASE_DIR / "w1a1_summary.txt"

os.environ.setdefault("MPLCONFIGDIR", str(BASE_DIR / ".matplotlib-cache"))

import matplotlib.pyplot as plt


def main() -> None:
    df = pd.read_excel(DATA_FILE, sheet_name="descriptive_aggregation (1)")

    # Keep category order from the spreadsheet and plot the main total metric.
    df = df.sort_values("category")

    top_category = df.loc[df["sales_sum"].idxmax(), "category"]
    top_sales = df["sales_sum"].max()

    summary = [
        "Week 1 Activity 1 Analysis",
        "",
        f"Rows: {len(df)}",
        f"Columns: {', '.join(df.columns)}",
        "",
        "Sales by category:",
        df[["category", "sales_sum", "sales_mean", "sales_count"]].to_string(index=False),
        "",
        f"Highest total sales: Category {top_category} with {top_sales:,.0f}",
    ]

    SUMMARY_FILE.write_text("\n".join(summary), encoding="utf-8")

    plt.figure(figsize=(7, 4.5))
    plt.bar(df["category"], df["sales_sum"], color="#4C78A8")
    plt.title("Total Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Sales")
    plt.grid(axis="y", linestyle="--", alpha=0.35)
    plt.tight_layout()
    plt.savefig(CHART_FILE, dpi=160)
    plt.close()

    print("\n".join(summary))
    print(f"\nSaved chart: {CHART_FILE}")
    print(f"Saved summary: {SUMMARY_FILE}")


if __name__ == "__main__":
    main()
