# Dog Breed & Pet Image Classifier: CNN Architecture Benchmarking

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=flat&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Torchvision](https://img.shields.io/badge/Torchvision-Models-blue?style=flat&logo=pytorch&logoColor=white)](https://pytorch.org/vision/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A deep learning computer vision pipeline implemented in **PyTorch** and **Torchvision** that benchmarks pre-trained Convolutional Neural Network (CNN) architectures—**ResNet-18**, **VGG-16**, and **AlexNet**—for image classification, object detection (Dog vs. Not-a-Dog), and granular breed identification.

Developed by **Prateek Kalwar** as part of the **Udacity AI Programming with Python Nanodegree**.

---

## 📌 Project Overview

When deploying computer vision models in production, choosing the right model architecture requires balancing **classification accuracy**, **memory footprint**, and **inference latency**. 

This project implements a modular CLI-based evaluation harness to test and benchmark three standard CNN architectures trained on ImageNet (1.2M images across 1,000 object categories):
1. **ResNet-18:** Deep residual learning with skip connections (computationally efficient, avoids vanishing gradients).
2. **VGG-16:** Uniform 3x3 convolution stack with dense fully connected layers (high precision, larger parameter size).
3. **AlexNet:** Foundational deep convolutional architecture (fastest runtime, lower capacity).

---

## ⚙️ Image Preprocessing & Inference Pipeline

Every input image passes through a standardized torchvision transform pipeline matching ImageNet training statistics:

```
[ Raw Image (PIL) ]
        │
        ▼
[ Resize: 256px ]
        │
        ▼
[ Center Crop: 224x224 ]
        │
        ▼
[ Convert to Tensor (0 - 1) ]
        │
        ▼
[ Normalize: mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225] ]
        │
        ▼
[ Forward Pass (model.eval() with no gradients) ]
        │
        ▼
[ Argmax Prediction -> ImageNet Class Mapping ]
```

---

## 📊 Benchmark Metrics & Comparison

The pipeline computes granular evaluation metrics across 40 labeled pet test images:

| Metric | AlexNet | VGG-16 | ResNet-18 | Best Architecture |
| :--- | :---: | :---: | :---: | :---: |
| **% Correct Dog Detection** | `100.0%` | `100.0%` | `100.0%` | **Tie (All 100%)** |
| **% Correct Not-a-Dog Detection** | `100.0%` | `100.0%` | `100.0%` | **Tie (All 100%)** |
| **% Correct Breed Classification** | `80.0%` | `93.3%` | `90.0%` | **VGG-16 (93.3%)** |
| **% Label Match** | `75.0%` | `87.5%` | `82.5%` | **VGG-16 (87.5%)** |
| **Inference Runtime / Latency** | `Fastest` | `Slowest` | `Optimal` | **ResNet-18 (Speed/Accuracy Balance)** |

### Key Architectural Takeaways:
- **VGG-16** achieved the highest breed classification accuracy (**93.3%**), but requires substantially larger memory overhead and higher FLOPs per inference.
- **ResNet-18** delivers near-VGG precision (**90.0%**) while executing at a fraction of the parameter count, making it the most production-viable choice for edge/real-time systems.
- **AlexNet** provides the fastest inference speeds, suitable for resource-constrained or rapid prototyping environments where lower breed accuracy is acceptable.

---

## 📁 Repository Structure

```
.
├── check_images.py              # Main execution script measuring runtime and running evaluation
├── classifier.py                # Preprocessing pipeline and PyTorch model inference engine
├── classify_images.py           # Compares true pet labels with model predictions
├── get_input_args.py            # CLI argument parsing using argparse (--dir, --arch, --dogfile)
├── get_pet_labels.py            # Formats and cleans ground-truth labels from filenames
├── adjust_results4_isadog.py    # Classifies whether prediction is a dog using dognames.txt
├── calculates_results_stats.py  # Computes accuracy, breed precision, and error statistics
├── print_results.py             # Formats and displays summary tables and misclassifications
├── dognames.txt                 # Lookup table of valid ImageNet dog breeds (221 classes)
├── imagenet1000_clsid_to_human.txt # ImageNet 1,000-class index-to-label mapping dictionary
├── pet_images/                  # Curated benchmark dataset of test images
├── run_models_batch.sh          # Batch benchmark script for Linux/macOS
├── run_models_batch.bat         # Batch benchmark script for Windows
├── requirements.txt             # Project dependencies
├── .gitignore                   # Git ignore rules for cache & environments
└── README.md                    # Project documentation
```

---

## 🛠️ Quickstart & Reproduction

### 1. Clone the Repository
```bash
git clone https://github.com/prateek-kalwar-95/Dog-Breed-Image-Classifier-CNN.git
cd Dog-Breed-Image-Classifier-CNN
```

### 2. Environment Setup
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# Install dependencies:
pip install -r requirements.txt
```

### 3. Run Inference on a Model Architecture
Run inference with the model of your choice (`vgg`, `resnet`, or `alexnet`):

```bash
# Evaluate using ResNet:
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt

# Evaluate using VGG:
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt

# Evaluate using AlexNet:
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt
```

### 4. Run Batch Benchmark (All 3 Architectures)
```bash
# On Windows:
run_models_batch.bat

# On Linux / macOS:
chmod +x run_models_batch.sh
./run_models_batch.sh
```

---

## 👨‍💻 Author
**Prateek Kalwar**  
- **GitHub:** [@prateek-kalwar-95](https://github.com/prateek-kalwar-95)  
- Completed as part of the **Udacity AI Programming with Python Nanodegree**.

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
