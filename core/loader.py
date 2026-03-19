import os
import face_recognition
from config import KNOWN_DIR, VALID_EXTENSIONS

def load_known_faces(known_dir=KNOWN_DIR):
    """
    loads and encodes known face images from known_faces directory.
    return a dict known_faces = {name: enconding}
    """
    known_faces = {}

    files = os.listdir(known_dir)

    for file_name in files:
        if not file_name.lower().endswith(VALID_EXTENSIONS):
            # print(f'No images found in {known_dir}.')
            continue
        path = os.path.join(known_dir, file_name)
        name = os.path.splitext(file_name)[0]
        image = face_recognition.load_image_file(path)
        encodings = face_recognition.face_encodings(image)

        if not encodings:
            print(f'No face found in {file_name}.')
            continue

        known_faces[name] = encodings[0]
        print(f'Encodings loaded: {name}')

    return known_faces
