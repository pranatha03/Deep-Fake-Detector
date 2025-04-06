# Deep-Fake-Detector
# 🔍 Deepfake Detector – Hackathon Project

## 🧠 Project Overview

This is a smart, AI-powered Deepfake Detector web application built as part of a hackathon challenge. It detects whether an uploaded **image** or **video** is real or fake using a **pretrained deep learning model**.

- 🔍 Supports both image & video formats
- ⚡ Fast predictions via FastAPI backend
- 🖥️ Simple & clean frontend built with HTML, CSS, and JavaScript 
- 🧠 Uses a CNN-based or transformer-based model for deepfake classification

---

## ⚙️ Tech Stack

| Frontend | Backend  | AI Model         | Deployment |
|----------|----------|------------------|------------|
| HTML/CSS or React | FastAPI  | PyTorch/TensorFlow | Render/Vercel |

---

## 🛠️ How It Works

1. User uploads an image or video.
2. File is sent to the FastAPI server.
3. The AI model processes the media and returns a prediction.
4. Frontend displays whether the input is **real or fake**.

---

## 📁 File Structure (partial)

Deep-Fake-Detector/ ├── backend/ │ ├── main.py # FastAPI app entry point │ ├── model.py # Deepfake detection logic using pretrained model │ ├── utils.py # Helper functions (e.g., preprocessing) │ └── requirements.txt # Python dependencies │ ├── frontend/ │ ├── index.html # Main web page │ ├── styles.css # Futuristic UI styling │ ├── script.js # Handles file uploads & prediction requests │ └── assets/ # Images, icons, or animations │ ├── model/ │ └── deepfake_model.pth # Pretrained PyTorch model (or .h5 for TensorFlow) │ ├── static/ # Static files served by FastAPI │ └── README.md # You're reading it!

markdown
Copy
Edit

---

## 🚀 Deployment

You can deploy this project using:

- **Render** (Backend)
- **Vercel / Netlify** (Frontend)
- Or use **Docker** for a containerized solution.

### Quick Deployment on Render (Backend)
1. Push your code to GitHub.
2. Create a new Web Service on [Render](https://render.com/).
3. Choose your repo, select Python, and set the **Start Command** as:
uvicorn backend.main:app --host 0.0.0.0 --port 8000

yaml
Copy
Edit
4. Add `requirements.txt` as your Python environment file.

### Frontend Deployment on Vercel
1. Push your `frontend` folder to a separate repo (or subfolder).
2. Deploy it using [Vercel](https://vercel.com/) with HTML/CSS config.

---
