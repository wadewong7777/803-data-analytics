from pathlib import Path

import matplotlib
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    csv_path = base_dir / "age_networth.csv"

    df = pd.read_csv(csv_path)

    x = df["Age"]
    y = df["Net Worth"]

    plt.scatter(x, y)
    plt.xlabel("Age")
    plt.ylabel("Net Worth")
    plt.title("Age vs Net Worth")

    output_path = base_dir / "age_networth_scatter.png"
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()

    print(f"Saved plot to {output_path}")
    print("Correlation:", x.corr(y))


if __name__ == "__main__":
    main()
