import torch
import torch.nn as nn
from torchvision import models, transforms
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from PIL import Image
import os

# Set device (GPU or CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load model function
def load_model():
    model = models.resnet18(pretrained=True)  # Using a pretrained ResNet-18 model
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, 2)  # Modify for binary classification (real vs fake)
    model.to(device)
    model.eval()  # Set model to evaluation mode
    return model

model = load_model()

# Preprocessing transformation for the images
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])  # Adjust if needed
])

# Predict function
def predict(image_path: str):
    image = Image.open(image_path).convert("RGB")
    input_tensor = transform(image).unsqueeze(0).to(device)  # Add batch dimension
    with torch.no_grad():
        output = model(input_tensor)
        prediction = torch.argmax(output, dim=1).item()  # Get the predicted class (0 for Real, 1 for Fake)
    return prediction

# Evaluate function to calculate accuracy, F1 score, etc.
def evaluate_model(test_data_path):
    true_labels = []
    predictions = []
    test_data_path = r"C:\Users\Admin\Desktop\test_data_images"
    
    for filename in os.listdir(r"C:\Users\Admin\Desktop\test_data_images"):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Image files
            img_path = os.path.join(r"C:\Users\Admin\Desktop\test_data_images", filename)
            label = 1 if "fake" in filename else 0  # Assuming 'fake' in filename indicates deepfake
            
            true_labels.append(label)
            
            # Get model prediction
            predicted_label = predict(img_path)
            predictions.append(predicted_label)
    
    # Calculate accuracy
    accuracy = accuracy_score(true_labels, predictions)
    print(f"Accuracy: {accuracy * 100:.2f}%")
    
    # Calculate Precision, Recall, and F1 Score
    precision = precision_score(true_labels, predictions)
    recall = recall_score(true_labels, predictions)
    f1 = f1_score(true_labels, predictions)
    
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1 Score: {f1:.2f}")
    
    # Print confusion matrix
    cm = confusion_matrix(true_labels, predictions)
    print("Confusion Matrix:")
    print(cm)

# Specify your test dataset directory
test_data_path = "path_to_test_images"  # Change this to the directory containing your test images

# Call the evaluation function
evaluate_model(test_data_path)
