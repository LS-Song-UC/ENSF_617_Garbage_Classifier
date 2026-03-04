# ENSF-617 Assignment 2 - Garbage Classification

## Flowchart
![Flowchart](./assets/Garbage_Classification_Transfer_Learning_Flowchart.png)

## Jupyter Notebooks
1. Garbage_Classification_Distill_BERT_Text.ipynb
2. Garbage_Classification_ResNET50_TL_Image_Fine-tuning.ipynb
3. Garbage_Classification_ResNet50_TL_Image_Frozen.ipynb
4. Garbage_Classification_ResNET+Distill_BERT_MM_Learning.ipynb

## Python Scripts
1. garbage_classifier_fusion_learning(TALC_ver_Full_Multimodal).py

## Results
**Confusion Matrix and Metrics**
![Run Resulting Confusion Matrix and Metrics](./assets/Run%20Resulting%20Confusion%20Matrix%20and%20Metrics.png)


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
├── mm_confusion_matrix.png
├── mm_misclassified_final.txt
├── multimodal_loss_curve1.png
├── old_multimodal_loss_curve1.png
├── ResNET_garbage_loss_chart_image_Fine_Tuned.png
├── Stats for Report.rtf
└── Text_loss_curve.png
```

# Misclassified Images

#### Black (True = 0)
**Kleenex_Box_74.png**
Prediction: Blue | Actual: Black
![Misclassified Item](./assets/misclassified_images/Kleenex_Box_74\.png)

**Soiled_Cling_Wrap_953.png**
Prediction: Green | Actual: Black
![Misclassified Item](./assets/misclassified_images/Soiled_Cling_Wrap_953.png)

**Air_Freshener_915.png**
Prediction: TTR | Actual: Black
![Misclassified Item](./assets/misclassified_images/Air_Freshener_915.png)

#### Blue (True = 1)
**Disposable_cup_13.png**
Prediction: Green | Actual: Blue
![Misclassified Item](./assets/misclassified_images/Disposable_cup_13.png)

**Dirty_Take_Out_Container_119.png**
Prediction: Green | Actual: Blue
![Misclassified Item](./assets/misclassified_images/Dirty_Take_Out_Container_119.png)

**Glass_Pot_72.png**
Prediction: TTR | Actual: Blue
![Misclassified Item](./assets/misclassified_images/Glass_Pot_72.png)

#### Green (True = 2)
**chewed_gum_1993.png**
Prediction: Black | Actual: Green
![Misclassified Item](./assets/misclassified_images/chewed_gum_1993.png)

**Food_Container_71.png**
Prediction: Blue | Actual: Green
![Misclassified Item](./assets/misclassified_images/Food_Container_71.png)

**Wooden_Stirstick_39.png**
Prediction: TTR | Actual: Green
![Misclassified Item](./assets/misclassified_images/Wooden_Stirstick_39.png)

#### TTR (True = 3)
**CD_case_2519.png**
Prediction: Black | Actual: TTR
![Misclassified Item](./assets/misclassified_images/CD_case_2519.png)

**Air_freshener_spray_bottle_2133.png**
Prediction: Blue | Actual: TTR
![Misclassified Item](./assets/misclassified_images/Air_freshener_spray_bottle_2133.png)

**Used_napkin_2723.png**
Prediction: Green | Actual: TTR
![Misclassified Item](./assets/misclassified_images/Used_napkin_2723.png)
