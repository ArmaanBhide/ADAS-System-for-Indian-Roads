# 🚗 ADAS System for Indian Roads

An AI-powered **Advanced Driver Assistance System (ADAS)** developed for Indian road scenarios using **Ultralytics YOLOv8** and **YOLO26** object detection models trained on the **DIRS21** dataset.

---

## 📌 Project Overview

This project aims to improve road safety by detecting vehicles and road users in real time using deep learning.

The system is trained on the **DIRS21 (Dataset for Indian Road Scenarios)** and is capable of detecting:

- 🚗 Car
- 🚌 Bus
- 🛺 Auto Rickshaw
- 🚲 Bicycle
- 🏍 Motorcycle
- 🚶 Person
- 🚚 Truck

---

## 🧠 Models Used

- YOLOv8n
- YOLO26n

---

## 📊 Dataset

- Dataset: DIRS21
- Train: **80%**
- Validation: **10%**
- Test: **10%**

---

## ⚙️ Training Configuration

| Parameter | Value |
|-----------|-------|
| Image Size | 640 × 640 |
| Batch Size | 8 |
| Optimizer | AdamW (Auto) |
| Early Stopping | Patience = 10 |
| Framework | Ultralytics YOLO |
| Hardware | NVIDIA GPU (CUDA) |

---

## 📈 Best Results

| Model | Epochs | Accuracy | Precision | Recall | mAP@50 | mAP@50-95 |
|--------|---------|----------|-----------|--------|---------|------------|
| YOLOv8n | 60 | 79.40% | 81.68% | 77.13% | 85.48% | 48.54% |
| YOLO26n | 60 | **80.48%** | **84.50%** | 76.47% | **85.14%** | **49.07%** |

---

## 🛠 Technologies Used

- Python
- PyTorch
- Ultralytics
- OpenCV
- NumPy
- Pandas
- Matplotlib

---

## 🚀 Future Improvements

- Lane Detection
- Traffic Sign Recognition
- Distance Estimation
- Collision Warning
- Real-time deployment on Jetson Nano

---

## 👨‍💻 Author

**Armaan Bhide**