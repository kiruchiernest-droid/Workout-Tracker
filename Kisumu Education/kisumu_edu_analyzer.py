import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Create Sample DataFrames with Intended Flaws
# Inconsistencies: 'Manyatta Primary School' vs 'Manyatta Pri', 'Kondele Academy' vs 'Kondele Acad'
# Missing values: NaN in attendance for Kibuye Mixed
# Duplicate row: Kondele Acad has an exact duplicate in the infrastructure file
attendance_data = {
    "school_name": [
        "Manyatta Primary School",
        "Milimani School",
        "Kondele Academy",
        "Kibuye Mixed",
        "Nyabondo Boys",
    ],
    "average_attendance_pct": [92.5, 88.0, 95.2, np.nan, 85.6],
    "county": ["Kisumu", "Kisumu", "Kisumu", "Kisumu", "Kisumu"],
}

infra_data = {
    "school_name": [
        "Manyatta Pri",
        "Milimani School",
        "Kondele Acad",
        "Kondele Acad",
        "Kibuye Mixed",
        "Nyabondo Boys",
    ],
    "num_classrooms": [12, 8, 20, 20, 6, 15],
    "water_access": ["Yes", "Yes", "Yes", "Yes", "No", "Yes"],
}

df_attendance = pd.DataFrame(attendance_data)
df_infra = pd.DataFrame(infra_data)


# 2. Data Cleaning Pipeline
def standardize_school_names(name):
    """Normalizes variations in school name strings."""
    return (
        name.strip()
        .lower()
        .replace("primary school", "pri")
        .replace("academy", "acad")
    )


# Standardize merge keys
df_attendance["merge_key"] = df_attendance["school_name"].apply(
    standardize_school_names
)
df_infra["merge_key"] = df_infra["school_name"].apply(
    standardize_school_names
)

# Deduplicate the infrastructure dataset
df_infra_cleaned = df_infra.drop_duplicates(subset=["merge_key"])

# Handle missing values in attendance records
df_attendance_cleaned = df_attendance.dropna(subset=["average_attendance_pct"])

# 3. Merge & Analyze
df_merged = pd.merge(
    df_attendance_cleaned, df_infra_cleaned, on="merge_key"
).drop(columns=["merge_key"])

# Calculate Pearson Correlation Coefficient
correlation_coefficient = df_merged["num_classrooms"].corr(
    df_merged["average_attendance_pct"]
)
print(f"Calculated Pearson Correlation: {correlation_coefficient:.4f}")
