
# 🚀 AR Object Detection using YOLOv5 (Trained Model: exp5 - 50 Epochs)

This project involves training a YOLOv5 model on a custom-labeled dataset and running real-time object detection via webcam to simulate AR interaction. The model is trained for 50 epochs and saved under the `runs/train/exp5/` directory.

---

## 🔧 Setup and Training (Task 4)

### 1️⃣ Clone YOLOv5 and Install Requirements
```bash
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```

### 2️⃣ Dataset Directory Structure

> 📁 Dataset is stored inside the `model/` directory

```
model/dataset/
├── images/
│   ├── train/
│   └── val/
├── labels/
│   ├── train/
│   └── val/
└── data.yaml
```

### 3️⃣ Sample `data.yaml` File
```yaml
train: ../model/images/train
val: ../model/images/val

nc: 1
names: ['your_class_name']
```

### 4️⃣ Start Training with YOLOv5s for 50 Epochs
```bash
python train.py --img 640 --batch 16 --epochs 50 --data data.yaml --weights yolov5s.pt --device cpu
```

- 📁 Outputs stored in: `runs/train/exp5/`
- 🧠 Final trained weights: `runs/train/exp5/weights/best.pt`

---

## 🖼️ Image Results and Logs from Training
- `results.png`: Accuracy, precision, recall plots
- `confusion_matrix.png`: Visual matrix of predictions
- `F1_curve.png`, `PR_curve.png`, `R_curve.png`, `P_curve.png`: Evaluation metrics
- `train_batch*.jpg`: Training sample predictions
- `val_batch0_pred.jpg`, `val_batch0_labels.jpg`: Validation predictions
- `results.csv`: Raw performance logs
- `best.pt`: Trained model weights

---

## 🧪 Real-Time Webcam Detection (Task 5)

### 5️⃣ Run Real-Time Detection from Webcam
```bash
python detect.py --weights runs/train/exp5/weights/best.pt --img 640 --conf 0.25 --source 0
```

- 📸 Opens your webcam
- 🔲 Draws real-time bounding boxes over detected objects
- 📁 Detection results (captured frames or logs) saved in: `runs/detect/exp*/`

---

✅ **Completed:**
- Custom dataset collection and labeling with MakeSense.ai
- Model training for 50 epochs using YOLOv5s
- Live detection using webcam
