import face_recognition
import numpy as np

known_face_encodings = []
known_face_names = []

# Register endpoint
def register_face(image_path, name):
    # Load the image and find the face locations
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)

    # If no faces found in the image, return error
    if len(face_locations) == 0:
        return "No faces found in the image"

    # Encode the face and append it to the list of known face encodings
    face_encoding = face_recognition.face_encodings(image, face_locations)[0]
    known_face_encodings.append(face_encoding)
    known_face_names.append(name)

    return "Face registered successfully"


# Recognize endpoint
def recognize_face(image_path):
    # Load the image and find the face locations
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)

    # If no faces found in the image, return error
    if len(face_locations) == 0:
        return "No faces found in the image"

    # Encode the face and compare it to the known face encodings
    face_encoding = face_recognition.face_encodings(image, face_locations)[0]
    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)

    # If the distance is too high, return unknown
    if face_distances[best_match_index] > 0.6:
        return "Unknown"

    # Otherwise, return the name of the best match
    return known_face_names[best_match_index]
