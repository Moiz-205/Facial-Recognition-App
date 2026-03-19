import cv2
from config import COLORS, FONT, FONT_SCALE, FONT_THICK, FRAME_SCALE

def scale_face_location(top, right, bottom, left):
    """
    scales face coordinates back to original frame size.
    detection is perform on resized frame and render applied on original.
    """
    scale = int(1 / FRAME_SCALE)

    top = top * scale
    right = right * scale
    bottom = bottom * scale
    left = left * bottom

    return top, right, bottom, left

def get_box_color(confidence):
    """
    returns colored box based on confidence level.
    """
    if confidence == 'high' or confidence == 'medium':
        return COLORS['known']
    elif confidence == 'low':
        return COLORS['low']
    else:
        return COLORS['unknown']

def draw_face(frame, top, right, bottom, left, name, distance, confidence):
    """
    draws a box and label on single detected face.
    """
    color = get_box_color(confidence)

    cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
    label = f'{name} ({distance:.2f})'

    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
    cv2.putText(frame, label, (left + 6, bottom - 10), FONT, FONT_SCALE, (0,0,0), FONT_THICK)

    return frame

def render_frame(frame, face_locations, results):
    """
    iterate over all detected faces and draws each one.
    """
    for i in range(len(face_locations)):
        top, right, bottom, left = face_locations[i]
        name, distance, confidence = results[i]

        top, right, bottom, left = scale_face_location(top, right, bottom, left)
        frame = draw_face(frame, top, right, bottom, left, name, distance, confidence)

    return frame
