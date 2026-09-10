# AI Project 4 - Image Recognition

A basic image recognition project built with Python that demonstrates two common computer vision tasks:

- Optical Character Recognition (OCR)
- Object Detection using a pre-trained MobileNet-SSD model

The project processes image data and extracts readable text or identifies objects with confidence scores.

---

## Project Overview

Images contain unstructured information that cannot be directly processed like normal structured data.

This project uses computer vision techniques and pre-trained recognition tools to process images and convert visual information into useful machine-readable results.

The project contains two separate recognition pipelines:

### 1. OCR Pipeline

Uses Tesseract OCR to detect and extract text from an image.

### 2. Object Detection Pipeline

Uses OpenCV DNN and a pre-trained MobileNet-SSD model to detect objects and draw bounding boxes around them.

---

## Technologies Used

- Python
- OpenCV
- Tesseract OCR
- Pytesseract
- Pillow
- MobileNet-SSD
- Caffe Model

---

## Project Structure

```text
AI_Project_4/
|
|-- models/
|   |-- deploy.prototxt
|   `-- mobilenet_iter_73000.caffemodel
|
|-- Screenshots/
|   |-- output1.png
|   |-- output2.png
|   `-- output3.png
|
|-- input.jpg
|-- objects.jpg
|-- output.jpg
|-- detection_output.jpg
|-- recognition.py
|-- object_detection.py
|-- requirements.txt
`-- README.md
```
