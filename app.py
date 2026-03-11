import streamlit as st
from PIL import Image
import random

st.title("AI Fashion Assistant 👗")

st.write("Upload a photo and get fashion suggestions.")

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
"Matte finish",
"Soft glam",
"Bold lipstick look",
"Minimal clean makeup"
]

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Photo", use_column_width=True)

    if st.button("Generate Style"):
        st.subheader("AI Suggestions")

        st.write("Hairstyle:", random.choice(hairstyles))
        st.write("Outfit:", random.choice(outfits))
        st.write("Makeup:", random.choice(makeup))
