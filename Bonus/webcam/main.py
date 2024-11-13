import streamlit as st 
from PIL import Image


uploaded_image = st.file_uploader("Upload Image")
with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")
    
if camera_image:
    img = Image.open(camera_image)
    gray_img = img.convert("L")
    st.image(gray_img)

if uploaded_image:
    file = Image.open(uploaded_image)
    gray_file = file.convert("L")
    st.image(gray_file)