import streamlit as st
import cv2
import numpy as np
from PIL import Image
import random

st.title("AI Fashion Assistant 👗")

st.write("Upload your photo and AI will detect your face.")

uploaded_file = st.file_uploader("Upload your photo", type=["jpg","png","jpeg"])

hairstyles = [
"Curly fade",
"Buzz cut",
"Afro style",
"Short textured cut",
"Side part fade"
]

outfits = [
"Casual V-neck outfit",
"Streetwear hoodie",
"Smart casual blazer",
"Summer t-shirt and jeans",
"Sporty tracksuit"
]

makeup = [
"Natural glow",
"Soft glam",
"Matte finish",
"Bold lipstick",
"Minimal makeup"
]

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    img = np.array(image)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    st.image(img, caption="Detected Face", use_column_width=True)

    if len(faces) > 0:
        if st.button("Generate AI Style"):
            st.subheader("AI Fashion Suggestions")

            st.write("Hairstyle:", random.choice(hairstyles))
            st.write("Outfit:", random.choice(outfits))
            st.write("Makeup:", random.choice(makeup))

    else:
        st.warning("No face detected. Try another image.")
