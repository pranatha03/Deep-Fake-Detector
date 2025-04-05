import torch
import torch.nn as nn

# Define a simple CNN model
class DummyCNN(nn.Module):
    def __init__(self):
        super(DummyCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
     
        self.fc1 = nn.Linear(16 * 64 * 64, 2)  # 2 output classes: Real vs. Fake

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = x.view(-1, 16 * 64 * 64)
        x = torch.softmax(self.fc1(x), dim=1)
        return x

# Instantiate the model
model = DummyCNN()

# Save the model's state dictionary to a file
torch.save(model.state_dict(), 'cnn_deepfake_model.pth')
print("Dummy model saved as cnn_deepfake_model.pth")
