import cv2
import numpy as np


def crop_face(img_arr):
    """Detects and crops the face from an image array."""
    img_arr = cv2.cvtColor(img_arr, cv2.COLOR_BGR2RGB)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(img_arr, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        x, y, w, h = faces[0]

        margin = 200
        x_margin = max(0, x - margin)
        y_margin = max(0, y - margin)
        w_margin = min(img_arr.shape[1], w + 2 * margin)
        h_margin = min(img_arr.shape[0], h + 2 * margin)

        cropped_face = img_arr[y_margin:y_margin + h_margin, x_margin:x_margin + w_margin]
        cropped_face = cv2.resize(cropped_face, (224, 224)) / 255.0
        return cropped_face

    return -1


def image_classifier(img_path):
    """
    Classifies an image as REAL or FAKE.
    Returns: 1 = FAKE, 0 = REAL, -1 = Error/No face found
    """
    try:
        img = cv2.imread(img_path)

        if img is None:
            print("Error: Unable to read image")
            return -1

        face = crop_face(img)

        if not isinstance(face, np.ndarray):
            print("No face detected in image")
            return -1

        # TODO: Load your trained model and run prediction here
        # Example:
        # model = load_model('model.h5')
        # face_input = np.expand_dims(face, axis=0)
        # prediction = model.predict(face_input)
        # return int(prediction[0][0] > 0.5)  # 1 = FAKE, 0 = REAL

        return 0  # Placeholder: returns REAL

    except Exception as e:
        print(f"Error in image_classifier: {e}")
        return -1


def video_classifier(video_path):
    """
    Classifies a video as REAL or FAKE by analyzing frames.
    Returns: 1 = FAKE, 0 = REAL, -1 = Error/No faces found
    """
    try:
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print("Error: Unable to open video")
            return -1

        count = 0
        fake_frame = 0
        real_frame = 0

        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            count += 1

            # Process every 3rd frame to save time
            if not count % 3 == 0:
                continue

            face = crop_face(frame)

            if not isinstance(face, np.ndarray):
                continue

            # TODO: Load your trained model and run prediction here
            # Example:
            # model = load_model('model.h5')
            # face_input = np.expand_dims(face, axis=0)
            # prediction = model.predict(face_input)
            # if prediction[0][0] > 0.5:
            #     fake_frame += 1
            # else:
            #     real_frame += 1

            real_frame += 1  # Placeholder: all frames counted as REAL

        cap.release()

        if (fake_frame + real_frame) == 0:
            return -1  # No faces detected in any frame

        # Majority vote: if more than 50% frames are fake, classify as FAKE
        if fake_frame > real_frame:
            return 1  # FAKE
        else:
            return 0  # REAL

    except Exception as e:
        print(f"Error in video_classifier: {e}")
        return -1
