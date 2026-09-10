<div align="center">

# 🖼️ DecodeLabs AI Project 4 — Image Recognition

### Text Recognition (OCR) & Object Detection using OpenCV, Tesseract & MobileNet-SSD

![Python](https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-DNN%20%26%20Vision-5C3EE8?logo=opencv&logoColor=white)
![Tesseract](https://img.shields.io/badge/Tesseract-OCR-yellowgreen)
![MobileNet--SSD](https://img.shields.io/badge/Model-MobileNet--SSD-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

_Developed as part of the DecodeLabs Artificial Intelligence Industrial Training Program_

</div>

---

## 📌 Project Overview

This project is a **basic image recognition system** that demonstrates two common computer vision tasks:

- 🔤 **Text Recognition** using Tesseract OCR
- 🎯 **Object Detection** using a pre-trained MobileNet-SSD model

The system processes sample images, recognizes text or objects, calculates confidence scores, and displays the results clearly.

---

## ✨ Features

| Category                | Capabilities                                                                  |
| ----------------------- | ----------------------------------------------------------------------------- |
| 🖼️ **Image Processing** | Processes input images using OpenCV                                           |
| 🧪 **Preprocessing**    | Grayscale conversion, Gaussian blur, Otsu thresholding, Adaptive thresholding |
| 🔤 **OCR**              | Extracts text using Tesseract OCR, calculates OCR confidence scores           |
| 🎯 **Object Detection** | Detects objects using MobileNet-SSD with an **80% confidence threshold**      |
| 📦 **Visualization**    | Draws bounding boxes, displays labels & confidence scores                     |
| 💾 **Output**           | Saves processed output images                                                 |

---

## 🔤 Part 1 — Text Recognition (OCR)

The OCR component uses **Tesseract OCR** through the **Pytesseract** library.

The input image is an **invoice** containing information such as company details, invoice number, customer information, products, prices, and total amount.

The image is resized and processed using different preprocessing techniques before being passed to Tesseract OCR. The preprocessing methods tested include:

- 🔲 Grayscale Conversion
- 🌫️ Gaussian Blur
- ⚫ Otsu Thresholding
- 🔳 Adaptive Thresholding

The system compares the confidence scores from the different preprocessing methods and **automatically selects the method with the highest confidence**.

### 📊 OCR Result

| Metric                           | Value         |
| -------------------------------- | ------------- |
| 🏆 Best Preprocessing Method     | **Grayscale** |
| 📈 Average OCR Confidence        | **92.61%**    |
| 🎯 Required Confidence Threshold | 80%           |
| ✅ Validation Result             | **PASSED**    |

> The system successfully recognized the main text from the invoice image.

---

## 🎯 Part 2 — Object Detection

The object detection component uses a **pre-trained MobileNet-SSD model** with OpenCV's **DNN module**.

The model processes an input image and identifies objects along with their confidence scores. Only detections with a confidence score of **80% or higher** are accepted, and detected objects are displayed using bounding boxes and labels.

### 📊 Object Detection Result

| #   | Object    | Confidence | Status    |
| --- | --------- | ---------- | --------- |
| 1   | 🧍 Person | 99.99%     | ✅ Passed |
| 2   | 🚗 Car    | 99.99%     | ✅ Passed |

**Total detected objects: 2**

> Both detections passed the required 80% confidence threshold.

---

## 🧠 Concepts Used

`Image Recognition` · `Optical Character Recognition` · `Image Preprocessing` · `Grayscale Conversion` · `Gaussian Blur` · `Otsu Thresholding` · `Adaptive Thresholding` · `OCR Confidence Scoring` · `Object Detection` · `Bounding Boxes` · `Confidence Thresholding` · `Pre-trained Models` · `MobileNet-SSD` · `OpenCV DNN`

---

## 🛠️ Technologies Used

<div align="center">

![Python](https://img.shields.io/badge/-Python%203-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/-OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Pytesseract](https://img.shields.io/badge/-Pytesseract-yellowgreen?style=for-the-badge)
![Tesseract OCR](https://img.shields.io/badge/-Tesseract%20OCR-43853D?style=for-the-badge)
![MobileNet-SSD](https://img.shields.io/badge/-MobileNet--SSD-orange?style=for-the-badge)
![Pillow](https://img.shields.io/badge/-Pillow-blueviolet?style=for-the-badge)
![VS Code](https://img.shields.io/badge/-VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

</div>

---

## 📁 Project Structure

```text
AI_Project_4/
│
├── models/
│   ├── deploy.prototxt
│   └── mobilenet_iter_73000.caffemodel
│
├── Screenshots/
│   ├── output1.png
│   ├── output2.png
│   └── output3.png
│
├── input.jpg
├── objects.jpg
├── output.jpg
├── detection_output.jpg
├── recognition.py
├── object_detection.py
├── requirements.txt
└── README.md
```

---

## 👤 Author

**Muhammad Hamza**
Software Engineering Student · Iqra University

[![GitHub](https://img.shields.io/badge/GitHub-mhamza2004-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mhamza2004)

---

## 🖼️ Output Screenshots

### 🔤 OCR Result

![OCR Result](Screenshots/output1.png)

### 🎯 Object Detection Terminal Output

![Object Detection Terminal Output](Screenshots/output2.png)

### 📦 Object Detection Result

![Object Detection Result](Screenshots/output3.png)

---

<div align="center">

⭐ _Part of the DecodeLabs AI Industrial Training Program_ ⭐

</div>
