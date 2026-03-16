import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

st.title("AI Fashion & Hairstyle Assistant")

st.write("Upload a photo or take a picture to get hairstyle suggestions.")

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Upload option
uploaded_file = st.file_uploader("Upload a photo", type=["jpg", "png", "jpeg"])

# Camera option
camera_photo = st.camera_input("Or take a photo")

image = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)

elif camera_photo is not None:
    image = Image.open(camera_photo)

if image is not None:

    img = np.array(image)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:

        st.success("You looks amazing!")

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)

        st.image(img, channels="BGR")

        st.subheader("Recommended Hairstyles")

        hairstyles = [
            "Low Fade",
            "Buzz Cut",
            "Textured Crop",
            "Curly Top Fade",
            "Classic Taper"
        ]

        for style in hairstyles:
            st.write("•", style)

        st.subheader("Recommended Outfit")
        st.write("• Casual V-neck outfit")

        # Convert image for download
        result = Image.fromarray(img)
        buf = io.BytesIO()
        result.save(buf, format="PNG")

        st.download_button(
            label="Download Styled Image",
            data=buf.getvalue(),
            file_name="styled_photo.png",
            mime="image/png"
        )

    else:

        st.error("No face detected. Try another photo.")
