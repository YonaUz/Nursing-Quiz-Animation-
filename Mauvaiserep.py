# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 00:31:12 2021

@author: yonau
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
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

        self.label = QLabel()
        self.label.setGeometry(QtCore.QRect(0,0,697,392))
        self.label.setObjectName("label")
        
        #self.begin=QPushButton('On commence !')
        #self.b=Musique_titres.Window().reponse()
        #self.info= QLabel(f"{self.b}")
        
        #set qmovie as label
        self.movie = QMovie("Perdu2.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        
        self.grid = QGridLayout()
        self.grid.addWidget(self.label,0,1)
        #self.grid.addWidget(self.info,1,1)
        self.setLayout(self.grid)
        

        #self.setGeometry(50,50,320,200)
        self.setGeometry(137,62,697,392)
        self.setWindowTitle("QUIZ - Residence AMARAGGI")
        self.InitUI()
    
    def InitUI(self):
        self.show()
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())