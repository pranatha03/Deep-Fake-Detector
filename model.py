import cv2
from PIL import Image
import torch
import torchvision.transforms as transforms

def extract_first_frame(video_path):
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        raise ValueError("Could not read frame from video")

    # Convert BGR (OpenCV) to RGB (PIL)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(frame)
    return image

def predict(video_path):
    # Step 1: Extract the first frame from the video
    image = extract_first_frame(video_path)

    # Step 2: Transform for model input
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])
    image_tensor = transform(image).unsqueeze(0)

    # Step 3: Dummy prediction (replace with your model inference)
    # result = model(image_tensor)
    return {"prediction": "real"}  # placeholder result
