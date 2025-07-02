from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware  # ← add this
from PIL import Image
import pytesseract
import io
import cv2
import numpy as np

# Set path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

app = FastAPI()

# ← Add this block to allow requests from your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # you can lock this down to ["http://localhost:5500"] later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))

        gray = image.convert("L")
        image_np = np.array(gray)
        if np.mean(image_np) < 127:
            image_np = cv2.bitwise_not(image_np)
        _, thresh = cv2.threshold(image_np, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(thresh, config=custom_config)

        if not text.strip():
            return JSONResponse({"error": "No text found"}, status_code=400)
        return JSONResponse({"text": text})

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
