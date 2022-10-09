import streamlit as st
import numpy as np
import helper
import cv2
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

st.sidebar.title("Tomato Plant Disease Detector")

selectbox = st.sidebar.selectbox(
    'Select the type of input', ('None','Upload Image', 'Live Camera'))

# Image Input
if selectbox == 'Upload Image':
    Uploaded_file = st.sidebar.file_uploader(
        "Insert File", type=['.jpg', '.jpeg', '.png'])
    if Uploaded_file is not None:
        file_bytes = np.asarray(
            bytearray(Uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = helper.preprocess(frame)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        # prediction
        output = helper.prediction(frame)
        str_out = 'prediction : ' + str(output[0])
        st.success(str_out)

# CAMERA Input
if selectbox == 'Live Camera':
    Start_camera = st.sidebar.checkbox("Start Camera")

    if Start_camera is True:
        st.title("Start Camera")
        FRAME_WINDOW = st.image([])
        FRAME_WINDOW1 = st.success(["Starting Video"])
        camera = cv2.VideoCapture(0)
        while True:
            _, frame = camera.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            FRAME_WINDOW.image(frame)
            # prediction
            output = helper.prediction(frame)
            str_out = 'prediction : ' + str(output[0])
            FRAME_WINDOW1.success(str_out)
