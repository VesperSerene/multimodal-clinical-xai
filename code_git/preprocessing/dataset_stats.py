from pathlib import Path
import pandas as pd


# ============================================================
# 1. Project path
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent


INDEX_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "cxr_report_index.csv"
)


# ============================================================
# 2. Read linkage index
# ============================================================

df = pd.read_csv(
    INDEX_PATH
)


# ============================================================
# 3. Calculate statistics
# ============================================================

num_cxr_records = len(df)

num_unique_subjects = (
    df["subject_id"].nunique()
)

num_unique_studies = (
    df["study_id"].nunique()
)

num_reports_found = (
    df["has_report"].sum()
)

num_reports_missing = (
    len(df)
    - num_reports_found
)

report_coverage = (
    df["has_report"].mean()
)

report_missing_rate = (
    1 - report_coverage
)


# ============================================================
# 4. Print results
# ============================================================

print("=" * 60)

print(
    "MIMIC-CXR / Report Linkage Statistics"
)

print("=" * 60)


print(
    "\nCXR records:",
    num_cxr_records
)


print(
    "Unique patients:",
    num_unique_subjects
)


print(
    "Unique studies:",
    num_unique_studies
)


print(
    "Reports found:",
    num_reports_found
)


print(
    "Reports missing:",
    num_reports_missing
)


print(
    "Report coverage:",
    f"{report_coverage:.2%}"
)


print(
    "Report missing rate:",
    f"{report_missing_rate:.2%}"
)


print("=" * 60)