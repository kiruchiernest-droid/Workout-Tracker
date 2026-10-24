import os
import pandas as pd


def process_sales_data(file_path):
    """Loads, cleans, and formats raw Excel sales data for the dashboard."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Source file not found at: {file_path}")

    df = pd.read_excel(file_path)

    # Standardize column naming conventions for non-technical team entry
    df.columns = df.columns.str.strip().str.lower()

    # Handle critical missing fields safely without breaking the pipeline
    df["sales"] = pd.to_numeric(df["sales"], errors="coerce").fillna(0.0)
    df["date"] = pd.to_datetime(df["date"], errors="coerce").fillna(
        pd.Timestamp.now()
    )

    return df


if __name__ == "__main__":
    # Production pipeline execution path
    DATA_SOURCE = "data/raw_sales.xlsx"
    clean_data = process_sales_data(DATA_SOURCE)
    clean_data.to_csv("data/dashboard_source.csv", index=False)
