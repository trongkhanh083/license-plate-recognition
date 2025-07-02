import streamlit as st
from PIL import Image
import numpy as np
import cv2
from src.plate_detection import preprocess_image, find_license_plate
from src.char_recognition import recognize_plate_text

# Page configuration
st.set_page_config(
    page_title="License Plate Recognition",
    page_icon="🚗",
    layout="wide"
)

st.title("License Plate Recognition System")
st.markdown("Upload an image of a car to detect and recognize license plate")
    
uploaded = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
if uploaded is not None:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        img = Image.open(uploaded).convert("RGB")
        img_np = np.array(img)
        st.image(img, caption="Uploaded image")
        
    raw_img, gray, edged = preprocess_image(img_np)
    plate, plate_contour = find_license_plate(gray, edged)
    text = recognize_plate_text(plate)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if plate is not None:
            st.success('Detected license plate')
            cv2.drawContours(raw_img, [plate_contour], -1, (0, 255, 0), 3)
            st.image(raw_img)
        else:
            st.warning("No license plate detected")
        
    with col2:
        if plate is not None:
            st.success('License plate')
            st.image(plate)
        else:
            st.warning("No license plate detected")

    with col3:
        if text is not None:
            st.success('Recognized text')
            st.markdown(f"### {text}")
        else:
            st.warning("No plate text recognized")
