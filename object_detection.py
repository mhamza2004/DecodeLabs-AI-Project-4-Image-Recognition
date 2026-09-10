import cv2


# Load the object detection model
model = cv2.dnn.readNet(
    "models/mobilenet_iter_73000.caffemodel",
    "models/deploy.prototxt",
    "Caffe"
)


# Object classes supported by MobileNet-SSD
classes = [
    "background", "aeroplane", "bicycle", "bird", "boat",
    "bottle", "bus", "car", "cat", "chair", "cow",
    "diningtable", "dog", "horse", "motorbike", "person",
    "pottedplant", "sheep", "sofa", "train", "tvmonitor"
]


# Read input image
image = cv2.imread("objects.jpg")

if image is None:
    print("Input image not found.")
    exit()


# Get image dimensions
height, width = image.shape[:2]


# Convert image into a blob
blob = cv2.dnn.blobFromImage(
    cv2.resize(image, (300, 300)),
    0.007843,
    (300, 300),
    127.5
)


# Run the model
model.setInput(blob)
detections = model.forward()


print("Object Detection")
print("----------------")

print("Image loaded successfully.")
print("Model loaded successfully.")
print("Confidence threshold: 80%")


# Check each detected object
detected_objects = 0

for i in range(detections.shape[2]):

    confidence = detections[0, 0, i, 2]

    # Only keep detections with 80% or higher confidence
    if confidence >= 0.80:

        class_id = int(detections[0, 0, i, 1])

        label = classes[class_id]

        # Get bounding box coordinates
        box = detections[0, 0, i, 3:7] * [
            width, height, width, height
        ]

        start_x, start_y, end_x, end_y = box.astype("int")

        # Draw bounding box
        cv2.rectangle(
            image,
            (start_x, start_y),
            (end_x, end_y),
            (0, 255, 0),
            2
        )

        # Create label
        text = f"{label}: {confidence * 100:.2f}%"

        cv2.putText(
            image,
            text,
            (start_x, start_y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

        print(
            f"{label} - {confidence * 100:.2f}% confidence"
        )

        detected_objects += 1


print("\nDetected Objects:", detected_objects)


# Save the final image
cv2.imwrite("detection_output.jpg", image)

print("Detection output saved as detection_output.jpg")
