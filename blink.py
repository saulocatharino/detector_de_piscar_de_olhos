from PIL import Image, ImageDraw
import face_recognition
import cv2
import numpy as np
from scipy.spatial import distance
import os

cap = cv2.VideoCapture(0)


def tudo():

    ret, frames = cap.read()
    frame = cv2.flip( frames, 1 )
    rob_small_frame = frame[:, :, ::-1]
    face_landmarks_list = face_recognition.face_landmarks(rob_small_frame)
    for face_landmarks in face_landmarks_list:
        frame = frame[:, :, ::-1]
        pil_image = Image.fromarray(frame)
        d = ImageDraw.Draw(pil_image, 'RGBA')

        d.line(face_landmarks['chin'], fill=(150, 255, 255, 255))
        d.line(face_landmarks['nose_tip'],fill=(150, 255, 255, 255))
        d.line(face_landmarks['nose_bridge'],fill=(150, 255, 255, 255))

        d.line(face_landmarks['left_eyebrow'], fill=(150, 255, 255, 255), width=2)
        d.line(face_landmarks['right_eyebrow'], fill=(150, 255, 255, 255), width=2)


        d.line(face_landmarks['top_lip'], fill=(150, 255, 255, 255), width=2)
        d.line(face_landmarks['bottom_lip'], fill=(150, 255, 255, 255), width=2)

        d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(150, 255, 255, 255), width=2)
        d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(150, 255, 255, 255), width=2)


        bottom_right = face_landmarks['right_eye'][1][0], face_landmarks['right_eye'][1][1]
        top_right = face_landmarks['right_eye'][5][0],face_landmarks['right_eye'][5][1]
        bottom_left = face_landmarks['left_eye'][1][0], face_landmarks['left_eye'][1][1]
        top_left = face_landmarks['left_eye'][5][0],face_landmarks['left_eye'][5][1]

        blink_right = distance.euclidean(bottom_right, top_right)
        blink_left = distance.euclidean(bottom_left, top_left)

        if blink_left < 10:
            os.system("clear")
            print("Piscou olho esquerdo.")
            print()
        if blink_right < 10:
            os.system("clear")
            print("Piscou olho direito.")
            print()

        image = np.array(pil_image)
        image = image[:, :, ::-1]
        cv2.imshow("Eye Blink", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            exit()


while True:
    tudo()
