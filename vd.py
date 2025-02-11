import cv2
import os
from ultralytics import YOLO

# Load YOLOv5 model (use 'yolov5su.pt' for improved accuracy)
model = YOLO("yolov5su.pt")

# Input and output paths
inputPath = os.getcwd() + "/test_images/"
outputPath = os.getcwd() + "/output_images/"
os.makedirs(outputPath, exist_ok=True)

# Process all images in the input folder
for filename in os.listdir(inputPath):
    if filename.endswith((".png", ".jpg", ".jpeg")):
        img_path = os.path.join(inputPath, filename)
        
        # Perform detection and save output
        results = model.predict(img_path, save=True, project=outputPath, name="",exist_ok=True)
        print(f"Processed: {filename}")

print("Detection completed!")
