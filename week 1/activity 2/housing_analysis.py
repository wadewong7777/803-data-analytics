from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
os.environ.setdefault("MPLCONFIGDIR", str(BASE_DIR / ".matplotlib-cache"))

import matplotlib.pyplot as plt
import pandas as pd

DATA_FILE = BASE_DIR / "Housing.csv"
SUMMARY_FILE = BASE_DIR / "housing_story_summary.txt"
DISTRIBUTION_CHART = BASE_DIR / "housing_price_distribution.png"
AREA_CHART = BASE_DIR / "housing_area_quartiles.png"
FEATURE_CHART = BASE_DIR / "housing_feature_premiums.png"

PRICE_SCALE = 1_000_000


def money_millions(value: float) -> str:
    return f"{value / PRICE_SCALE:.2f}M"


def add_bar_labels(ax, values, fmt="{:.2f}M", horizontal=False):
    for i, value in enumerate(values):
        if horizontal:
            ax.text(value + 0.04, i, fmt.format(value), va="center", fontsize=10)
        else:
            ax.text(i, value + 0.07, fmt.format(value), ha="center", fontsize=10)


def main() -> None:
    df = pd.read_csv(DATA_FILE)
    df["price_m"] = df["price"] / PRICE_SCALE

    mean_price = df["price"].mean()
    median_price = df["price"].median()

    summary_lines = [
        "Housing Prices Dataset - Initial Story",
        "",
        f"Rows: {len(df)}",
        f"Columns: {', '.join(df.columns)}",
        f"Average price: {money_millions(mean_price)}",
        f"Median price: {money_millions(median_price)}",
        f"Lowest price: {money_millions(df['price'].min())}",
        f"Highest price: {money_millions(df['price'].max())}",
        "",
        "Main numeric relationships with price:",
    ]

    numeric_corr = (
        df[["price", "area", "bedrooms", "bathrooms", "stories", "parking"]]
        .corr(numeric_only=True)["price"]
        .sort_values(ascending=False)
    )
    for feature, corr in numeric_corr.items():
        if feature != "price":
            summary_lines.append(f"- {feature}: correlation {corr:.2f}")

    df["area_group"] = pd.qcut(
        df["area"],
        4,
        labels=["Smallest 25%", "Lower-mid 25%", "Upper-mid 25%", "Largest 25%"],
    )
    area_summary = (
        df.groupby("area_group", observed=True)
        .agg(count=("price", "size"), average_price=("price", "mean"), median_area=("area", "median"))
        .reset_index()
    )

    features = ["airconditioning", "mainroad", "prefarea", "guestroom", "hotwaterheating", "basement"]
    feature_rows = []
    for feature in features:
        means = df.groupby(feature)["price"].mean()
        premium = means.get("yes", 0) - means.get("no", 0)
        feature_rows.append(
            {
                "feature": feature,
                "yes_count": int((df[feature] == "yes").sum()),
                "no_count": int((df[feature] == "no").sum()),
                "yes_average": means.get("yes", 0),
                "no_average": means.get("no", 0),
                "premium": premium,
            }
        )
    feature_summary = pd.DataFrame(feature_rows).sort_values("premium", ascending=False)

    summary_lines.extend([
        "",
        "Average price by area quartile:",
        area_summary.to_string(index=False),
        "",
        "Average price premium for yes/no features:",
        feature_summary.to_string(index=False),
        "",
        "Initial story:",
        "Housing prices rise most clearly with area. Comfort and access features also separate higher-priced homes from lower-priced homes. The strongest simple premiums are air conditioning, main road access, preferred area, and guestroom availability. These are descriptive patterns, not proof of causation.",
    ])
    SUMMARY_FILE.write_text("\n".join(summary_lines), encoding="utf-8")

    plt.style.use("seaborn-v0_8-whitegrid")

    fig, ax = plt.subplots(figsize=(9, 5.2))
    ax.hist(df["price_m"], bins=18, color="#4C78A8", edgecolor="white")
    ax.axvline(mean_price / PRICE_SCALE, color="#F58518", linewidth=2.2, label=f"Mean {money_millions(mean_price)}")
    ax.axvline(median_price / PRICE_SCALE, color="#54A24B", linewidth=2.2, label=f"Median {money_millions(median_price)}")
    ax.set_title("Most Housing Prices Sit in the Middle Market", fontsize=15, weight="bold")
    ax.set_xlabel("Price (millions)")
    ax.set_ylabel("Number of houses")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(DISTRIBUTION_CHART, dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5.2))
    x_labels = area_summary["area_group"].astype(str)
    y_values = area_summary["average_price"] / PRICE_SCALE
    ax.bar(x_labels, y_values, color=["#72B7B2", "#54A24B", "#ECA82C", "#E45756"])
    ax.set_title("Average Price Rises with House Area", fontsize=15, weight="bold")
    ax.set_xlabel("Area group")
    ax.set_ylabel("Average price (millions)")
    ax.set_ylim(0, max(y_values) + 1.0)
    add_bar_labels(ax, y_values)
    fig.tight_layout()
    fig.savefig(AREA_CHART, dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5.2))
    chart_data = feature_summary.copy()
    chart_data["premium_m"] = chart_data["premium"] / PRICE_SCALE
    labels = [
        "Air conditioning",
        "Main road",
        "Preferred area",
        "Guest room",
        "Hot water heating",
        "Basement",
    ]
    label_map = dict(zip(features, labels))
    chart_labels = chart_data["feature"].map(label_map)
    ax.barh(chart_labels, chart_data["premium_m"], color="#4C78A8")
    ax.invert_yaxis()
    ax.set_title("Comfort and Location Features Add Price Premiums", fontsize=15, weight="bold")
    ax.set_xlabel("Average price difference: Yes minus No (millions)")
    add_bar_labels(ax, chart_data["premium_m"], horizontal=True)
    ax.set_xlim(0, chart_data["premium_m"].max() + 0.6)
    fig.tight_layout()
    fig.savefig(FEATURE_CHART, dpi=180)
    plt.close(fig)

    print("Saved analysis files:")
    for file_path in [SUMMARY_FILE, DISTRIBUTION_CHART, AREA_CHART, FEATURE_CHART]:
        print(f"- {file_path}")


if __name__ == "__main__":
    main()
