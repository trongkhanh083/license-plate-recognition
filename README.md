
# 🚗 License Plate Recognition

A Python-based License Plate Recognition system that detects and extracts license plate text from vehicle images using OpenCV for image processing and Tesseract OCR for text recognition.

---

## 🚀 Features

- Image Upload – Upload vehicle images (JPG, PNG, JPEG)
- License Plate Detection – Locates license plates using contour detection
- OCR Text Recognition – Extracts text using Tesseract OCR
- Real-Time Processing – Fast detection and recognition

## ⚙️ Installation
- Python 3.10+
   ```bash
   git clone https://github.com/trongkhanh083/license-plate-recognition.git
   cd license-plate-recognition
   pip install -r requirements.txt
   sudo apt install tesseract-ocr
   ```
   
## 🧠 Usage
  ```bash
  ./scripts/run_training.sh
  ```

### 🖼️ Web Interface
```bash
streamlit run streamlit_app.py
```
