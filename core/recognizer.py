import os
from deepface import DeepFace
from config import KNOWN_DIR, THRESHOLD, CONFIDENCE_BANDS
from config import DEEPFACE_MODEL, DEEPFACE_DETECTOR, DEEPFACE_DISTANCE

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

def recognize_face(frame):
    """
    captures a frame and checks against all known_faces directory.
    returns either (name, distance) if face is found.
    or ('unknown', None) if no face is found.
    """
    try:
        results = DeepFace.find(
            img_path=frame,
            db_path=KNOWN_DIR,
            model_name=DEEPFACE_MODEL,
            detector_backend=DEEPFACE_DETECTOR,
            distance_metric=DEEPFACE_DISTANCE,
            enforce_detection=False,
            silent=True
        )

        if not results or len(results[0]) == 0:
            return 'Unknown', None

        best_match = results[0].iloc[0]     # type: ignore
        distance = float(best_match[f'{DEEPFACE_MODEL}_{DEEPFACE_DISTANCE}'])

        if distance > THRESHOLD:
            return 'Unknown', distance

        name = os.path.splitext(os.path.basename(best_match['identity']))[0]
        return name, distance

    except Exception as e:
        print(f'Recognition failed: {e}')
        return 'Unknown', None
