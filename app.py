import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("AI Fashion & Hairstyle Assistant")

st.write("Upload your photo and AI will analyze your face shape.")

uploaded_file = st.file_uploader("Upload your photo", type=["jpg","png","jpeg"])

def detect_face_shape(w,h):

    ratio = w/h

    if ratio > 0.95 and ratio < 1.05:
        return "Round"

    elif ratio > 1.05:
        return "Square"

    else:
        return "Oval"

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    img = np.array(image)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(30,30)
    )

    for (x,y,w,h) in faces:

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        shape = detect_face_shape(w,h)

        cv2.putText(
            img,
            shape,
            (x,y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255,0,0),
            2
        )

        st.image(img, caption="AI Face Detection", use_column_width=True)

        st.subheader("AI Analysis")

        st.write("Detected Face Shape:", shape)

        if shape == "Round":

            st.write("Recommended Hairstyle: Textured Fade")
            st.write("Recommended Outfit: Streetwear Jacket")

        elif shape == "Square":

            st.write("Recommended Hairstyle: Curly Top Fade")
            st.write("Recommended Outfit: Smart Casual Blazer")

        else:

            st.write("Recommended Hairstyle: Classic Side Part")
            st.write("Recommended Outfit: Casual V-Neck Outfit")
