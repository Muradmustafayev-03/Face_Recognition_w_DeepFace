from deepface import DeepFace
import json

backends = ["opencv", "ssd", "dlib", "mtcnn", "retinaface"]
models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib", "SFace"]
metrics = ["cosine", "euclidean", "euclidean_l2"]


def face_recognition(img):
    # Perform face recognition on the provided image
    # Find faces and identify people using a specific model and distance metric
    people = DeepFace.find(img_path=img, db_path="Data/", model_name=models[2], distance_metric=metrics[1])
    # as the function is designed to accept cropped images of a single face,
    # there will be only 1 person recognized
    person = people[0]['identity'][0].split('/')[1]
    return json.dumps(person)
