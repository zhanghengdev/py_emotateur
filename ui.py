# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from random import *
import sys, os

class ui(object):
    def __init__(self, Form):
        self.Form = Form
        self.Form.setObjectName("Form")

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
        self.next_button = QtWidgets.QPushButton(Form)
        self.next_button.setIcon(QtGui.QIcon("icon/next.png"))
        self.next_button.setObjectName("next_button")
        self.buttonsHorizontalLayout.addWidget(self.next_button)
        self.showmore_button = QtWidgets.QPushButton(Form)
        self.showmore_button.setIcon(QtGui.QIcon("icon/convert.png"))
        self.showmore_button.setObjectName("showmore_button")
        self.buttonsHorizontalLayout.addWidget(self.showmore_button)
        self.about_us_button = QtWidgets.QPushButton(Form)
        self.about_us_button.setIcon(QtGui.QIcon("icon/info.png"))
        self.about_us_button.setObjectName("about_us_button")
        self.buttonsHorizontalLayout.addWidget(self.about_us_button)
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
        self.left_label_down.hide()
        self.left_vertical_layout.addWidget(self.left_label_down)

        self.similarity_vertical_layout = QtWidgets.QVBoxLayout()
        self.similarity_vertical_layout.setObjectName("similarity_vertical_layout")
        self.similarity = QtWidgets.QLabel(Form)
        self.similarity.setAlignment(QtCore.Qt.AlignCenter)
        self.similarity.setObjectName("similarity")
        self.similarity_vertical_layout.addWidget(self.similarity)
        self.similarity_number = QtWidgets.QLabel(Form)
        self.similarity_number.setAlignment(QtCore.Qt.AlignCenter)
        self.similarity_number.setPixmap(QtGui.QPixmap("icon/sim.png").scaled(40, 40))
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
        self.right_label_down.hide()
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
        self.showmore_button.clicked.connect(self.show_more_info)
        self.about_us_button.clicked.connect(self.show_about_us)
        QtCore.QMetaObject.connectSlotsByName(self.Form)
        self.Form.setWindowTitle("emotateur")
        self.Form.setFixedSize(1400, 600)
        self.setFrench()

    def start_home_screen(self):
        self.left_label_up.hide()
        self.graphicsView.show()
        self.left_label_down.hide()
        self.right_label_down.hide()
        self.Form.setFixedSize(1400, 600)

    def stop_home_screen(self):
        self.left_label_up.show()
        self.graphicsView.hide()
        self.left_label_down.hide()
        self.right_label_down.hide()
        self.Form.setFixedSize(1400, 600)

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

    def show_more_info(self):
        if self.left_label_down.isVisible():
            self.left_label_down.hide()
            self.right_label_down.hide()
            self.Form.setFixedSize(1400, 600)
        else:
            self.left_label_down.show()
            self.right_label_down.show()
            self.Form.setFixedSize(1400, 1080)

    def show_about_us(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle('Imamapi')
        msgBox.setIconPixmap(QtGui.QPixmap("icon/img.jpg").scaled(640, 640))
        ret = msgBox.exec_()

    def setFrench(self):
        self.home_button.setText("Maison")
        self.start_button.setText("Commencer")
        self.next_button.setText("prochain")
        self.similarity.setText("similarité")
        self.showmore_button.setText("Changer le mode d'affichage")
        self.about_us_button.setText("À propos de nous")
    def setEnglish(self):
        self.home_button.setText("Home")
        self.start_button.setText("Start")
        self.next_button.setText("Next")
        self.similarity.setText("similarity")
        self.showmore_button.setText("Switch the display mode")
        self.about_us_button.setText("About us")
    def setChinese(self):
        self.home_button.setText("回到主页")
        self.start_button.setText("开始游戏")
        self.next_button.setText("下一个")
        self.similarity.setText("相似度")
        self.showmore_button.setText("切换显示模式")
        self.about_us_button.setText("关于我们")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = ui(Form)
    Form.show()
    sys.exit(app.exec_())
