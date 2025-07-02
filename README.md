# Handwritten-Character-recognitio

This web application allows users to upload images of handwritten text and extracts the text using Optical Character Recognition (OCR) powered by Tesseract. Built with a FastAPI backend and a modern HTML/CSS/JavaScript frontend, it supports image preprocessing for better accuracy and offers a simple, clean user experience.

---

## 📌 Features

- Upload any handwritten image
- Automatic preprocessing (grayscale, inversion, thresholding)
- Text extraction using Tesseract OCR
- Copy or download extracted text
- Clean and attractive UI
- Toggle button & responsive layout

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript (Vanilla)
- **Backend:** FastAPI (Python)
- **OCR Engine:** Tesseract
- **Image Processing:** OpenCV, Pillow (PIL)

---

## 🚀 How It Works

1. **User uploads an image** via the browser.
2. **Frontend sends** the image to FastAPI backend.
3. **Backend processes** the image:
   - Converts to grayscale
   - Inverts (if dark background)
   - Applies thresholding
4. **Tesseract OCR** extracts the text.
5. **Frontend displays** the text with copy & download options.

---

## 🧪 Installation & Run

### 1. Clone this repository

```bash
git clone https://github.com/your-username/handwritten-text-recognition.git
cd handwritten-text-recognition
