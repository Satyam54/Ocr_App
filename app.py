import streamlit as st
import pytesseract
import cv2
from PIL import Image

st.title("Optical Character Recognition (OCR)")
st.text("Upload an image to extract text!")
uploaded_file= st.file_uploader("Choose an image",type=["png","jpg","jpeg"])
if uploaded_file is not None:
  img= Image.open(uploaded_file)
  st.image(img,caption="Uploaded Image", use_column_width = True)
  st.write("")

  if st.button('PREDICT:'):
    st.write("RESULT:")
    output=pytesseract.image_to_string(img)
    st.write(output)
