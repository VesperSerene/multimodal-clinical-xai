# Multimodal Clinical XAI

Research codebase for multimodal clinical prediction with missing modalities,
focusing on explanation consistency, faithfulness, and consistency-regularized
training using MIMIC-IV, MIMIC-CXR, and CareBench.

## Research Objective

This project investigates whether attention-based explanation proxies remain
consistent and faithful when one clinical modality is missing.

## Modalities

- Chest X-ray: MIMIC-CXR-JPG
- Radiology report: MIMIC-CXR reports
- Structured EHR: MIMIC-IV

## Prediction Task

25-label phenotype prediction following the CareBench benchmark.

## Project Pipeline

1. Prepare CareBench EHR-CXR cohort
2. Link CXR studies with radiology reports
3. Construct tri-modal dataset
4. Train multimodal baselines
5. Simulate missing modalities
6. Apply explanation-consistency regularization
7. Evaluate prediction, consistency, and faithfulness

## Models

- Concatenation
- Gated Fusion
- Cross-Attention
- Consistency-Regularized Cross-Attention

## Evaluation

Prediction:
- Macro AUPRC
- Macro AUROC
- Micro F1

Explanation consistency:
- Jensen-Shannon Divergence
- Spearman correlation

Explanation faithfulness:
- Deletion AUC
- Insertion AUC

## Data

The MIMIC datasets are not distributed with this repository.
Users must obtain authorized access through PhysioNet.

## Status

Research in progress.