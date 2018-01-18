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
 faceBB = [200, 160, 230, 230]

 img_reference = cv2.imread('img/9.jpg')
 color = [50, 155, 50]
 res_reference = cv2.resize(img_reference,(frame.shape[1],frame.shape[0]), interpolation = cv2.INTER_CUBIC)
 res_reference, face_key_points_reference = fc.get_face_key_points(res_reference, faceBB)
 cv2.rectangle(res_reference, (faceBB[0], faceBB[1]), (faceBB[0] + faceBB[2], faceBB[1] + faceBB[3]), color, 2)
 cv2.imshow("img", res_reference)
 cv2.waitKey(0)
 cv2.destroyAllWindows()

if __name__ == '__main__':
 run()
