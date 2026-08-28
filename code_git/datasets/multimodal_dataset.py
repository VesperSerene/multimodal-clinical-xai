import torch


def create_dummy_multimodal_sample():

    # --------------------------------
    # Dummy EHR
    #
    # 48 hours
    # 49 EHR features
    # --------------------------------

    ehr = torch.zeros(
        48,
        49,
        dtype=torch.float32
    )


    # --------------------------------
    # Dummy text
    #
    # 之后这里会替换成真实 report
    # --------------------------------

    text = (
        "No acute cardiopulmonary abnormality."
    )


    # --------------------------------
    # Dummy phenotype labels
    #
    # CareBench phenotype = 25 labels
    # --------------------------------

    labels = torch.zeros(
        25,
        dtype=torch.float32
    )


    # --------------------------------
    # 模拟一个 multimodal sample
    # --------------------------------

    sample = {

        "ehr": ehr,

        "image": None,

        "text": text,

        "labels": labels,

        "has_ehr": True,

        "has_image": False,

        "has_text": True,

        "subject_id": None,

        "study_id": None,

        "dicom_id": None
    }


    return sample


if __name__ == "__main__":

    sample = (
        create_dummy_multimodal_sample()
    )

    print(
        "EHR shape:",
        sample["ehr"].shape
    )

    print(
        "Text:",
        sample["text"]
    )

    print(
        "Label shape:",
        sample["labels"].shape
    )

    print(
        "has_ehr:",
        sample["has_ehr"]
    )

    print(
        "has_image:",
        sample["has_image"]
    )

    print(
        "has_text:",
        sample["has_text"]
    )