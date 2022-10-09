import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
import numpy as np
import cv2

def preprocess(frame):
    frame = np.array(frame)
    image = cv2.resize(frame, (256, 256))
    image = image.astype('float32')
    image /= 255
    image = np.expand_dims(image, axis=0)
    return image

def prediction(frame):
    model = tf.keras.models.load_model('tomato')
    frame = cv2.resize(frame, (256, 256), interpolation= cv2.INTER_AREA)
    frame = frame.reshape(1, frame.shape[0], frame.shape[1], 3)
    prediction = model.predict(frame)
    pred = prediction.argmax()
    le.classes_ = np.load('classes.npy')
    output = le.inverse_transform([pred])
    return output