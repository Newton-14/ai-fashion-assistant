import streamlit as st
import random

st.title("AI Fashion Assistant 👗")

hairstyles = [
    "Braided Hair",
    "Long Wavy Hair",
    "Curly Hair",
    "Ponytail"
]

outfits = [
    "Casual V-neck Outfit",
    "Floral Dress",
    "Street Style Outfit",
    "Elegant Evening Dress"
]

makeups = [
    "Natural Makeup",
    "Soft Glam Makeup",
    "Bold Red Lip Makeup",
    "Minimal Makeup"
]

if st.button("Generate Style"):
    st.subheader("Hairstyle")
    st.write(random.choice(hairstyles))

    st.subheader("Outfit")
    st.write(random.choice(outfits))

    st.subheader("Makeup")
    st.write(random.choice(makeups))
