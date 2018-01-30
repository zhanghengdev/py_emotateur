import PyOpenPose as OP
import cv2
import numpy as np
import os
from numpy.linalg import pinv
from scipy.spatial import distance

OPENPOSE_ROOT = os.environ["OPENPOSE_ROOT"]

class face_comparator:
    def __init__(self, outSize):
        download_heatmaps = False
        with_hands = False
        with_face = True
        self.outSize = outSize
        self.op = OP.OpenPose((640, 480), (240, 240), tuple(self.outSize), "COCO", OPENPOSE_ROOT + os.sep + "models" + os.sep, 0,
                         download_heatmaps, OP.OpenPose.ScaleMode.ZeroToOne, with_face, with_hands)
        self.last_distance_0 = 0
        self.last_distance_1 = 0
        self.last_distance_2 = 0

    def computeBB(self, face_key_points, faceBB, padding=0.4):
        score = np.mean(face_key_points[:, 2])
        if score < 0.5:
            return False, faceBB
        minX = np.min(face_key_points[:, 0])
        minY = np.min(face_key_points[:, 1])
        maxX = np.max(face_key_points[:, 0])
        maxY = np.max(face_key_points[:, 1])
        width = maxX - minX
        height = maxY - minY
        padX = width * padding / 2
        padY = height * padding / 2
        minX -= padX
        minY -= padY
        width += 2 * padX
        height += 2 * padY
        return True, [int(minX), int(minY), int(width), int(height)]

    def get_face_key_points(self, img, faceBB):
        rgb = img[:, :self.outSize[0]]
        self.op.detectFace(rgb, np.array(faceBB, dtype=np.int32).reshape((1, 4)))
        res = self.op.render(rgb)
        face_key_points = self.op.getKeypoints(self.op.KeypointType.FACE)[0].reshape(-1, 3)
        return res, face_key_points

    def compare_face(self, face_key_points_1, face_key_points_2):
        # check if most part of the face is detected
        score = np.mean(face_key_points_2[:, 2])
        if score < 0.5:
            return 0
        face_key_points_1[:, 2] = 1
        face_key_points_2[:, 2] = 1

        # alignement_1
        a = 1/(distance.euclidean(face_key_points_1[30, :2], face_key_points_1[8, :2]))
        T_1 = np.array([[a,0,0],[0,a,0],[0,0,1]])
        # alignement_2
        location_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                                27, 28, 29, 30]
        I = np.transpose(face_key_points_2[location_indexes, :])
        face_key_points_1_transformed = np.transpose(np.dot(T_1, np.transpose(face_key_points_1)))
        I_p = np.transpose(face_key_points_1_transformed[location_indexes, :])
        T_2 = np.dot(I_p, pinv(I))

        # vectors
        signature_indexes = [17, 18, 19, 20, 21,                                # left eye brow
                                22, 23, 24, 25, 26,                             # right eye brow
                                36, 37, 38, 39, 40, 41,                         # left eye
                                42, 43, 44, 45, 46, 47,                         # right eye
                                48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, # outside mouth
                                60, 61, 62, 63, 64, 65, 66, 67,                 # inside mouth
                                68, 69]                                         # pupil
        center_index = 30
        # vectors_1
        face_key_points_1_signature_aligned = np.transpose(np.dot(T_1, np.transpose(face_key_points_1[signature_indexes, :])))
        face_key_points_1_center_aligned = np.transpose(np.dot(T_1, np.transpose(face_key_points_1[center_index, :])))
        vectors_1 = face_key_points_1_signature_aligned[:,:2]-face_key_points_1_center_aligned[:2]
        # vectors_2
        face_key_points_2_signature_aligned = np.transpose(np.dot(T_2, np.transpose(face_key_points_2[signature_indexes, :])))
        face_key_points_2_center_aligned = np.transpose(np.dot(T_2, np.transpose(face_key_points_2[center_index, :])))
        vectors_2 = face_key_points_2_signature_aligned[:,:2]-face_key_points_2_center_aligned[:2]


        # Gauss filter
        gauss_filter = [7/74, 26/74, 41/74]

        # Euclidean distance
        #euclidean_distance = 0
        #for i in range(len(signature_indexes)):
            #l2_distance += np.linalg.norm(vectors_1[i, :]-vectors_2[i, :])
        #    euclidean_distance += distance.euclidean(vectors_1[i, :], vectors_2[i, :])

        # squared Euclidean distance
        squared_euclidean_distance = 0
        for i in range(len(signature_indexes)):
            squared_euclidean_distance += (distance.euclidean(vectors_1[i, :], vectors_2[i, :]))**2
        self.last_distance_2 = self.last_distance_1
        self.last_distance_1 = self.last_distance_0
        self.last_distance_0 = squared_euclidean_distance
        squared_euclidean_distance = np.dot(gauss_filter, [self.last_distance_2, self.last_distance_1, self.last_distance_0])
        # cos distance
        #cos_distance = 0
        #for i in range(len(signature_indexes)):
        #    cos_distance += distance.cosine(vectors_1[i, :], vectors_2[i, :])

        # squared cos distance
        #squared_cos_distance = 0
        #for i in range(len(signature_indexes)):
        #    squared_cos_distance += (distance.cosine(vectors_1[i, :], vectors_2[i, :])/10)**2

        # total distance
        #total_distance = l2_distance + cos_distance*1000
        total_distance = squared_euclidean_distance
        print('total_distance={}\r'.format(total_distance), end='')

        # convert distance to similarity
        #distance_when_similarity_is_90 = 30
        #distance_when_similarity_is_0 = 100
        #similarity = min(1, max(0, 0.9*(distance_when_similarity_is_0-total_distance)/(distance_when_similarity_is_0-distance_when_similarity_is_90)))

        sim = max(0, min(1, 1-total_distance))
        return ((sim*100)**0.5)*10
