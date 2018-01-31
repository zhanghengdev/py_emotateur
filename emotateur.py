from ui import ui
from result_win import result_win
from PyQt5 import QtCore, QtGui, QtWidgets
from face_comparator import *
import cv2
import sys
import time

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
        self.ui.one_player_button.clicked.connect(self.start_one_player_game)
        self.ui.two_players_button.clicked.connect(self.start_two_players_game)
        self.ui.next_button.clicked.connect(self.load_next_image)
        self.ui.stop_button.clicked.connect(self.stop_two_players_game)
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
        self.one_player_game_timer=QtCore.QTimer()
        self.one_player_game_timer.timeout.connect(self.one_player_mode_update_frame)
        self.one_player_game_timer.timeout.connect(self.one_player_mode_update_score)
        self.two_players_left_timer=QtCore.QTimer()
        self.two_players_left_timer.timeout.connect(self.two_players_mode_update_reference)
        self.two_players_right_timer=QtCore.QTimer()
        self.two_players_right_timer.timeout.connect(self.two_players_mode_update_score)
        self.home_timer=QtCore.QTimer()
        self.home_timer.timeout.connect(self.one_player_mode_update_frame)
        self.home_timer.timeout.connect(self.ui.update_home_scene)
        self.detected = False
        self.current_image = 0
        self.start_time = 0
        self.start_home_screen()

    def opencvimg_2_pixmap(self, srcMat):
        cv2.cvtColor(srcMat, cv2.COLOR_BGR2RGB,srcMat)
        height, width, bytesPerComponent= srcMat.shape
        bytesPerLine = bytesPerComponent* width
        srcQImage= QtGui.QImage(srcMat.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        return QtGui.QPixmap.fromImage(srcQImage)

    def start_home_screen(self):
        self.stop_all_timers()
        self.home_timer.start(1000/5)
        self.ui.set_state(0)
        self.ui.update_score(0)
        self.detected = False

    def load_image(self):
        img_reference_file_name = os.path.join('img','{}.jpg'.format(self.current_image))
        img_reference = cv2.imread(img_reference_file_name)
        res_reference = cv2.resize(img_reference,(640, 480), interpolation = cv2.INTER_CUBIC)
        faceBB = self.reference_faceBB[self.current_image]
        res_reference, self.face_key_points_reference = self.fc.get_face_key_points(res_reference, faceBB)
        self.reference_image = QtGui.QPixmap(img_reference_file_name).scaled(640, 480)
        self.ui.update_left_label_up_with_pixmap(self.reference_image)
        self.ui.update_left_label_down_with_pixmap(self.opencvimg_2_pixmap(res_reference))

    def stop_all_timers(self):
        self.home_timer.stop()
        self.one_player_game_timer.stop()
        self.two_players_left_timer.stop()
        self.two_players_right_timer.stop()

    def start_one_player_game(self):
        self.stop_all_timers()
        self.current_image = 0
        self.start_time = time.time()
        self.load_image()
        self.one_player_game_timer.start(1000/2)
        self.ui.set_state(1)
        self.result_win = result_win(QtWidgets.QWidget())

    def start_two_players_game(self):
        self.stop_all_timers()
        self.start_time = time.time()
        self.one_player_game_timer.stop()
        self.two_players_left_timer.start(1000/2)
        self.ui.set_state(2)
        self.result_win = result_win(QtWidgets.QWidget())

    def two_players_mode_update_reference(self):
        time_used = time.time()-self.start_time
        self.ui.update_time_left(15-time_used)
        if time_used > 15:
            self.two_players_left_timer.stop()
            self.start_time = time.time()
            self.two_players_right_timer.start(1000/2)
            return

        img_reference_file_name = os.path.join('icon','no_signal.jpg')
        reference_image = QtGui.QPixmap(img_reference_file_name).scaled(640, 480)
        self.ui.update_right_label_up_with_pixmap(reference_image)
        self.ui.update_right_label_down_with_pixmap(reference_image)

        frame = self.read_image_from_webcam()
        res, self.face_key_points_reference = self.fc.get_face_key_points(frame, self.faceBB)
        self.detected, self.faceBB = self.fc.computeBB(self.face_key_points_reference, self.faceBB)
        frame = self.draw_rectangle(frame)
        res = self.draw_rectangle(res)
        self.reference_image = self.opencvimg_2_pixmap(frame)
        self.ui.update_left_label_up_with_pixmap(self.reference_image)
        self.ui.update_left_label_down_with_pixmap(self.opencvimg_2_pixmap(res))

    def two_players_mode_update_score(self):
        time_used = time.time()-self.start_time
        self.ui.update_time_left(20-time_used)
        if time_used > 20:
            self.two_players_right_timer.stop()
            self.start_time = time.time()
            self.two_players_left_timer.start(1000/2)
            return

        frame = self.read_image_from_webcam()
        res, face_key_points = self.fc.get_face_key_points(frame, self.faceBB)
        self.detected, self.faceBB = self.fc.computeBB(face_key_points, self.faceBB)
        frame_rec = self.draw_rectangle(frame)
        res = self.draw_rectangle(res)
        self.ui.update_right_label_up_with_pixmap(self.opencvimg_2_pixmap(frame_rec))
        self.ui.update_right_label_down_with_pixmap(self.opencvimg_2_pixmap(res))
        similarity = self.fc.compare_face(self.face_key_points_reference, face_key_points)
        similarity = similarity if time_used > 10 else 0
        self.ui.update_score(similarity)
        if similarity > 90:
            self.two_players_right_timer.stop()
            self.start_time = time.time()
            self.two_players_left_timer.start(1000/2)
            self.result_win.add_images(self.reference_image,self.opencvimg_2_pixmap(frame))

    def stop_two_players_game(self):
        self.result_win.Form.show()
        self.start_home_screen()

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

    def one_player_mode_update_frame(self):
        frame = self.read_image_from_webcam()
        frame = self.draw_rectangle(frame)
        self.ui.update_right_label_up_with_pixmap(self.opencvimg_2_pixmap(frame))

    def one_player_mode_update_score(self):
        frame = self.read_image_from_webcam()
        res, face_key_points = self.fc.get_face_key_points(frame, self.faceBB)
        self.detected, self.faceBB = self.fc.computeBB(face_key_points, self.faceBB)
        res = self.draw_rectangle(res)
        self.ui.update_right_label_down_with_pixmap(self.opencvimg_2_pixmap(res))
        similarity = self.fc.compare_face(self.face_key_points_reference, face_key_points)
        self.ui.update_score(similarity)
        time_used = time.time()-self.start_time
        self.ui.update_time_left(60-time_used)
        if time_used > 60:
            self.result_win.Form.show()
            self.start_home_screen()
        if similarity > 90:
            self.result_win.add_images(self.reference_image,self.opencvimg_2_pixmap(frame))
            self.load_next_image()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    e = emotateur()
    e.Form.show()
    sys.exit(app.exec_())
