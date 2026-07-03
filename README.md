# 🚗 ADAS System for Indian Roads

> **An AI-powered Advanced Driver Assistance System (ADAS) for Indian road scenarios using Ultralytics YOLOv8 and YOLO26 object detection models trained on the DIRS21 dataset.**

---

## 📖 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Dataset](#dataset)
- [Models Used](#models-used)
- [Training Configuration](#training-configuration)
- [Results](#results)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [Author](#author)


## 📌 Project Overview

Road traffic in India presents unique challenges due to high vehicle density, mixed traffic conditions, frequent pedestrian movement, and the presence of vehicles such as auto-rickshaws that are often absent from conventional driving datasets.

This project develops an **AI-powered Advanced Driver Assistance System (ADAS)** capable of detecting multiple road users in real time using state-of-the-art **Ultralytics YOLO object detection models**. The models were trained on the **DIRS21 (Dataset for Indian Road Scenarios)** to improve detection performance in realistic Indian driving environments.

To evaluate modern object detection architectures, two different models were trained and compared:

- **YOLOv8n**
- **YOLO26n**

Both models were trained using identical datasets and training configurations, allowing a fair comparison of their detection accuracy, precision, recall, and mAP performance.

The final system demonstrates accurate detection of multiple traffic participants and serves as a foundation for future ADAS features such as lane detection, collision warning, traffic sign recognition, and autonomous driving assistance.


## ✨ Features

- 🚗 Real-time vehicle detection using Ultralytics YOLO models
- 🛺 Detection of Indian road-specific vehicles such as Auto Rickshaws
- 🚌 Multi-class object detection across seven traffic categories
- 📊 Comparative evaluation of YOLOv8n and YOLO26n
- 📈 Automatic performance evaluation using Precision, Recall, mAP@50 and mAP@50-95
- ⚡ GPU-accelerated training using CUDA
- 📦 Training pipeline with automatic dataset splitting
- 🛑 Early stopping to prevent overfitting
- 📉 Automatic loss and metric visualization generated after training


## 📂 Dataset

**Dataset Used:** DIRS21 (Dataset for Indian Road Scenarios)

The dataset contains real-world Indian traffic scenes and includes multiple classes commonly encountered on Indian roads.

### Dataset Split

| Split | Percentage |
|--------|------------|
| Training | 80% |
| Validation | 10% |
| Testing | 10% |

### Classes

- Auto Rickshaw
- Bicycle
- Bus
- Car
- Motorcycle
- Person
- Truck


## 🤖 Models Used

Two Ultralytics object detection models were trained and evaluated.

| Model | Purpose |
|---------|----------|
| YOLOv8n | Baseline Model |
| YOLO26n | Improved architecture for comparison |


## ⚙️ Training Configuration

| Parameter | Value |
|-----------|-------|
| Framework | Ultralytics |
| Language | Python |
| Image Size | 640 × 640 |
| Batch Size | 8 |
| Optimizer | AdamW (Auto) |
| Device | NVIDIA GPU (CUDA) |
| Early Stopping | Patience = 10 |
| Dataset Split | 80 / 10 / 10 |
| Data Augmentation | Mosaic, Flip, Scale, HSV Augmentation |


## 📊 Model Performance

| Metric | YOLOv8n (60 Epochs) | YOLO26n (60 Epochs) |
|---------|--------------------|---------------------|
| Detection Accuracy | 79.40% | **80.48%** |
| Precision | 81.68% | **84.50%** |
| Recall | **77.13%** | 76.47% |
| mAP@50 | **85.48%** | 85.14% |
| mAP@50-95 | 48.54% | **49.07%** |

### Observations

- YOLO26n achieved the highest overall detection accuracy.
- YOLO26n produced higher precision, reducing false detections.
- YOLOv8n achieved a slightly higher recall, detecting more true objects.
- Both models achieved comparable mAP@50 values above 85%.
- YOLO26n achieved the best mAP@50-95, indicating stronger localization performance across different IoU thresholds.


