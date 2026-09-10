import cv2
import pytesseract
from pytesseract import Output


# Read input image
image = cv2.imread("input.jpg")

if image is None:
    print("Input image not found.")
    exit()


# Make the image bigger
image = cv2.resize(
    image,
    None,
    fx=2,
    fy=2,
    interpolation=cv2.INTER_CUBIC
)


# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Remove small noise
blur = cv2.GaussianBlur(gray, (3, 3), 0)


# Create different versions for OCR
otsu = cv2.threshold(
    blur,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)[1]

adaptive = cv2.adaptiveThreshold(
    blur,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    31,
    11
)


# Store preprocessing results
images = {
    "Grayscale": gray,
    "Otsu Threshold": otsu,
    "Adaptive Threshold": adaptive
}


best_image = None
best_text = ""
best_confidence = 0
best_method = ""


# Test each preprocessing method
for method, processed in images.items():

    config = "--psm 6"

    text = pytesseract.image_to_string(
        processed,
        config=config
    )

    data = pytesseract.image_to_data(
        processed,
        config=config,
        output_type=Output.DICT
    )

    confidences = []

    for value in data["conf"]:
        try:
            confidence = float(value)

            if confidence >= 0:
                confidences.append(confidence)

        except ValueError:
            pass


    if confidences:
        average_confidence = sum(confidences) / len(confidences)
    else:
        average_confidence = 0


    print(
        f"{method}: {average_confidence:.2f}% confidence"
    )


    # Keep the best result
    if average_confidence > best_confidence:
        best_confidence = average_confidence
        best_text = text
        best_image = processed
        best_method = method


print("\nImage Recognition")
print("-----------------")

print("Pre-processing completed.")
print("Image Scaling: Done")
print("Grayscale: Done")
print("Gaussian Blur: Done")
print("Otsu Thresholding: Done")
print("Adaptive Thresholding: Done")

print("\nBest Pre-processing Method")
print("--------------------------")
print(best_method)

print("\nRecognized Text")
print("---------------")

if best_text.strip():
    print(best_text.strip())
else:
    print("No text was detected.")


print("\nAverage Confidence:",
      round(best_confidence, 2), "%")


# Check the 80% validation requirement
if best_confidence >= 80:
    print("Validation: PASSED")
    print("Confidence is above the 80% threshold.")
else:
    print("Validation: FAILED")
    print("Confidence is below the 80% threshold.")


# Save the best processed image
cv2.imwrite("output.jpg", best_image)

print("\nProcessed image saved as output.jpg")
