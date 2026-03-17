import os

## directories for images
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
KNOWN_DIR = os.path.join(PROJECT_DIR, "known_faces")
UNKNOWN_DIR = os.path.join(PROJECT_DIR, "unknown_faces")

## settings
# face distance threshold setting
THRESHOLD = 0.50
# seconds for saving an unknown faces
COOLDOWN_SEC = 3

# confidence bands based on distance
CONFIDENCE_BANDS = {
    'high': (0.0, 0.35),
    'medium': (0.35, 0.50),
    'low': (0.50, 0.65)
}

## camera settigns
CAMERA_INDEX = 0
FRAME_SCALE = 0.25

### ui settings
COLORS = {
    'known': (0, 255, 0),
    'low': (0, 255, 255),
    'unknown': (0, 0, 255),
}
FONT = 1
FONT_SCALE = 0.7
FONT_THICK = 2
