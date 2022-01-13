# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 18:54:01 2021

@author: yonau
"""

import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,QLabel,
                             QApplication, QMainWindow, QWidget, QTextEdit, QDialog)
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from questions import quiz_culture_propositions
from questions import quiz_culture
import random
import Bonnerep
import Mauvaiserep
import Musique_titres
liste_culture=[1,2,3]


class Window(QWidget):
    """Choisit aléatoirement un drapeau parmi ceux enregistrés
    et réagit en fonction de l'exactitude de la réponse.
    La réponse sera le pays correspondant au drapeau"""
    
    def __init__(self):
        super().__init__() #Constructeur 
        
        #choix aléatoire de la musique 
        self.a= random.choice(liste_culture)
        self.question= quiz_culture[self.a]
        
        self.setStyleSheet("background-color: mistyrose;")
        
        #titre de la fenetre 
        self.title = "QUIZ - Residence AMARAGGI"
        
        # Geometrie et place de la fenetre a l'ouverture 
        self.setGeometry(137,62,697,392)
        
        #a=quiz_musique_titre[1]['bonnerep']
        self.texte = QLabel(self.question)

        # setting font and size
        self.texte.setFont(QFont('Times', 20))
        
        self.next= QPushButton('Suivant')
        self.next.setStyleSheet("background-color: coral;font-size:18px;font-family:Times New Roman;")
        
        self.grid = QGridLayout()
        self.grid.addWidget(self.texte,2,5)
        
        self.intru=QPushButton(quiz_culture_propositions[self.a]['intru'])
        self.prop2=QPushButton(quiz_culture_propositions[self.a]['prop2'])
        self.prop3=QPushButton(quiz_culture_propositions[self.a]['prop3'])
        self.prop4=QPushButton(quiz_culture_propositions[self.a]['prop4'])
        self.prop5=QPushButton(quiz_culture_propositions[self.a]['prop5'])
        self.prop6=QPushButton(quiz_culture_propositions[self.a]['prop6'])
        self.prop7=QPushButton(quiz_culture_propositions[self.a]['prop7'])
        
        #self.prop2.setStyleSheet("background-color: thistle;font-size:18px;font-family:Times New Roman;")
        #self.bonnerep.setStyleSheet("background-color: thistle;font-size:18px;font-family:Times New Roman;")
       
        self.maliste=[self.intru, self.prop2, self.prop3, self.prop4, self.prop5, self.prop6, self.prop7]
        self.un= random.choice(self.maliste)
        self.grid.addWidget(self.un,0,0)
        self.maliste.remove(self.un)
        
        self.deux= random.choice(self.maliste)
        self.grid.addWidget(self.deux,1,0)
        self.maliste.remove(self.deux)
        
        self.trois= random.choice(self.maliste)
        self.grid.addWidget(self.trois,2,0)
        self.maliste.remove(self.trois)
        
        self.quatre= random.choice(self.maliste)
        self.grid.addWidget(self.quatre,3,0)
        self.maliste.remove(self.quatre)
        
        self.cinq= random.choice(self.maliste)
        self.grid.addWidget(self.cinq,4,0)
        self.maliste.remove(self.cinq)
        
        self.six= random.choice(self.maliste)
        self.grid.addWidget(self.six,2,0)
        self.maliste.remove(self.six)
        
        self.sept= random.choice(self.maliste)
        self.grid.addWidget(self.sept,5,0)
        self.maliste.remove(self.sept)
        
        self.grid.addWidget(self.next,6,0)
        self.setLayout(self.grid)
        
        self.InitUI() #Appel de la fonction pour organser la fenetre 
        
    def InitUI(self):
        
        self.setWindowTitle(self.title)
        
        self.intru.setStyleSheet("background-color: lightcoral;font-size:18px;font-family:Times New Roman;")
        self.prop2.setStyleSheet("background-color: lightcoral;font-size:18px;font-family:Times New Roman;")
        self.prop3.setStyleSheet("background-color: lightcoral;font-size:18px;font-family:Times New Roman;")
        self.prop4.setStyleSheet("background-color: lightcoral;font-size:18px;font-family:Times New Roman;")
        self.prop5.setStyleSheet("background-color: lightcoral;font-size:18px;font-family:Times New Roman;")
        self.prop6.setStyleSheet("background-color: lightcoral;font-size:18px;font-family:Times New Roman;")
        self.prop7.setStyleSheet("background-color: lightcoral;font-size:18px;font-family:Times New Roman;")
        
        self.intru.clicked.connect(self.intru_click)
        self.prop2.clicked.connect(self.prop2_click)
        self.prop3.clicked.connect(self.prop3_click)
        self.prop4.clicked.connect(self.prop4_click)
        self.prop5.clicked.connect(self.prop5_click)
        self.prop6.clicked.connect(self.prop6_click)
        self.prop7.clicked.connect(self.prop7_click)
        self.next.clicked.connect(self.suivant)
        self.show()
        # self.next.clicked.connect(self.commence)
    def intru_click(self):
        self.intru.setStyleSheet("background-color: red;font-size:18px;font-family:Times New Roman;")
    
    def prop2_click(self):
        self.prop2.setStyleSheet("background-color: limegreen;font-size:18px;font-family:Times New Roman;")
    
    def prop3_click(self):
        self.prop3.setStyleSheet("background-color: limegreen;font-size:18px;font-family:Times New Roman;")

    def prop4_click(self):
        self.prop4.setStyleSheet("background-color: limegreen;font-size:18px;font-family:Times New Roman;")
    
    def prop5_click(self):
        self.prop5.setStyleSheet("background-color: limegreen;font-size:18px;font-family:Times New Roman;")
    
    def prop6_click(self):
        self.prop6.setStyleSheet("background-color: limegreen;font-size:18px;font-family:Times New Roman;")
    
    def prop7_click(self):
        self.prop7.setStyleSheet("background-color: limegreen;font-size:18px;font-family:Times New Roman;")
    
    def suivant(self):
        self.mydialog= QMainWindow()
        self.ui=Musique_titres.Window()
        self.ui.InitUI(self.mydialog)
        self.mydialog.show()
        
if __name__=="__main__":
    App= QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec())