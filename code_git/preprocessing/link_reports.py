from pathlib import Path
import pandas as pd


# ============================================================
# 1. Project paths
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent


METADATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "mimic_cxr_jpg"
    / "mimic-cxr-2.0.0-metadata.csv.gz"
)


REPORT_ROOT = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "mimic_cxr_reports"
)


OUTPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "cxr_report_index.csv"
)


# ============================================================
# 2. Read metadata
# ============================================================

print("Loading CXR metadata...")

df = pd.read_csv(METADATA_PATH)

print("Metadata loaded.")

print(
    "Number of CXR records:",
    len(df)
)


# ============================================================
# 3. Function for building report path
# ============================================================

def build_report_path(
    subject_id,
    study_id
):

    subject_id = str(subject_id)

    study_id = str(study_id)

    group_folder = (
        f"p{subject_id[:2]}"
    )

    report_path = (
        REPORT_ROOT
        / "files"
        / group_folder
        / f"p{subject_id}"
        / f"s{study_id}.txt"
    )

    return report_path


# ============================================================
# 4. Create report path for every CXR record
# ============================================================

print(
    "Building report paths..."
)


df["report_path"] = [

    str(
        build_report_path(
            subject_id,
            study_id
        )
    )

    for subject_id, study_id in zip(
        df["subject_id"],
        df["study_id"]
    )
]


# ============================================================
# 5. Check whether reports exist
# ============================================================

print(
    "Checking report files..."
)


df["has_report"] = [

    Path(path).exists()

    for path in df["report_path"]
]


# ============================================================
# 6. Keep only useful linkage columns
# ============================================================

output_df = df[
    [
        "dicom_id",
        "subject_id",
        "study_id",
        "report_path",
        "has_report"
    ]
].copy()


# ============================================================
# 7. Save
# ============================================================

OUTPUT_PATH.parent.mkdir(
    parents=True,
    exist_ok=True
)


output_df.to_csv(
    OUTPUT_PATH,
    index=False
)


# ============================================================
# 8. Print basic results
# ============================================================

print("\nFinished.")

print(
    "\nOutput saved to:"
)

print(
    OUTPUT_PATH
)

print(
    "\nTotal CXR records:",
    len(output_df)
)

print(
    "Reports found:",
    output_df["has_report"].sum()
)

print(
    "Reports missing:",
    (~output_df["has_report"]).sum()
)