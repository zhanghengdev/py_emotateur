# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from random import *
import sys, os

class result_win(object):
    def __init__(self, Form):
        self.Form = Form
        self.Form.setObjectName("Form")
        self.overall_vertical_layout = QtWidgets.QVBoxLayout(Form)
        self.overall_vertical_layout.setObjectName("overall_vertical_layout")
        self.Form.setWindowTitle("emotateur")
        self.added = False

    def is_added(self):
        return self.added

    def add_images(self, pix_map0, pix_map1):
        self.added = True
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.left_label = QtWidgets.QLabel(self.Form)
        self.left_label.setObjectName("left_label")
        self.left_label.setPixmap(pix_map0.scaled(320, 240))
        self.horizontalLayout.addWidget(self.left_label)
        self.right_label = QtWidgets.QLabel(self.Form)
        self.right_label.setObjectName("right_label")
        self.right_label.setPixmap(pix_map1.scaled(320, 240))
        self.horizontalLayout.addWidget(self.right_label)
        self.overall_vertical_layout.addLayout(self.horizontalLayout)
