# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 10:56:29 2021

@author: yonau
"""

import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,QLabel,
                             QApplication, QMainWindow, QWidget, QTextEdit, QDialog)
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from questions import quiz_drapeaux
from questions import quiz_drapeaux_propositions
import random
from playsound import playsound
import Bonnerep
import Mauvaiserep
import Proverbes
liste_drapeaux=[1,2,3,4,5,6,7,8,9,10,11]


class Window(QWidget):
    """Choisit aléatoirement un drapeau parmi ceux enregistrés
    et réagit en fonction de l'exactitude de la réponse.
    La réponse sera le pays correspondant au drapeau"""
    
    def __init__(self):
        super().__init__() #Constructeur 
        
        #choix aléatoire de la musique 
        self.a= random.choice(liste_drapeaux)
        self.drapeau= quiz_drapeaux[self.a]
        
        self.setStyleSheet("background-color: blanchedalmond;")
        
        #titre de la fenetre 
        self.title = "QUIZ - Residence AMARAGGI"
        
        # Geometrie et place de la fenetre a l'ouverture 
        self.setGeometry(137,62,697,392)
        
        #a=quiz_musique_titre[1]['bonnerep']
        self.texte = QLabel("A quel pays appartient ce drapeau ?")

        # setting font and size
        self.texte.setFont(QFont('Times', 20))
        
        self.image = QPixmap(str(self.drapeau))
        
        self.label = QLabel()
        self.label.setPixmap(self.image)
        
        self.next= QPushButton('Suivant')
        self.next.setStyleSheet("background-color: salmon;font-size:18px;font-family:Times New Roman;")
        
        self.grid = QGridLayout()
        self.grid.addWidget(self.texte,0,1)
        self.grid.addWidget(self.label,1,1)
        
        #self.play.setStyleSheet("QPushButton{border-image: url(C:\\Users\\yonau\\Desktop\\EPISEN\\S2\\ECUE 261 Stage\\EHPAD\\play2.png);")
        self.bonnerep=QPushButton(quiz_drapeaux_propositions[self.a]['bonnerep'])
        self.prop2=QPushButton(quiz_drapeaux_propositions[self.a]['prop2'])
        
        self.prop2.setStyleSheet("background-color: peachpuff;font-size:18px;font-family:Times New Roman;")
        self.bonnerep.setStyleSheet("background-color: peachpuff;font-size:18px;font-family:Times New Roman;")
       
        self.maliste=[self.bonnerep, self.prop2]
        self.gauche= random.choice(self.maliste)
        
        self.grid.addWidget(self.gauche,2,0)
        self.maliste.remove(self.gauche)
        self.droite= random.choice(self.maliste)
        self.grid.addWidget(self.droite,2,2)
        self.grid.addWidget(self.next,3,1)
        self.setLayout(self.grid)
        
        self.InitUI() #Appel de la fonction pour organser la fenetre 
        
    def InitUI(self):
        
        self.setWindowTitle(self.title)

        self.bonnerep.clicked.connect(self.bonnerep_click)
        self.prop2.clicked.connect(self.prop2_click)
        self.next.clicked.connect(self.next_click)
        self.show()
        
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
    
    def next_click(self):
       self.mydialog3= QMainWindow()
       self.ui=Proverbes.Window()
       self.ui.InitUI(self.mydialog3)
       self.mydialog3.show() 

        
if __name__=="__main__":
    App= QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec())