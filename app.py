import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("AI Hairstyle & Fashion Assistant")

uploaded_file = st.file_uploader("Upload your photo", type=["jpg","png","jpeg"])

def detect_face_shape(w,h):

    ratio = w/h

    if 0.95 <= ratio <= 1.05:
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
        scaleFactor=1.2,
        minNeighbors=8,
        minSize=(100,100)
    )

    if len(faces) > 1:
        faces = faces[:1]

    for (x,y,w,h) in faces:

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        face_shape = detect_face_shape(w,h)

        st.image(img, caption="Detected Face", use_column_width=True)

        st.subheader("Face Shape")
        st.write(face_shape)

        st.subheader("Recommended Hairstyle")

        if face_shape == "Round":

            st.image("https://i.imgur.com/8zQZ4qX.jpg", caption="Textured Fade")
            st.write("Outfit: Streetwear Jacket")

        elif face_shape == "Square":

            st.image("https://i.imgur.com/BK9XK6p.jpg", caption="Curly Top Fade")
            st.write("Outfit: Smart Casual Blazer")

        else:

            st.image("https://i.imgur.com/2DhmtJ4.jpg", caption="Classic Side Part")
            st.write("Outfit: Casual V-Neck Outfit")
