import os
from flask import Flask, request
from deepface import DeepFace
from PIL import Image, ImageOps
from io import BytesIO
from time import time_ns

app = Flask(__name__)

backends = ["opencv", "ssd", "dlib", "mtcnn", "retinaface"]
models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib", "SFace"]
metrics = ["cosine", "euclidean", "euclidean_l2"]


def preprocess(image: Image):
    # convert to gray scale and apply histogram equalization of the image
    return ImageOps.equalize(image.convert("L"), None)


@app.route('/recognize', methods=['POST'])
def face_recognition():
    print('request accepted')
    image = Image.open(BytesIO(request.data))  # decode the bytestream into image
    image = preprocess(image)  # preprocess the image
    path = f'{time_ns()}.jpg'  # compose unique filename
    image.save(path, 'JPEG')  # save the image file
    try:
        people = DeepFace.find(img_path=path, db_path="Data/", model_name=models[2], distance_metric=metrics[1],
                               enforce_detection=False)
        person = people[0]['identity'][0].split('/')[1]
        print(person)
        return person
    except Exception as e:
        print(e)
        return ""
    finally:
        os.remove(path)


if __name__ == '__main__':
    app.run()
