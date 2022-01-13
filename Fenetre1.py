# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 23:47:35 2021

@author: yonau
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,QLabel,
                             QApplication, QMainWindow, QWidget, QTextEdit, QDialog)

import Musique_titres

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.image = QPixmap('QUIZ_Residence_Amaraggi5.png')
        self.begin=QPushButton('On commence !')
        
        self.label = QLabel()
        self.label.setPixmap(self.image)

        self.grid = QGridLayout()
        self.grid.addWidget(self.label,0,1)
        self.grid.addWidget(self.begin,1,1)
        self.setLayout(self.grid)

        self.setGeometry(137,62,697,392)
        self.setWindowTitle("QUIZ - Residence AMARAGGI")
        self.InitUI()
    
    def InitUI(self):
        self.show()
        self.begin.clicked.connect(self.commence)
        
    def commence(self):
        self.mydialog= QMainWindow()
        self.ui=Musique_titres.Window()
        self.ui.InitUI(self.mydialog)
        self.mydialog.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
