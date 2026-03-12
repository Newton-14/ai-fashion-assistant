import streamlit as st
import cv2
import numpy as np
from PIL import Image
import mediapipe as mp
import requests
from io import BytesIO

st.title("AI Grooming & Fashion Assistant")

option = st.radio("Choose input method", ["Upload Photo","Use Camera"])

if option == "Upload Photo":
    uploaded_file = st.file_uploader("Upload your photo", type=["jpg","jpeg","png"])
else:
    uploaded_file = st.camera_input("Take a photo")

mp_face = mp.solutions.face_detection
face_detection = mp_face.FaceDetection(model_selection=1, min_detection_confidence=0.6)

def detect_face_shape(w,h):

    ratio = w/h

    if 0.95 <= ratio <= 1.05:
        return "Round"

    elif ratio > 1.05:
        return "Square"

    else:
        return "Oval"


def detect_gender(w,h):

    if w > h:
        return "Male"
    else:
        return "Female"


def hairstyle_urls(shape):

    if shape == "Round":
        return [
        "https://images.unsplash.com/photo-1595152772835-219674b2a8a6",
        "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d",
        "https://images.unsplash.com/photo-1520975916090-3105956dac38"
        ]

    elif shape == "Square":
        return [
        "https://images.unsplash.com/photo-1520975922327-8c4f5c1c1b3f",
        "https://images.unsplash.com/photo-1544723795-3fb6469f5b39",
        "https://images.unsplash.com/photo-1524504388940-b1c1722653e1"
        ]

    else:
        return [
        "https://images.unsplash.com/photo-1517841905240-472988babdf9",
        "https://images.unsplash.com/photo-1519699047748-de8e457a634e",
        "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e"
        ]


def load_image(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))


if uploaded_file is not None:

    image = Image.open(uploaded_file)
    img = np.array(image)

    results = face_detection.process(img)

    if not results.detections:
        st.error("No face detected")

    else:

        for detection in results.detections[:1]:

            bbox = detection.location_data.relative_bounding_box

            h_img, w_img, _ = img.shape

            x = int(bbox.xmin * w_img)
            y = int(bbox.ymin * h_img)
            w = int(bbox.width * w_img)
            h = int(bbox.height * h_img)

            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

            face_shape = detect_face_shape(w,h)
            gender = detect_gender(w,h)

            st.subheader("Detected Face")
            st.image(img, use_column_width=True)

            st.subheader("Gender Prediction")
            st.write(gender)

            st.subheader("Face Shape")
            st.write(face_shape)

            st.subheader("Generated Hairstyles")

            urls = hairstyle_urls(face_shape)

            hairstyles = []

            for url in urls:
                hair = load_image(url)
                hairstyles.append(hair)
                st.image(hair)

            st.subheader("Virtual Hairstyle Simulation")

            hair_np = cv2.resize(np.array(hairstyles[0]), (w, int(h/2)))

            y1 = max(0,y-int(h/2))
            y2 = y
            x1 = x
            x2 = x+w

            try:
                img[y1:y2,x1:x2] = hair_np
                st.image(img, caption="Styled Result", use_column_width=True)

                result = Image.fromarray(img)

                st.download_button(
                    label="Download Styled Image",
                    data=result.tobytes(),
                    file_name="ai_style.png",
                    mime="image/png"
                )

            except:
                st.write("Simulation adjustment needed")

            st.subheader("Beard Style Suggestions")

            if gender == "Male":
                st.write("• Short boxed beard")
                st.write("• Goatee")
                st.write("• Stubble")

            else:
                st.write("Beard styles not applicable")

            st.subheader("Outfit Recommendation")

            if face_shape == "Round":
                st.write("Streetwear jacket with layered hoodie")

            elif face_shape == "Square":
                st.write("Smart casual blazer")

            else:
                st.write("Minimal casual V-neck outfit")
