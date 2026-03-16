import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("AI Fashion & Hairstyle Assistant")

st.write("Take a photo and get hairstyle suggestions.")

# OpenCV face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Camera input
img_file = st.camera_input("Take Photo")

if img_file is not None:

    # Convert image
    image = Image.open(img_file)
    img = np.array(image)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        st.success("Face detected!")

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        st.image(img, channels="BGR")

        st.subheader("Recommended Hairstyles")

        st.write("• Low fade")
        st.write("• Textured crop")
        st.write("• Buzz cut")
        st.write("• Curly top fade")

    else:
        st.error("IT'S LIKE YOU ARE UGLY. Please try again.")
