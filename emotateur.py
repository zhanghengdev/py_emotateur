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
    faceBB = [50, 50, 400, 400]

    img_reference_file_name = 'img/test1.jpg'
    img_reference = cv2.imread(img_reference_file_name)
    if 'test1' in img_reference_file_name:
        faceBB = [180, 50, 300, 300]
    elif 'test2' in img_reference_file_name:
        faceBB = [180, 60, 250, 250]
    res_reference = cv2.resize(img_reference,(frame.shape[1],frame.shape[0]), interpolation = cv2.INTER_CUBIC)
    res_reference, face_key_points_reference = fc.get_face_key_points(res_reference, faceBB)
    cv2.imshow("reference", res_reference)

    while True:
        start_time = time.time()
        try:
            ret, frame = cap.read()
            frame = cv2.flip( frame, 1 )

        except Exception as e:
            print("Failed to grab", e)
            break

        res, face_key_points = fc.get_face_key_points(frame, faceBB)
        cv2.putText(res, 'Press \'q\' to stop.', (20, 20), 0, 0.5, (0, 0, 255))
        cv2.putText(res, 'Press \'p\' to pause.', (20, 40), 0, 0.5, (0, 0, 255))
        cv2.imshow("webcam", res)

        key = cv2.waitKey(delay[paused])
        if key & 255 == ord('p'):
            paused = not paused

        if key & 255 == ord('q'):
            break

        actual_fps = 1.0 / (time.time() - start_time)
        similarity = fc.compare_face(face_key_points_reference, face_key_points)
        print('fps: %8.2f, similarity:%8.2f \r' % (actual_fps, similarity), end='')


if __name__ == '__main__':
    run()
