# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 22:55:24 2021

@author: yonau
"""

import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,QLabel,
                             QApplication, QMainWindow, QWidget, QTextEdit, QDialog)
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from questions import quiz_musique_titre 
from questions import quiz_question_musique
import random
from playsound import playsound
import Bonnerep
import Mauvaiserep
import Drapeaux
liste_titre=[1,2,3,4,5,6]


class Window(QWidget):
    """Choisit aléatoirement une musique parmi celles enregistrées 
    et réagit en fonction de l'exactitude de la réponse.
    La réponse sera le titre de la musique jouée"""
    
    def __init__(self):
        super().__init__() #Constructeur 
        
        #choix aléatoire de la musique 
        self.a= random.choice(liste_titre)
        self.musique= quiz_question_musique[self.a]
        
        #titre de la fenetre 
        self.title = "QUIZ - Residence AMARAGGI"
        
        # Geometrie et place de la fenetre a l'ouverture 
        self.setGeometry(137,62,697,392)
        
        self.setStyleSheet("background-color: lightcyan;")
        
        #a=quiz_musique_titre[1]['bonnerep']
        self.texte = QLabel("Quel est le titre de la chanson suivante ?")
        self.texte.setAlignment(QtCore.Qt.AlignCenter) #alignement au centre 
        # setting font and size
        self.texte.setFont(QFont('Times', 20))
        
        self.play=QPushButton('Musique')
        #self.play.setGeometry(100, 100,111,28)
        #self.play.setStyleSheet("background-image : url(C:\\Users\\yonau\\Desktop\\EPISEN\\S2\\ECUE 261 Stage\\EHPAD\\play-button.png);")
        self.play.setIcon(QtGui.QIcon('play-icon'))
        #self.play.setStyleSheet("QPushButton{border-image: url(C:\\Users\\yonau\\Desktop\\EPISEN\\S2\\ECUE 261 Stage\\EHPAD\\play2.png);")
        self.bonnerep=QPushButton(quiz_musique_titre[self.a]['bonnerep'])
        self.prop2=QPushButton(quiz_musique_titre[self.a]['prop2'])
        self.prop3=QPushButton(quiz_musique_titre[self.a]['prop3'])
        self.prop4=QPushButton(quiz_musique_titre[self.a]['prop4'])
        
        self.play.setStyleSheet("background-color: lightblue;font-size:18px;font-family:Times New Roman;")
        self.bonnerep.setStyleSheet("background-color: lightsteelblue;font-size:18px;font-family:Times New Roman;")
        self.prop2.setStyleSheet("background-color: lightsteelblue;font-size:18px;font-family:Times New Roman;")
        self.prop3.setStyleSheet("background-color: lightsteelblue;font-size:18px;font-family:Times New Roman;")
        self.prop4.setStyleSheet("background-color: lightsteelblue;font-size:18px;font-family:Times New Roman;")
        
        self.next= QPushButton('Suivant')
        self.next.setStyleSheet("background-color: cornflowerblue;font-size:18px;font-family:Times New Roman;")
        self.maliste=[self.bonnerep, self.prop2, self.prop3, self.prop4]
        
        self.InitUI() #Appel de la fonction pour organser la fenetre 
        
    def InitUI(self):
        
        self.setWindowTitle(self.title)

        h_box = QHBoxLayout()
        h_box.addWidget(self.texte)
        
        h0_box = QHBoxLayout() #Organisation horizontale 
        h0_box.addWidget(self.play)
        
        h1_box = QHBoxLayout()
        h2_box = QHBoxLayout()
        h3_box = QHBoxLayout()
        
        self.gauche1= random.choice(self.maliste)
        h1_box.addWidget(self.gauche1)
        self.maliste.remove(self.gauche1)
        
        self.droite1= random.choice(self.maliste)
        h1_box.addWidget(self.droite1)
        self.maliste.remove(self.droite1)
        
        self.gauche2= random.choice(self.maliste)
        h2_box.addWidget(self.gauche2)
        self.maliste.remove(self.gauche2)
        
        self.droite2= random.choice(self.maliste)
        h2_box.addWidget(self.droite2)
        
        h3_box.addWidget(self.next)
        
        v_box = QVBoxLayout() #Organisation verticale 
        v_box.addLayout(h_box)
        v_box.addLayout(h0_box)
        v_box.addLayout(h1_box)
        v_box.addLayout(h2_box)
        v_box.addLayout(h3_box)
        
        self.setLayout(v_box)
        
        self.play.clicked.connect(self.play_music)
        self.bonnerep.clicked.connect(self.bonnerep_click)
        self.prop2.clicked.connect(self.prop2_click)
        self.prop3.clicked.connect(self.prop3_click)
        self.prop4.clicked.connect(self.prop4_click)
        self.next.clicked.connect(self.next_click)
        self.show()
    
    def play_music(self):
        self.music=str(quiz_question_musique[self.a]+'.mp3')
        playsound(self.music)
        
    def bonnerep_click(self):
        self.mydialog= QMainWindow()
        self.ui=Bonnerep.Window()
        self.ui.InitUI(self.mydialog)
        self.mydialog.show()
    
    def prop2_click(self):
        self.mydialog2= QMainWindow()
        self.ui=Mauvaiserep.Window()
        self.ui.InitUI(self.mydialog2)
        self.mydialog2.show()
    
    def prop3_click(self):
        self.mydialog3= QMainWindow()
        self.ui=Mauvaiserep.Window()
        self.ui.InitUI(self.mydialog3)
        self.mydialog3.show()
    
    def prop4_click(self):
        self.mydialog4= QMainWindow()
        self.ui=Mauvaiserep.Window()
        self.ui.InitUI(self.mydialog4)
        self.mydialog4.show()
    
    def next_click(self):
       self.mydialog5= QMainWindow()
       self.ui=Drapeaux.Window()
       self.ui.InitUI(self.mydialog5)
       self.mydialog5.show() 
    

        
if __name__=="__main__":
    App= QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec())