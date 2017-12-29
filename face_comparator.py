"""
Example script using only the Face detector of Openpose.
"""

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
        self.op = OP.OpenPose((656, 368), (240, 240), tuple(self.outSize), "COCO", OPENPOSE_ROOT + os.sep + "models" + os.sep, 0,
                         download_heatmaps, OP.OpenPose.ScaleMode.ZeroToOne, with_face, with_hands)

    def get_face_key_points(self, img, faceBB):
        rgb = img[:, :self.outSize[0]]
        self.op.detectFace(rgb, np.array(faceBB, dtype=np.int32).reshape((1, 4)))
        res = self.op.render(rgb)
        cv2.rectangle(res, (faceBB[0], faceBB[1]), (faceBB[0] + faceBB[2], faceBB[1] + faceBB[3]), [50, 155, 50], 2)
        face_key_points = self.op.getKeypoints(self.op.KeypointType.FACE)[0].reshape(-1, 3)
        return res, face_key_points

    def compare_face(self, face_key_points_1, face_key_points_2):
        sim = 0
        score = np.mean(face_key_points_2[:, 2])
        if score < 0.5:
            return 0
        face_key_points_1[:, 2] = 1
        face_key_points_2[:, 2] = 1
        # alignement
        location_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 27, 28, 29, 30]
        # homographie
        #transformation = np.zeros((len(location_indexes)*2, 9))
        #for i, location_index in enumerate(location_indexes):
        #    transformation[2i, 0] = face_key_points_2[location_index, 0]    #x
        #    transformation[2i, 1] = face_key_points_2[location_index, 1]    #y
        #    transformation[2i, 2] = 1                                       #1
        #    transformation[2i, 3] = 0                                       #0
        #    transformation[2i, 4] = 0                                       #0
        #    transformation[2i, 5] = 0                                       #0
        #    transformation[2i, 6] = -1*face_key_points_1[location_index, 0]*face_key_points_2[location_index, 0]    #-x'*x
        #    transformation[2i, 7] = -1*face_key_points_1[location_index, 0]*face_key_points_2[location_index, 1]    #-x'*y
        #    transformation[2i, 8] = -1*face_key_points_1[location_index, 0] #-x'
        #    transformation[2i+1, 0] = 0                                     #0
        #    transformation[2i+1, 1] = 0                                     #0
        #    transformation[2i+1, 2] = 0                                     #0
        #    transformation[2i+1, 3] = face_key_points_2[location_index, 0]  #x
        #    transformation[2i+1, 4] = face_key_points_2[location_index, 1]  #y
        #    transformation[2i+1, 5] = 1                                     #1
        #    transformation[2i+1, 6] = -1*face_key_points_1[location_index, 1]*face_key_points_2[location_index, 0]    #-y'*x
        #    transformation[2i+1, 7] = -1*face_key_points_1[location_index, 1]*face_key_points_2[location_index, 1]    #-y'*y
        #    transformation[2i+1, 8] = -1*face_key_points_1[location_index, 1] #-y'
        # transformation affine
        #I = np.zeros((3, len(location_indexes)))
        #I_p = np.zeros((3, len(location_indexes)))
        #for i, location_index in enumerate(location_indexes):
        #    I[0,i] = face_key_points_2[location_index, 0]    #x
        #    I[1,i] = face_key_points_2[location_index, 1]    #y
        #    I[2,i] = 1
        #    I_p[0,i] = face_key_points_1[location_index, 0]  #x'
        #    I_p[1,i] = face_key_points_1[location_index, 1]  #y'
        #    I_p[2,i] = 1
        I = np.transpose(face_key_points_2[location_indexes, :])
        I_p = np.transpose(face_key_points_1[location_indexes, :])
        T = np.dot(I_p, pinv(I))

        # vectors
        signature_indexes = [17, 18, 19, 20, 21,                                # left eye brow
                                22, 23, 24, 25, 26,                             # right eye brow
                                36, 37, 38, 39, 40, 41,                         # left eye
                                42, 43, 44, 45, 46, 47,                         # right eye
                                48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, # outside mouth
                                60, 61, 62, 63, 64, 65, 66, 67,                 # inside mouth
                                68, 69]                                         # eyes
        center_index = 30
        #vectors_1 = np.zeros((len(signature_indexes), 2))
        #vectors_2 = np.zeros((len(signature_indexes), 2))
        #for i, signature_index in enumerate(signature_indexes):
            # vectors_1
        #    vectors_1[i,0] = face_key_points_1[signature_index, 0] - face_key_points_1[center_index, 0] #x'-x'0
        #    vectors_1[i,1] = face_key_points_1[signature_index, 1] - face_key_points_1[center_index, 1] #y'-y'0
            # vectors_2
        #    face_key_point_2_before_aligned = np.zeros((1,3))
        #    face_key_point_2_before_aligned[0,0] = face_key_points_2[signature_index, 0]
        #    face_key_point_2_before_aligned[0,0] = face_key_points_2[signature_index, 0]
        #    face_key_point_2_aligned = T*face_key_points_2[signature_index, 0:1]

        # vectors_1
        vectors_1 = face_key_points_1[signature_indexes, :2] - face_key_points_1[center_index, :2]
        # vectors_2
        face_key_points_2_signature_aligned = np.transpose(np.dot(T, np.transpose(face_key_points_2[signature_indexes, :])))
        face_key_points_2_center_aligned = np.transpose(np.dot(T, np.transpose(face_key_points_2[center_index, :])))
        vectors_2 = face_key_points_2_signature_aligned[:,:2]-face_key_points_2_center_aligned[:2]

        # l2 distance
        l2_distance = 0
        for i in range(len(signature_indexes)):
            #l2_distance += np.linalg.norm(vectors_1[i, :]-vectors_2[i, :])
            l2_distance += distance.euclidean(vectors_1[i, :], vectors_2[i, :])

        # l2 normalised distance
        l2_normalised_distance = 0
        for i in range(len(signature_indexes)):
            #l2_distance += np.linalg.norm(vectors_1[i, :]-vectors_2[i, :])
            vector_1_nor = vectors_1[i, :] / np.linalg.norm(vectors_1[i, :])
            vector_2_nor = vectors_2[i, :] / np.linalg.norm(vectors_2[i, :])
            l2_normalised_distance += distance.euclidean(vector_1_nor, vector_2_nor)

        # cos distance
        #cos_distance = 0
        #for i in range(len(signature_indexes)):
        #    cos_distance += distance.cosine(vectors_1[i, :], vectors_2[i, :])

        # total distance
        #total_distance = l2_distance + cos_distance*1000
        total_distance = 0

        print('*********')
        print('l2_distance={}'.format(l2_distance))
        print('l2_normalised_distance={}'.format(l2_normalised_distance))
        return total_distance
