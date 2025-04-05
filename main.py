from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

app = FastAPI()

# Enable CORS so frontend (on a different port or domain) can access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    print(f"📁 Received file: {file.filename}")

    # Save the uploaded file temporarily (optional but good for real model use)
    temp_dir = "temp_uploads"
    os.makedirs(temp_dir, exist_ok=True)
    file_path = os.path.join(temp_dir, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # TODO: Replace the below line with your actual deepfake detection model
    result = "real"  # or "fake" depending on your model output

    print(f"✅ Prediction result: {result}")

    return {"result": result}
