import time
import cv2

import numpy as np
import os
from face_comparator import *

def run():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    imgSize = list(frame.shape)
    outSize = imgSize[1::-1]

    fc = face_comparator(outSize)

    actual_fps = 0
    paused = False
    delay = {True: 0, False: 1}
    faceBB = [150, 80, 300, 300]

    img_reference = cv2.imread('img/2.jpg')
    res_reference = cv2.resize(img_reference,(frame.shape[1],frame.shape[0]), interpolation = cv2.INTER_CUBIC)
    res_reference, face_key_points_reference = fc.get_face_key_points(res_reference, faceBB)
    cv2.imshow("img", res_reference)

    while True:
        #start_time = time.time()
        try:
            ret, frame = cap.read()
            frame = cv2.flip( frame, 1 )

        except Exception as e:
            print("Failed to grab", e)
            break

        res, face_key_points = fc.get_face_key_points(frame, faceBB)
        cv2.imshow("OpenPose result", res)

        #print('face_key_points={}'.format(face_key_points))

        key = cv2.waitKey(delay[paused])
        if key & 255 == ord('p'):
            paused = not paused

        if key & 255 == ord('q'):
            break

        if key & 255 == ord('r'):
            faceBB = initFaceBB

        #actual_fps = 1.0 / (time.time() - start_time)
        #print('actual_fps={}'.format(actual_fps))

        fc.compare_face(face_key_points_reference, face_key_points)


if __name__ == '__main__':
    run()
