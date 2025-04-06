from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import predict_deepfake_image, predict_deepfake_video
import os

app = FastAPI()

# Allow frontend to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Deepfake Detection API is running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        file_bytes = await file.read()
        ext = os.path.splitext(file.filename)[1].lower()

        if ext in [".jpg", ".jpeg", ".png"]:
            label, confidence = predict_deepfake_image(file_bytes)
        elif ext in [".mp4", ".avi", ".mov", ".webm"]:
            label, confidence = predict_deepfake_video(file_bytes)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file format")

        return {
            "label": label,
            "confidence": round(confidence * 100, 2)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
# main.py
from fastapi import FastAPI, UploadFile, File
from model import predict_deepfake_image
import traceback

app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        file_bytes = await file.read()
        label, confidence = predict_deepfake_image(file_bytes, file.filename)
        return {"label": label, "confidence": confidence}
    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}
