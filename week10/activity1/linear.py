import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
plt.tight_layout()
plt.savefig("week10/activity1/regression_comparison.png", dpi=300)
