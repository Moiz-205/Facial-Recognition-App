import cv2
from config import KNOWN_DIR
from core.loader import check_known_faces
from core.recognizer import recognize_face, get_confidence
from core.saver import save_unknown_face
from camera.stream import open_camera, read_frame, close_camera
from ui.render import render_frame


def main():
    if not check_known_faces(KNOWN_DIR):
        print('No faces found in known_dir.')
        return None

    capture = open_camera()

    if capture is None:
        return None

    while True:
        frame, resized_rgb = read_frame(capture)

        if frame is None:
            break

        name, distance = recognize_face(resized_rgb)

        if distance is not None:
            confidence = get_confidence(distance)
        else:
            confidence = 'unknown'

        results = [(name, distance, confidence)]
        face_locations = []

        frame = render_frame(frame, face_locations, results)

        if name == "Unknown":
            save_unknown_face(frame=frame, top=0, right=0, bottom=0, left=0)

        cv2.imshow("Face Recognition (Press Q to Exit)", frame)

        if cv2.waitKey(10) == ord("q"):
            break

    close_camera(capture)


if __name__ == "__main__":
    main()
