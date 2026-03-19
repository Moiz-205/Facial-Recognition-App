import os
import time
import cv2
from datetime import datetime
from config import UNKNOWN_DIR, COOLDOWN_SEC

last_saved = 0  # runtime cooldown variable

def save_unknown_face(frame, top, right, bottom, left):
    """
    saves a cropped unknown face from the frame if cooldown has passed.
    """
    global last_saved

    now = time.time()
    time_diff = now - last_saved

    if time_diff < COOLDOWN_SEC:
        return

    crop = frame[top:bottom, left:right]

    if crop.size == 0:
        return

    time_string = datetime.now().strftime('%Y%m%d_%H%M%S')
    save_path = os.path.join(UNKNOWN_DIR, f'unknown_{time_string}.jpg')

    cv2.imwrite(save_path, crop)
    print(f'Unknown face image saved to {save_path}')

    last_saved = now
