import os
from flask import Flask, request, jsonify
from deepface import DeepFace

app = Flask(__name__)

backends = ["opencv", "ssd", "dlib", "mtcnn", "retinaface"]
models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib", "SFace"]
metrics = ["cosine", "euclidean", "euclidean_l2"]


@app.route('/recognize', methods=['POST'])
def recognize_person():
    # Check if an image file was provided in the request
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})
    # Get the image from request
    image_file = request.files['image']
    # Return recognized face as json string
    return jsonify(face_recognition(image_file))


def face_recognition(image_file):
    # Create the temp directory if it doesn't exist
    os.makedirs('/temp/', exist_ok=True)
    # Create a path to store the image temporary
    path = os.path.join('/temp/', image_file.filename)
    # Save the image file (because the function takes the path)
    image_file.save(path)
    # Perform face recognition on the provided image
    # Find faces and identify people using a specific model and distance metric
    people = DeepFace.find(img_path=path, db_path="Data/", model_name=models[2], distance_metric=metrics[1])
    # Remove the file as it is no longer needed
    os.remove(path)
    # as the function is designed to accept cropped images of a single face,
    # there will be only 1 person recognized
    person = people[0]['identity'][0].split('/')[1]
    return person


if __name__ == '__main__':
    app.run()
