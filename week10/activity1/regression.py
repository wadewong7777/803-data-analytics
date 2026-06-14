import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

## This dataset lacks senior level experience data, so the model may overestimate salaries for higher experience levels.

df = pd.read_csv("week10/activity1/salary-dataset.csv")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.regplot(
    data=df,
    x="YearsExperience",
    y="Salary",
    order=1,
    ci=None,
    ax=axes[0],
    line_kws={"color": "red"},
)
axes[0].set_title("Linear Regression")

sns.regplot(
    data=df,
    x="YearsExperience",
    y="Salary",
    order=3,
    ci=None,
    ax=axes[1],
    line_kws={"color": "green"},
)
axes[1].set_title("Polynomial Regression Degree 3")

plt.tight_layout()
plt.savefig("week10/activity1/regression_comparison.png", dpi=300)

## Polynomial regression is better than linear regression.
linear_model = np.poly1d(np.polyfit(df["YearsExperience"], df["Salary"], 1))
polynomial_model = np.poly1d(np.polyfit(df["YearsExperience"], df["Salary"], 3))

for year in [14, 14.5, 15]:
    print(f"{year} years linear predicted salary: {linear_model(year):.2f}")
    print(f"{year} years polynomial predicted salary: {polynomial_model(year):.2f}")

""" 14 years linear predicted salary: 153441.74
14 years polynomial predicted salary: 138926.10
14.5 years linear predicted salary: 157973.48
14.5 years polynomial predicted salary: 138763.90
15 years linear predicted salary: 162505.22
15 years polynomial predicted salary: 137905.07 """
