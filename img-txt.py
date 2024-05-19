import streamlit as st
import cv2
import pytesseract
import numpy as np



def perform_ocr(image):

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray_image)
    return text


def main():
    st.title("OCR with Tesseract")


    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:

        image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        st.write("")

        text = perform_ocr(image)


        st.header("Extracted Text:")
        st.write(text)


if __name__ == "__main__":
    main()
