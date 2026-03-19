import cv2
from config import CAMERA_INDEX, FRAME_SCALE

def open_camera():
    """
    launces camera and returns a videocapture object.
    """
    capture = cv2.VideoCapture(CAMERA_INDEX)

    if not capture.isOpened():
        print('Camera is not working.')
        return None
    else:
        print('Camera opened successfully.')
        return capture

def read_frame(capture):
    """
    read a signle frame from the camera
    returns original frame and resized rgb frame for detection.
    """
    success, frame = capture.read()

    if not success:
        print('Failure to read frame.')
        return None, None
    else:
        resized_frame = cv2.resize(frame, dsize=(0,0), fx=FRAME_SCALE, fy=FRAME_SCALE)
        resized_rgb = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)

        return frame, resized_rgb

def close_camera(capture):
    """closes camera and destroys the application window."""
    capture.release()
    cv2.destroyAllWindows()
    print('Camera closed.')
