# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from random import *
import sys, os

class ui(object):
    def __init__(self, Form):
        self.Form = Form
        self.Form.setObjectName("Form")
        self.Form.setFixedSize(1400, 500)

        self.overall_vertical_layout = QtWidgets.QVBoxLayout(Form)
        self.overall_vertical_layout.setObjectName("overall_vertical_layout")

        self.buttonsHorizontalLayout = QtWidgets.QHBoxLayout()
        self.buttonsHorizontalLayout.setObjectName("buttonsHorizontalLayout")
        self.home_button = QtWidgets.QPushButton(Form)
        self.home_button.setIcon(QtGui.QIcon("icon/home.png"))
        self.home_button.setObjectName("home_button")
        self.buttonsHorizontalLayout.addWidget(self.home_button)
        self.start_button = QtWidgets.QPushButton(Form)
        self.start_button.setIcon(QtGui.QIcon("icon/start.png"))
        self.start_button.setObjectName("start_button")
        self.buttonsHorizontalLayout.addWidget(self.start_button)
        self.one_player_button = QtWidgets.QPushButton(Form)
        self.one_player_button.setIcon(QtGui.QIcon("icon/one.png"))
        self.one_player_button.setObjectName("one_player_button")
        self.buttonsHorizontalLayout.addWidget(self.one_player_button)
        self.two_players_button = QtWidgets.QPushButton(Form)
        self.two_players_button.setIcon(QtGui.QIcon("icon/two.png"))
        self.two_players_button.setObjectName("two_players_button")
        self.buttonsHorizontalLayout.addWidget(self.two_players_button)
        self.next_button = QtWidgets.QPushButton(Form)
        self.next_button.setIcon(QtGui.QIcon("icon/next.png"))
        self.next_button.setObjectName("next_button")
        self.buttonsHorizontalLayout.addWidget(self.next_button)
        self.stop_button = QtWidgets.QPushButton(Form)
        self.stop_button.setIcon(QtGui.QIcon("icon/stop.png"))
        self.stop_button.setObjectName("stop_button")
        self.buttonsHorizontalLayout.addWidget(self.stop_button)
        self.showmore_button = QtWidgets.QPushButton(Form)
        self.showmore_button.setIcon(QtGui.QIcon("icon/convert.png"))
        self.showmore_button.setObjectName("showmore_button")
        self.buttonsHorizontalLayout.addWidget(self.showmore_button)
        self.buttonsHorizontalLayout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.info_label = QtWidgets.QLabel(Form)
        self.info_label.setObjectName("info_label")
        self.buttonsHorizontalLayout.addWidget(self.info_label)
        self.time_left_label = QtWidgets.QLabel(Form)
        self.time_left_label.setObjectName("time_left_label")
        self.buttonsHorizontalLayout.addWidget(self.time_left_label)
        self.buttonsHorizontalLayout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.french_button = QtWidgets.QPushButton(Form)
        self.french_button.setIcon(QtGui.QIcon("icon/france.ico"))
        self.french_button.setText("Français")
        self.french_button.setObjectName("french_button")
        self.buttonsHorizontalLayout.addWidget(self.french_button)
        self.english_button = QtWidgets.QPushButton(Form)
        self.english_button.setIcon(QtGui.QIcon("icon/angleterre.ico"))
        self.english_button.setText("English")
        self.english_button.setObjectName("english_button")
        self.buttonsHorizontalLayout.addWidget(self.english_button)
        self.chinese_button = QtWidgets.QPushButton(Form)
        self.chinese_button.setIcon(QtGui.QIcon("icon/chine.ico"))
        self.chinese_button.setText("中文")
        self.chinese_button.setObjectName("chinese_button")
        self.buttonsHorizontalLayout.addWidget(self.chinese_button)
        self.overall_vertical_layout.addLayout(self.buttonsHorizontalLayout)

        self.left_vertical_layout = QtWidgets.QVBoxLayout()
        self.left_vertical_layout.setObjectName("left_vertical_layout")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setFixedSize(640, 480)
        self.graphicsView.setObjectName("graphicsView")
        self.left_vertical_layout.addWidget(self.graphicsView)
        self.left_label_up = QtWidgets.QLabel(Form)
        self.left_label_up.setObjectName("left_label_up")
        self.left_vertical_layout.addWidget(self.left_label_up)
        self.left_label_down = QtWidgets.QLabel(Form)
        self.left_label_down.setObjectName("left_label_down")
        self.left_vertical_layout.addWidget(self.left_label_down)

        self.similarity_vertical_layout = QtWidgets.QVBoxLayout()
        self.similarity_vertical_layout.setObjectName("similarity_vertical_layout")
        self.similarity = QtWidgets.QLabel(Form)
        self.similarity.setAlignment(QtCore.Qt.AlignCenter)
        self.similarity.setObjectName("similarity")
        self.similarity_vertical_layout.addWidget(self.similarity)
        self.similarity_number = QtWidgets.QLabel(Form)
        self.similarity_number.setAlignment(QtCore.Qt.AlignCenter)
        self.similarity_number.setObjectName("similarity_number")
        self.similarity_vertical_layout.addWidget(self.similarity_number)

        self.similarity_horizontal_layout = QtWidgets.QHBoxLayout()
        self.similarity_horizontal_layout.setObjectName("similarity_horizontal_layout")
        self.similarity_horizontal_layout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.verticalSlider = QtWidgets.QSlider(Form)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.verticalSlider.setTickInterval(5)
        self.verticalSlider.setObjectName("verticalSlider")
        self.similarity_horizontal_layout.addWidget(self.verticalSlider)
        self.similarity_horizontal_layout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.similarity_vertical_layout.addLayout(self.similarity_horizontal_layout)

        self.right_vertical_layout = QtWidgets.QVBoxLayout()
        self.right_vertical_layout.setObjectName("right_vertical_layout")
        self.right_label_up = QtWidgets.QLabel(Form)
        self.right_label_up.setObjectName("right_label_up")
        self.right_vertical_layout.addWidget(self.right_label_up)
        self.right_label_down = QtWidgets.QLabel(Form)
        self.right_label_down.setObjectName("right_label_down")
        self.right_vertical_layout.addWidget(self.right_label_down)

        self.main_horizontal_layout = QtWidgets.QHBoxLayout()
        self.main_horizontal_layout.setObjectName("main_horizontal_layout")
        self.main_horizontal_layout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.main_horizontal_layout.addLayout(self.left_vertical_layout)
        self.main_horizontal_layout.addLayout(self.similarity_vertical_layout)
        self.main_horizontal_layout.addLayout(self.right_vertical_layout)
        self.main_horizontal_layout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.overall_vertical_layout.addLayout(self.main_horizontal_layout)

        self.scene = QtWidgets.QGraphicsScene()

        self.french_button.clicked.connect(self.setFrench)
        self.english_button.clicked.connect(self.setEnglish)
        self.chinese_button.clicked.connect(self.setChinese)
        self.start_button.clicked.connect(self.start_button_clicked)
        self.showmore_button.clicked.connect(self.show_more_info)
        QtCore.QMetaObject.connectSlotsByName(self.Form)
        self.Form.setWindowTitle("emotateur")
        self.setFrench()

    def set_state(self, mode):
        if mode == 0:
            self.start_button.setEnabled(True)
            self.home_button.setEnabled(False)
            self.next_button.hide()
            self.stop_button.hide()
            self.showmore_button.setEnabled(False)
            self.left_label_up.hide()
            self.graphicsView.show()
            self.left_label_down.hide()
            self.right_label_up.show()
            self.right_label_down.hide()
            self.one_player_button.hide()
            self.two_players_button.hide()
            self.info_label.hide()
            self.time_left_label.hide()
        else:
            self.start_button.setEnabled(False)
            self.home_button.setEnabled(True)
            if mode == 1:
                self.next_button.show()
                self.stop_button.hide()
            else:
                self.next_button.hide()
                self.stop_button.show()
            self.showmore_button.setEnabled(True)
            self.left_label_up.show()
            self.graphicsView.hide()
            self.left_label_down.hide()
            self.right_label_up.show()
            self.right_label_down.hide()
            self.one_player_button.hide()
            self.two_players_button.hide()
            self.info_label.show()
            self.time_left_label.show()

    def start_button_clicked(self):
        if self.one_player_button.isVisible():
            self.one_player_button.hide()
            self.two_players_button.hide()
        else:
            self.one_player_button.show()
            self.two_players_button.show()

    def update_home_scene(self):
        random_file = os.listdir('img/')[randint(0, len(os.listdir('img/'))-1)]
        file_name = os.path.join('img', random_file)
        item=QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap(file_name).scaled(160,120))
        self.scene.addItem(item)
        lig = randint(1, 3)
        col = randint(1, 3)
        item.setPos(col*160,lig*120)
        self.graphicsView.setScene(self.scene)

    def update_left_label_up_with_pixmap(self, pixmap_up):
        self.left_label_up.setPixmap(pixmap_up)
    def update_left_label_down_with_pixmap(self, pixmap_down):
        self.left_label_down.setPixmap(pixmap_down)
    def update_right_label_up_with_pixmap(self, pixmap_up):
        self.right_label_up.setPixmap(pixmap_up)
    def update_right_label_down_with_pixmap(self, pixmap_down):
        self.right_label_down.setPixmap(pixmap_down)

    def update_score(self, similarity):
        self.similarity_number.setText( "%.2f%%" % (similarity))
        if similarity > 90:
            self.similarity_number.setPixmap(QtGui.QPixmap("icon/success.png").scaled(40, 40))
        elif similarity > 80:
            self.similarity_number.setStyleSheet('color:green')
        elif similarity < 60:
            self.similarity_number.setStyleSheet('color:red')
        else:
            self.similarity_number.setStyleSheet('color:yellow')
        self.verticalSlider.setValue(int(similarity))

    def update_time_left(self, time):
        self.time_left_label.setText( "%.0fs" % (time))
        if time > 30:
            self.time_left_label.setStyleSheet('color:green')
        elif time < 10:
            self.time_left_label.setStyleSheet('color:red')
        else:
            self.time_left_label.setStyleSheet('color:yellow')

    def show_more_info(self):
        if self.left_label_down.isVisible():
            self.left_label_down.hide()
            self.right_label_down.hide()
            self.left_label_up.show()
            self.right_label_up.show()
        else:
            self.left_label_down.show()
            self.right_label_down.show()
            self.left_label_up.hide()
            self.right_label_up.hide()

    def setFrench(self):
        self.home_button.setText("Maison")
        self.start_button.setText("Commencer")
        self.next_button.setText("Prochain")
        self.info_label.setText("Temps restant:")
        self.stop_button.setText("Arrêter")
        self.similarity.setText("Similarité")
        self.showmore_button.setText("Points clés")
        self.one_player_button.setText('1 joueur')
        self.two_players_button.setText('2 joueurs')
    def setEnglish(self):
        self.home_button.setText("Home")
        self.start_button.setText("Start")
        self.next_button.setText("Next")
        self.stop_button.setText("Stop")
        self.info_label.setText("Time left:")
        self.similarity.setText("Similarity")
        self.showmore_button.setText("Landmarks")
        self.one_player_button.setText('1 player')
        self.two_players_button.setText('2 players')
    def setChinese(self):
        self.home_button.setText("回到主页")
        self.start_button.setText("开始游戏")
        self.next_button.setText("下一个")
        self.stop_button.setText("停止")
        self.info_label.setText("剩余时间：")
        self.similarity.setText("相似度")
        self.showmore_button.setText("显示关键点")
        self.one_player_button.setText('单人模式')
        self.two_players_button.setText('对战模式')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = ui(Form)
    Form.show()
    sys.exit(app.exec_())
