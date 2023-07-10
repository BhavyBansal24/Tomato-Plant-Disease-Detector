# Tomato-Plant-Disease-Detector

![](https://github.com/BhavyBansal24/Tomato-Plant-Disease-Detector/blob/master/extras/dataset.jpg?raw=true)

### Project is live at : [Tomato-Plant-Disease-Detector](https://bhavybansal24-tomato-plant-disease-detector-app-jo66w9.streamlitapp.com/)

## Quick Offline Setup :

- method 1 (using Docker)
- Open cmd in local and run all below commands..

  ```
  git clone https://github.com/BhavyBansal24/Tomato-Plant-Disease-Detector.git
  docker build -t tomato_app .
  docker run -dp 8501:8501 --name Tomantina tomato_app
  timeout 2 /nobreak && start http://localhost:8501

  ```

- Method 2 : (using Conda venv)
- Clone this repo
- Open cmd in Clone folder
- Create a conda environment on your device using commands below on cmd,
  ```
  conda create -n test_env python=3.9
  conda activate test_env
  ```
- Install require libraries
  ```
  pip install requirements.txt
  ```
- Run the application
  ```
  streamlit run app.py
  ```

## How to use Tomato-Plant-Disease-Detector web-app:

- Click [here](https://bhavybansal24-tomato-plant-disease-detector-app-jo66w9.streamlitapp.com/)
- Select type of Input ['Upload Image', 'Take A Shot', 'Live Camera (Experimental)']
  ![](https://github.com/BhavyBansal24/Tomato-Plant-Disease-Detector/blob/master/extras/selectType.jpeg?raw=true)

## Upload Image

- Click on Browse files & Upload a Image file, Model will classify your uploaded Image from the known tomato disease classes.
  ![](https://github.com/BhavyBansal24/Tomato-Plant-Disease-Detector/blob/master/extras/UploadIMG.jpeg?raw=true)
- After uploading completes, you can see the prediction on right side as shown below
  ![](https://github.com/BhavyBansal24/Tomato-Plant-Disease-Detector/blob/master/extras/predictionIMG.jpeg?raw=true)

---

## Take A Shot

- Take a shot of the tomato plant leaf by clicking **Take Photo** on right side of the application.

---

## Live Camera (Experimental)

- As of now Streamlit is not supporting to use camera directly from API.
- Here is an way to access the Live Camera feature on your offline device :
  - Clone this repo
  - Open cmd in Clone folder
  - Create a conda environment on your device using commands below on cmd,
  ```
  conda create -n test_env python=3.9
  conda activate test_env
  pip install requirements.txt
  streamlit run app.py
  ```
  - Note : you may be asked for Email to start streamlit (proceed anyways)
  - It will redirect you to your default browser and open application offline
  - here you may use the Live Camera (Experimental) feature without any error.

---

## Model Details :

- Sequential model
  ![](https://github.com/BhavyBansal24/Tomato-Plant-Disease-Detector/blob/master/extras/model.jpeg?raw=true)
- Training of 10 Epoch
  ![](https://github.com/BhavyBansal24/Tomato-Plant-Disease-Detector/blob/master/extras/training.jpeg?raw=true)

---

## Model Results :

- Model Accuracy and Loss
  - ![](https://github.com/BhavyBansal24/Tomato-Plant-Disease-Detector/blob/master/extras/Accuracy&Loss.png?raw=true)

---

## Model Evaluation

- Classification Report
  - ![](https://github.com/BhavyBansal24/Tomato-Plant-Disease-Detector/blob/master/extras/ClassificationReport.jpeg?raw=true)
- Confusion Matrix
  - ![](https://github.com/BhavyBansal24/Tomato-Plant-Disease-Detector/blob/master/extras/ConfusionMatrix.png?raw=true)

---

## Dataset used for Training model:

- Dataset is taken from kaggle and link for dataset is [here](https://www.kaggle.com/datasets/asheniranga/leaf-disease-dataset-combination)
- This dataset contains images of 256 X 256 size & RGB colored of different plant species.
- For this project I have choosen tomoto plant with 10 classes of diseases namely :
  - Bacterial Spot
  - Early Blight
  - Healthy
  - Late Blight
  - Leaf Mold
  - Septoria Leaf Spot
  - Spider Mites Two-Spotted Spider Mite
  - Target Spot
  - Tomato Mosaic Virus
  - Tomato Yellow Leaf Curl Virus

---

## Libraries and framework used in project :

- [Pandas](https://pandas.pydata.org/)
- [Numpy](https://numpy.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Sklearn](https://scikit-learn.org/stable/)
- [Matplotlib](https://matplotlib.org/)
- [streamlit](https://streamlit.io/)
- [Tensorflow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)
- [OpenCV](https://opencv.org/)

---

## Do check my Kaggle (ipynb)Notebook:

- Link to my kaggle notebook is [here](https://www.kaggle.com/code/bhavybansal/cnn-plant-village-multi-models-with-deployment)
- Do upvote my notebook, Hope you like it.
- and do Not forgot to check my other notebooks on kaggle as well

---

### Do 🌟 this Github Repository, Hope you have loved my work

---

## Moreover don't forget to follow me on :

- [github](https://github.com/BhavyBansal24)
- [Kaggle](https://www.kaggle.com/bhavybansal)
- [Linkedin](https://www.linkedin.com/in/bhavybansal24/)
- [Twitter](https://twitter.com/BhavyBansal_24)
- [Instagram](https://www.instagram.com/bhavybansal_24/)

---

## Portfolio Website :

- Hope you love to know more about me, check my Portfolio Website [here](https://bhavybansal24.github.io/Neural-Programmer/)
