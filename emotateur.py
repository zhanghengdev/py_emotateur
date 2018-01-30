from ui import ui
from PyQt5 import QtCore, QtGui, QtWidgets
from face_comparator import *
import cv2
import sys

class emotateur():
    def __init__(self):
        self.Form=QtWidgets.QWidget()
        self.ui = ui(self.Form)
        self.cap=cv2.VideoCapture()
        if not self.cap.open(0):
            print("camera configuration failed")
            sys.exit(0)
        ret, frame = self.cap.read()
        imgSize = list(frame.shape)
        outSize = imgSize[1::-1]
        self.fc = face_comparator(outSize)
        self.ui.home_button.clicked.connect(self.start_home_screen)
        self.ui.start_button.clicked.connect(self.start_game)
        self.ui.next_button.clicked.connect(self.load_next_image)
        self.faceBB = [150, 75, 300, 300]
        self.reference_faceBB = [   [180, 50, 300, 300],
                                    [180, 60, 250, 250],
                                    [220, 120, 230, 230],
                                    [250, 90, 200, 200],
                                    [150, 75, 300, 300],
                                    [160, 100, 250, 250],
                                    [180, 100, 300, 300],
                                    [180, 80, 300, 300],
                                    [120, 100, 380, 380],
                                    [200, 160, 230, 230],
                                    [120, 120, 400, 400],
                                    [280, 100, 200, 200],
                                    [150, 100, 300, 300],
                                    [200, 100, 300, 300],
                                    [150, 30, 350, 350],
                                    [130, 120, 320, 320],
                                    [130, 120, 320, 320],
                                    [180, 100, 250, 250],
                                    [220, 100, 150, 150],
                                    [250, 80, 200, 200]   ]
        self.update_frame_score_timer=QtCore.QTimer()
        self.update_frame_score_timer.timeout.connect(self.updateFrame)
        self.update_frame_score_timer.timeout.connect(self.updateScore)
        self.home_timer=QtCore.QTimer()
        self.home_timer.timeout.connect(self.updateFrame)
        self.home_timer.timeout.connect(self.ui.update_home_scene)
        self.detected = False
        self.current_image = 0
        self.start_home_screen()

    def opencvimg_2_pixmap(self, srcMat):
        cv2.cvtColor(srcMat, cv2.COLOR_BGR2RGB,srcMat)
        height, width, bytesPerComponent= srcMat.shape
        bytesPerLine = bytesPerComponent* width
        srcQImage= QtGui.QImage(srcMat.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        return QtGui.QPixmap.fromImage(srcQImage)

    def start_home_screen(self):
        if self.update_frame_score_timer.isActive():
            self.update_frame_score_timer.stop()
        self.home_timer.start(1000/5)
        self.ui.set_state(False)
        self.ui.update_score(0)
        self.detected = False

    def load_image(self):
        img_reference_file_name = os.path.join('img','{}.jpg'.format(self.current_image))
        img_reference = cv2.imread(img_reference_file_name)
        res_reference = cv2.resize(img_reference,(640, 480), interpolation = cv2.INTER_CUBIC)
        faceBB = self.reference_faceBB[self.current_image]
        res_reference, self.face_key_points_reference = self.fc.get_face_key_points(res_reference, faceBB)
        self.ui.update_left_label_up_with_pixmap(QtGui.QPixmap(img_reference_file_name).scaled(640, 480))
        self.ui.update_left_label_down_with_pixmap(self.opencvimg_2_pixmap(res_reference))

    def start_game(self):
        self.home_timer.stop()
        self.current_image = 0
        self.load_image()
        self.update_frame_score_timer.start(1000/2)
        self.ui.set_state(True)

    def load_next_image(self):
        if self.current_image == 20:
            self.current_image = 0
        else:
            self.current_image += 1
        self.load_image()

    def read_image_from_webcam(self):
        ret, srcMat=self.cap.read()
        frame=cv2.resize(srcMat, (640, 480), interpolation=cv2.INTER_CUBIC)
        frame=cv2.flip(frame, 1)
        return frame

    def draw_rectangle(self, frame):
        if self.detected:
            color = [50, 155, 50]
        else:
            color = [50, 50, 155]
        cv2.rectangle(frame, (self.faceBB[0], self.faceBB[1]), (self.faceBB[0] + self.faceBB[2], self.faceBB[1] + self.faceBB[3]), color, 2)
        return frame

    def updateFrame(self):
        frame = self.read_image_from_webcam()
        frame = self.draw_rectangle(frame)
        self.ui.update_right_label_up_with_pixmap(self.opencvimg_2_pixmap(frame))

    def updateScore(self):
        frame = self.read_image_from_webcam()
        res, face_key_points = self.fc.get_face_key_points(frame, self.faceBB)
        self.detected, self.faceBB = self.fc.computeBB(face_key_points, self.faceBB)
        frame = self.draw_rectangle(res)
        self.ui.update_right_label_down_with_pixmap(self.opencvimg_2_pixmap(res))
        similarity = self.fc.compare_face(self.face_key_points_reference, face_key_points)
        self.ui.update_score(similarity)
        if similarity > 90:
            self.load_next_image()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    e = emotateur()
    e.Form.show()
    sys.exit(app.exec_())
