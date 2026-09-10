# AI Project 4 - Image Recognition

A basic image recognition project built with Python. This project demonstrates two common computer vision tasks:

1. Text Recognition using Tesseract OCR
2. Object Detection using MobileNet-SSD

The project follows a simple recognition pipeline where an input image is processed, analyzed, and converted into useful machine-readable output.

---

## Project Overview

The goal of this project is to demonstrate how a machine can process visual data and recognize text and objects from images.

The project contains two recognition approaches:

- OCR for extracting text from an image
- Object Detection for identifying objects and drawing bounding boxes around them

An 80% confidence threshold is used for validation in the recognition pipeline.

---

## Technologies Used

- Python
- OpenCV
- Tesseract OCR
- Pytesseract
- MobileNet-SSD
- Caffe pre-trained model
- Pillow

---

## Project Structure

```text
AI_Project_4/
|
|-- models/
|   |-- deploy.prototxt
|   |-- mobilenet_iter_73000.caffemodel
|
|-- Screenshots/
|   |-- output1.png
|   |-- output2.png
|   |-- output3.png
|
|-- input.jpg
|-- objects.jpg
|-- output.jpg
|-- detection_output.jpg
|-- recognition.py
|-- object_detection.py
|-- requirements.txt
|-- README.md
```
