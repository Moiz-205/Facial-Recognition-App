import os
from config import KNOWN_DIR, VALID_EXTENSIONS

def check_known_faces(known_dir=KNOWN_DIR):
    """
    checks for known_faces directory exist or not and does
    it has images or not.
    """
    if not os.path.exists(known_dir):
        print(f'Directory {known_dir} not found.')
        return False

    files = os.listdir(known_dir)
    valid = []

    for file_name in files:
        if file_name.lower().endswith(VALID_EXTENSIONS):
            valid.append(file_name)

    if not valid:
        print(f'No images found in {known_dir}')
        return False
    else:
        print(f'Found {len(valid)} known faces images: {valid}')
        return True
