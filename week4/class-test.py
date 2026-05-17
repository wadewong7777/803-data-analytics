import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load the dateset
df = pd.read_csv("week4/world_happiness_dataset.csv")

print(df.describe(percentiles=[0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99]))
