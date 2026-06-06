import os
import tempfile
from pathlib import Path

# Use a writable temp folder for Matplotlib cache files.
os.environ["MPLCONFIGDIR"] = str(Path(tempfile.gettempdir()) / "matplotlib-iris-simple")

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "Iris.csv"

# Load the dataset and apply basic cleaning.
df = pd.read_csv(DATA_PATH)
df = df.drop(columns=["Id"]).drop_duplicates().dropna()

X = df[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]]
y = df["Species"]

# Create one simple scatter plot for the dataset.
plt.figure(figsize=(8, 6))
for species in y.unique():
    group = df[df["Species"] == species]
    plt.scatter(group["SepalLengthCm"], group["PetalLengthCm"], label=species)

plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.title("Iris Dataset Visualisation")
plt.legend()
plt.tight_layout()
plt.savefig(BASE_DIR / "iris_scatter.png")
plt.close()

# Split the data into training and testing sets.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train a linear SVM model and make predictions.
model = SVC(kernel="linear")
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Save the evaluation results and cleaned dataset.
results_text = (
    "Iris Dataset Results\n"
    f"Rows after cleaning: {len(df)}\n"
    f"Accuracy: {accuracy_score(y_test, y_pred):.4f}\n"
    f"Precision: {precision_score(y_test, y_pred, average='weighted'):.4f}\n"
    f"Recall: {recall_score(y_test, y_pred, average='weighted'):.4f}\n"
    f"F1 Score: {f1_score(y_test, y_pred, average='weighted'):.4f}\n"
)

print(results_text)
(BASE_DIR / "iris_model_results.txt").write_text(results_text, encoding="utf-8")
df.to_csv(BASE_DIR / "iris_cleaned.csv", index=False)
