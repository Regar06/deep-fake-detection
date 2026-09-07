# 🕵️ Deepfake Detection

A deepfake detection application that analyzes **images and videos** to identify whether the content is **REAL or FAKE**.

The project uses **FastAPI, Python, OpenCV, TensorFlow/Keras, and a CNN-based deep learning approach** for face detection and deepfake classification.

---

## 🚀 Features

* 🖼️ Image-based deepfake detection
* 🎥 Video-based deepfake detection
* 👤 Automatic face detection using OpenCV Haar Cascades
* 🧠 CNN-based deepfake classification architecture
* ⚡ FastAPI backend
* 🌐 REST API endpoints for image and video prediction
* 📦 Docker/production deployment support through Gunicorn
* 🔄 Video frame sampling for faster processing

---

## 🏗️ Project Structure

```text
deep-fake-detection/
│
├── app.py                  # FastAPI application
├── features.py             # Face detection and classification logic
├── requirements.txt        # Python dependencies
├── Procfile                # Production deployment configuration
├── runtime.txt             # Python runtime version
│
├── training.ipynb          # Model training notebook
├── test.ipynb              # Model testing/evaluation notebook
│
├── README.md
└── .gitignore
```

---

## 🧠 Deep Learning Model

The project is designed around a **10-layer Deep Convolutional Neural Network (CNN)** for binary image classification.

### Model characteristics

* Input size: **224 × 224 × 3**
* Binary classification
* Sigmoid output activation
* Dropout regularization
* Convolutional layers with 64 filters in the initial layers
* Max-pooling layers
* Dilated convolutions in the later layers
* Designed specifically for facial deepfake detection

The model is intended to classify facial images into:

| Label | Meaning                   |
| ----- | ------------------------- |
| `0`   | REAL                      |
| `1`   | FAKE                      |
| `-1`  | Error / Face not detected |

---

## 🔍 Detection Pipeline

The general processing pipeline is:

```text
          Input
            │
       ┌────┴────┐
       │          │
     Image      Video
       │          │
       │     Extract Frames
       │          │
       └────┬─────┘
            │
       Face Detection
            │
       Face Cropping
            │
       Resize to 224×224
            │
       Normalize /255
            │
       CNN Classifier
            │
       ┌────┴────┐
       │         │
     REAL       FAKE
```

For videos, the application processes **every third frame** to reduce computational cost. The final video prediction is intended to be determined using a majority vote across analyzed frames.

---

## ⚙️ Technologies Used

### Backend

* Python
* FastAPI
* Uvicorn
* Gunicorn
* OpenCV
* NumPy
* Keras / TensorFlow

### Machine Learning

* Convolutional Neural Networks
* Binary classification
* Dropout regularization
* Face detection
* Image preprocessing

### Development

* Jupyter Notebook
* `training.ipynb`
* `test.ipynb`

---

## 📋 Requirements

Before running the project, make sure you have:

* Python **3.10+**
* pip
* Git

Python 3.11 is specified in the project runtime configuration.

---

## 💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/harshpx/deepfake-detection.git
cd deepfake-detection
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the API

Start the FastAPI server with:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at:

```text
http://localhost:8000
```

FastAPI's interactive API documentation is available at:

```text
http://localhost:8000/docs
```

---

## 🔌 API Endpoints

### Health Check

```http
GET /
```

Response:

```json
"API is running"
```

---

### Image Prediction

```http
POST /predictImage
```

Upload an image using the `image` form field.

Example response:

```json
{
  "result": 0
}
```

Possible results:

```text
0  → REAL
1  → FAKE
-1 → Error / No face detected
```

---

### Video Prediction

```http
POST /predictVideo
```

Upload a video using the `video` form field.

Example response:

```json
{
  "result": 0
}
```

Possible results:

```text
0  → REAL
1  → FAKE
-1 → Error / No face detected
```

---

## 🧪 Training

The project contains a Jupyter notebook for model training:

```text
training.ipynb
```

The intended training workflow includes:

1. Load the dataset
2. Detect/crop faces
3. Resize images to `224 × 224`
4. Normalize pixel values
5. Train the CNN
6. Validate model performance
7. Evaluate using classification metrics
8. Save the trained model

Testing and evaluation can be performed using:

```text
test.ipynb
```

---

## 📊 Model Evaluation

The original project evaluates the model using metrics such as:

* Accuracy
* Precision
* Recall
* Confusion Matrix
* ROC-AUC

The reported evaluation included:

```text
True Positive  : 602
False Positive : 7
False Negative : 5
True Negative  : 586
```

> **Note:** These figures represent the reported results from the original project/training setup and should not be interpreted as guaranteed performance on new datasets.

---

## ⚠️ Current Implementation Note

The API and preprocessing pipeline are implemented, but the current `features.py` contains **placeholder model-inference code**.

For example, image classification currently returns:

```python
return 0
```

and video processing currently counts detected frames as real.

To enable actual deepfake detection, the trained Keras model needs to be loaded and used for inference.

Conceptually:

```python
model = load_model("model.h5")

face_input = np.expand_dims(face, axis=0)
prediction = model.predict(face_input)

result = int(prediction[0][0] > 0.5)
```

Therefore, before presenting this repository as a fully functional deepfake detector, make sure the trained model file is included/configured and the inference code is enabled.

---

## 🔐 Input Processing

For images and video frames:

1. OpenCV reads the input.
2. A Haar Cascade detects faces.
3. The detected face is cropped with an additional margin.
4. The face is resized to `224 × 224`.
5. Pixel values are normalized to the `[0, 1]` range.
6. The processed image is passed to the deep learning model.

---

## 🚀 Production Deployment

The repository includes a `Procfile` configured for Gunicorn:

```text
web: gunicorn -k uvicorn.workers.UvicornWorker -w 4 -b 0.0.0.0:$PORT app:app
```

The application reads the deployment port from the `PORT` environment variable.

The runtime configuration specifies:

```text
Python 3.11.0
```

---

## 📁 Dataset

The dataset is intentionally excluded from Git using:

```text
Dataset
```

in `.gitignore`.

For training, download or prepare an appropriate deepfake dataset separately and place it in the expected project structure.

---

## 🛠️ Future Improvements

Potential improvements include:

* [ ] Integrate the trained `.h5` / `.keras` model
* [ ] Add confidence scores
* [ ] Improve face detection using modern face detectors
* [ ] Support multiple faces per image
* [ ] Improve video-level aggregation
* [ ] Add authentication and rate limiting
* [ ] Add frontend interface
* [ ] Add automated tests
* [ ] Add Docker configuration
* [ ] Add CI/CD with GitHub Actions
* [ ] Add model versioning
* [ ] Improve error handling and input validation

---

## 📜 Disclaimer

This project is intended for **research and educational purposes**.

Deepfake detection models can produce false positives and false negatives. Results should not be treated as definitive proof that an image or video is authentic or manipulated.

---

## 👨‍💻 Author

**Harsh**

GitHub:
https://github.com/harshpx

---

## ⭐ Contributing

Contributions, improvements, and bug fixes are welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/your-feature
```

3. Make your changes
4. Commit your changes

```bash
git commit -m "Add your feature"
```

5. Push the branch

```bash
git push origin feature/your-feature
```

6. Open a Pull Request

---

## 📄 License

Add your preferred open-source license here, such as MIT, before publishing the repository.
