import numpy as np
import face_recognition
from config import THRESHOLD, CONFIDENCE_BANDS

def get_confidence(distance):
    """
    returns confidence level string based on distance bands
    high, medium, low or unknown
    """
    for level, band in CONFIDENCE_BANDS.items():
        low = band[0]
        high = band[1]

        if low <= distance and distance < high:
            return level

    return 'unknown'

def recognize_face(face_encoding, known_faces):
    """
    compares face enconding against all known faces.
    return name, distance and confidence
    """
    names = list(known_faces.keys())
    encodings = list(known_faces.values())

    distance = face_recognition.face_distance(encodings, face_encoding)
    best_index = int(np.argmin(distance))
    best_dist = float(distance[best_index])

    if best_dist < THRESHOLD:
        name = names[best_index]
    else:
        name = 'unknown'

    confidence = get_confidence(best_dist)

    return name, best_dist, confidence
