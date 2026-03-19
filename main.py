import cv2
from config import KNOWN_DIR
from core.loader import load_known_faces
from core.recognizer import recognize_face
from core.saver import save_unknown_face
from camera.stream import open_camera, read_frame, close_camera
from ui.render import render_frame
import face_recognition


def main():
    known_faces = load_known_faces(KNOWN_DIR)
    capture = open_camera()

    if capture is None:
        return

    while True:
        frame, resized_rgb = read_frame(capture)

        if frame is None:
            break

        face_locations = face_recognition.face_locations(resized_rgb)
        face_encodings = face_recognition.face_encodings(resized_rgb, face_locations)

        results = []

        for face_encoding in face_encodings:
            name, distance, confidence = recognize_face(face_encoding, known_faces)
            results.append((name, distance, confidence))

        frame = render_frame(frame, face_locations, results)

        for i in range(len(results)):
            name, distance, confidence = results[i]
            top, right, bottom, left   = face_locations[i]

            if name == "Unknown":
                scale = int(1 / 0.25)
                save_unknown_face(frame, top * scale, right * scale, bottom * scale, left * scale)

        cv2.imshow("Face Recognition (Press A to Exit)", frame)

        if cv2.waitKey(10) == ord("a"):
            break

    close_camera(capture)


if __name__ == "__main__":
    main()
