# ENSF-617 Assignment 2 - Garbage Classification

## Jupyter Notebooks
1. Garbage_Classification_Distill_BERT_Text.ipynb
2. Garbage_Classification_ResNET50_TL_Image_Fine-tuning.ipynb
3. Garbage_Classification_ResNet50_TL_Image_Frozen.ipynb
4. Garbage_Classification_ResNET+Distill_BERT_MM_Learning.ipynb

## Python Scripts
1. garbage_classifier_fusion_learning(TALC_ver_Full_Multimodal).py

## Results
[Run Resulting Confusion Matrix and Metrics](./Run Resulting Confusion Matrix and Metrics.docx)
This document contains the results after running the complete multimodal training on TALC cluster.

### Run Results

#### Graphs and Outputs
```text
./run_result
.
├── Console_Outputs.rtf
├── Image_loss_curve.png
├── misclassified.txt
├── mm_misclassified.txt
├── multimodal_loss_curve.png
├── slurm-600536.out
└── Text_loss_curve.png

./run_result_latest
.
├── misclassified_image_fine_tuned.txt
├── mm_confusion_matrix.png
├── mm_misclassified_final.txt
├── multimodal_loss_curve1.png
├── old_multimodal_loss_curve1.png
├── ResNET_garbage_loss_chart_image_Fine_Tuned.png
├── Stats for Report.rtf
└── Text_loss_curve.png
```
