from __future__ import annotations

from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"


def load_dataset() -> tuple[pd.DataFrame, list[str]]:
    """Load and combine the extracted Beijing Multi-Site Air Quality CSV files."""
    if not DATA_DIR.exists():
        raise FileNotFoundError(f"Expected data folder at {DATA_DIR}, but it was not found.")

    csv_paths = sorted(DATA_DIR.rglob("PRSA_Data_*.csv"))
    if not csv_paths:
        raise FileNotFoundError(f"No CSV files found under {DATA_DIR}.")

    frames = [pd.read_csv(path, na_values=["NA"]) for path in csv_paths]

    df = pd.concat(frames, ignore_index=True)
    return df, [path.name for path in csv_paths]


def build_output(df: pd.DataFrame, source_files: list[str]) -> str:
    lines = [
        "Beijing Multi-Site Air Quality",
        f"Source files loaded: {len(source_files)}",
        f"Rows: {len(df)}",
        f"Columns: {df.shape[1]}",
        "",
        "Column names:",
        ", ".join(df.columns),
        "",
        "First 5 rows:",
        df.head().to_string(index=False),
        "",
        "Data types:",
        df.dtypes.astype(str).to_string(),
    ]
    return "\n".join(lines)


def main() -> None:
    df, source_files = load_dataset()
    output = build_output(df, source_files)
    print(output)


if __name__ == "__main__":
    main()
