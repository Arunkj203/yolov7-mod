# YOLOv7-mod | Architecture Reimplementation & Enhancement

**Reimplementation and enhancement of YOLOv7-mod (based on IEEE Access 2023) with Deformable Convolutions and modified ELAN layers.**
Validated reproducibility of research-level results, achieving significant improvements over baseline YOLOv7 on the **BDD dataset** at smaller scale.

---

## 📖 Overview

This project reimplements the **YOLOv7-mod** architecture as proposed in IEEE Access (2023).
Enhancements include:

* **Deformable Convolutions** for better feature extraction.
* **Modified ELAN layers** for improved learning capacity.

Results show:

* **+6% Precision**
* **+8% Recall**
* **+10% mAP** over the YOLOv7 baseline on **BDD dataset**.

---

## 🚀 Features

* **Reimplementation of Research Architecture** – faithful reproduction of YOLOv7-mod.
* **Deformable Convolutions** – captures geometric variations in objects.
* **Modified ELAN Layers** – optimized layer connectivity for richer features.
* **Training Pipeline** – end-to-end reproducible experiments.
* **BDD Dataset Evaluation** – benchmarked against baseline YOLOv7.

---

## 🛠️ Tech Stack

* **Framework**: PyTorch
* **Model Base**: YOLOv7
* **Enhancements**: Deformable Convolutions, ELAN modifications
* **Dataset**: BDD100K (Berkeley DeepDrive)
* **Logging/Visualization**: TensorBoard, Matplotlib

---

## 📦 Installation & Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/yolov7-mod.git
   cd yolov7-mod
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Download Pretrained Weights**

   * Get baseline YOLOv7 weights from the official repo.
   * Place them in the `weights/` directory.

4. **Prepare Dataset**

   * Download [BDD100K](https://bdd-data.berkeley.edu/) dataset.
   * Organize under `datasets/bdd/` following YOLO format.

---

## 📊 Training & Evaluation

### Train Model

```bash
python train.py --cfg cfg/yolov7-mod.yaml --data data/bdd.yaml --weights weights/yolov7.pt --epochs 100
```

### Evaluate Model

```bash
python test.py --data data/bdd.yaml --weights runs/train/exp/weights/best.pt
```

---

## 📈 Results

| Metric    | YOLOv7 Baseline | YOLOv7-mod (This Work) | Δ Improvement |
| --------- | --------------- | ---------------------- | ------------- |
| Precision | –               | +6%                    | ✅             |
| Recall    | –               | +8%                    | ✅             |
| mAP       | –               | +10%                   | ✅             |

*(Exact baseline numbers can be added when cited from the paper.)*

---

## 📜 Reference

This work is based on:

* **YOLOv7-mod: Enhanced YOLOv7 with Deformable Convolutions and Modified ELAN Layers** – *IEEE Access, 2023*.

If used in academic work, please cite the original paper and this reimplementation.

---

Do you want me to also add a **“Comparison with Paper Results” section** (side-by-side table of your results vs reported results), to make it look more academic?
