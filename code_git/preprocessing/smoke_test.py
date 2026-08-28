from pathlib import Path
import pandas as pd


# ============================================================
# 1. 自动找到 project 根目录
# ============================================================

# 当前文件：
# D:\um\p1\project\preprocessing\smoke_test.py
#
# parent 是 preprocessing
# parent.parent 就是 project

PROJECT_ROOT = Path(__file__).resolve().parent.parent


# ============================================================
# 2. 定义数据路径
# ============================================================

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


# ============================================================
# 3. 先检查文件夹和 metadata 是否存在
# ============================================================

print("=" * 60)
print("STEP 1: Check project paths")
print("=" * 60)

print("Project root:")
print(PROJECT_ROOT)

print("\nMetadata path:")
print(METADATA_PATH)

print("\nMetadata exists:")
print(METADATA_PATH.exists())

print("\nReport root:")
print(REPORT_ROOT)

print("\nReport root exists:")
print(REPORT_ROOT.exists())


# 如果 metadata 不存在，直接停止
if not METADATA_PATH.exists():
    print("\nERROR:")
    print("Cannot find metadata file.")
    print("Please check:")
    print(METADATA_PATH)
    raise SystemExit


# ============================================================
# 4. 读取 metadata
# ============================================================

print("\n" + "=" * 60)
print("STEP 2: Read CXR metadata")
print("=" * 60)

df = pd.read_csv(METADATA_PATH)

print("Metadata loaded successfully.")

print("\nNumber of CXR records:")
print(len(df))

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(
    df[
        [
            "dicom_id",
            "subject_id",
            "study_id"
        ]
    ].head()
)


# ============================================================
# 5. 取第一条记录
# ============================================================

row = df.iloc[0]

subject_id = str(row["subject_id"])
study_id = str(row["study_id"])
dicom_id = str(row["dicom_id"])


print("\n" + "=" * 60)
print("STEP 3: Test one CXR-report linkage")
print("=" * 60)

print("dicom_id:")
print(dicom_id)

print("\nsubject_id:")
print(subject_id)

print("\nstudy_id:")
print(study_id)


# ============================================================
# 6. 根据 subject_id 和 study_id 找 report
# ============================================================

# 例如:
#
# subject_id = 10000032
#
# subject folder:
# p10000032
#
# group folder:
# p10

group_folder = f"p{subject_id[:2]}"

report_path = (
    REPORT_ROOT
    / "files"
    / group_folder
    / f"p{subject_id}"
    / f"s{study_id}.txt"
)


print("\nExpected report path:")
print(report_path)

print("\nReport exists:")
print(report_path.exists())


# ============================================================
# 7. 如果找到 report，就读取前 1000 个字符
# ============================================================

if report_path.exists():

    with open(
        report_path,
        "r",
        encoding="utf-8"
    ) as f:

        report_text = f.read()

    print("\n" + "=" * 60)
    print("STEP 4: Report preview")
    print("=" * 60)

    print(report_text[:1000])

    print("\n")
    print("=" * 60)
    print("SMOKE TEST PASSED")
    print("=" * 60)

else:

    print("\n")
    print("=" * 60)
    print("REPORT NOT FOUND")
    print("=" * 60)

    print(
        "\nThis usually means your report folder "
        "has one extra directory level."
    )

    print(
        "\nLook inside:"
    )

    print(REPORT_ROOT)

    print(
        "\nand find where the 'files' folder actually is."
    )