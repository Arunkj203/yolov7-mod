# YOLOv7-MOD | Architecture Reimplementation & Enhancement

**Reimplementation of YOLOv7-MOD as proposed in IEEE Access 2023 (Wibowo et al.) for object detection in dense and mixed traffic.**
This project validates and enhances the published work by integrating **Deformable Convolutions** and modified **ELAN layers**, achieving reproducible improvements on the **BDD100K dataset**.

---

## 📖 Background

The paper *“Object Detection in Dense and Mixed Traffic for Autonomous Vehicles With Modified YOLO”* (IEEE Access, 2023) introduces YOLOv7-MOD, designed to handle:

* Small, faint, and partially occluded objects.
* Congested traffic scenarios common in developing countries.
* Custom datasets (Bandung traffic) and BDD100K for evaluation.

**Key modifications:**

* Integration of **Deformable Convolutions** for adaptive receptive fields.
* Use of **Soft-NMS** for better handling of overlapping detections.
* Architecture enhancements (modified ELAN layers).

---

## 🚀 Features

* **Reproducible YOLOv7-MOD architecture** (faithful to IEEE Access 2023).
* **Deformable Convolutions** for improved robustness to geometric variations.
* **Modified ELAN Layers** for stronger feature extraction.
* **BDD100K Evaluation** for benchmarking in real-world conditions.
* **Significant Gains**: +6% Precision, +8% Recall, +10% mAP compared to baseline.

---

## 🛠️ Tech Stack

* **Framework**: PyTorch
* **Model Base**: YOLOv7
* **Enhancements**: Deformable Convolutions, ELAN modifications, Soft-NMS
* **Datasets**:

  * Custom Bandung Traffic Dataset (from the paper)
  * BDD100K (for validation & scaling)

---

## 📦 Installation & Setup

1. **Clone Repository**

   ```bash
   git clone https://github.com/your-username/yolov7-mod.git
   cd yolov7-mod
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Download Pretrained Weights**

   * Official YOLOv7 weights for initialization.
   * Place them in the `weights/` folder.

4. **Prepare Dataset**

   * [BDD100K dataset](https://bdd-data.berkeley.edu/) or custom traffic dataset.
   * Convert to YOLO annotation format under `datasets/`.

---

## 📊 Training & Evaluation

### Train

```bash
python train.py --cfg cfg/yolov7-mod.yaml --data data/bdd.yaml --weights weights/yolov7.pt --epochs 100
```

### Test

```bash
python test.py --data data/bdd.yaml --weights runs/train/exp/weights/best.pt
```

---

## 📈 Results

### Paper Results (YOLOv7-MOD on Bandung Dataset)

* Precision: **96.87%**
* Recall: **94.68%**
* F1-score: **95.76%**
* mAP: **+1.05%** over baseline YOLOv7

### Our Reimplementation (BDD100K, smaller scale)

* **+6% Precision**
* **+8% Recall**
* **+10% mAP** over baseline YOLOv7

---

## 📜 Reference

If you use this work, please cite the original paper:

**A. Wibowo, B. R. Trilaksono, E. M. I. Hidayat, and R. Munir**,
*Object Detection in Dense and Mixed Traffic for Autonomous Vehicles With Modified YOLO,*
in **IEEE Access**, vol. 11, pp. 134866-134877, Dec. 2023, doi: [10.1109/ACCESS.2023.3335826](https://doi.org/10.1109/ACCESS.2023.3335826).

---


Do you want me to **add a side-by-side table** (Paper vs Your Reimplementation results) so the improvement is crystal clear in the README?
