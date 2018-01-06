# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pyqtWork\projetV1\test.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class ui(object):
    def __init__(self, Form):
        Form.setObjectName("Form")
        self.overall_vertical_layout = QtWidgets.QVBoxLayout(Form)
        self.overall_vertical_layout.setObjectName("overall_vertical_layout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.folder_button = QtWidgets.QPushButton(Form)
        self.folder_button.setIcon(QtGui.QIcon("icon/folder.png"))
        self.folder_button.setObjectName("folder_button")
        self.horizontalLayout.addWidget(self.folder_button)
        self.horizontalLayout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.french_button = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/france.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.french_button.setIcon(icon1)
        self.french_button.setObjectName("french_button")
        self.horizontalLayout.addWidget(self.french_button)
        self.english_button = QtWidgets.QPushButton(Form)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/angleterre.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.english_button.setIcon(icon2)
        self.english_button.setObjectName("english_button")
        self.horizontalLayout.addWidget(self.english_button)
        self.chinese_button = QtWidgets.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/chine.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chinese_button.setIcon(icon)
        self.chinese_button.setObjectName("chinese_button")
        self.horizontalLayout.addWidget(self.chinese_button)
        self.overall_vertical_layout.addLayout(self.horizontalLayout)

        self.main_horizontal_layout = QtWidgets.QHBoxLayout()
        self.main_horizontal_layout.setObjectName("main_horizontal_layout")
        self.left_label = QtWidgets.QLabel(Form)
        self.left_label.setObjectName("left_label")
        self.left_label.resize(640, 480)
        self.main_horizontal_layout.addWidget(self.left_label)

        self.similarity_vertical_layout = QtWidgets.QVBoxLayout()
        self.similarity_vertical_layout.setObjectName("similarity_vertical_layout")
        self.similarity = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.similarity.setFont(font)
        self.similarity.setAlignment(QtCore.Qt.AlignCenter)
        self.similarity.setObjectName("similarity")
        self.similarity_vertical_layout.addWidget(self.similarity)
        self.similarity_number = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.similarity_number.setFont(font)
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
        self.main_horizontal_layout.addLayout(self.similarity_vertical_layout)

        self.right_label = QtWidgets.QLabel(Form)
        self.right_label.setObjectName("right_label")
        self.right_label.resize(640, 480)
        self.main_horizontal_layout.addWidget(self.right_label)
        self.overall_vertical_layout.addLayout(self.main_horizontal_layout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "emotateur"))
        self.folder_button.setText(_translate("Form", "open file"))
        self.chinese_button.setText(_translate("Form", "中文"))
        self.french_button.setText(_translate("Form", "Français"))
        self.english_button.setText(_translate("Form", "English"))
        self.left_label.setText(_translate("Form", "left"))
        self.similarity.setText(_translate("Form", "similarity"))
        self.similarity_number.setText(_translate("Form", "100%"))
        self.right_label.setText(_translate("Form", "right"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui().setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
