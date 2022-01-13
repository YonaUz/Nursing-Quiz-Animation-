# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 13:53:47 2021

@author: yonau
"""

import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,QLabel,
                             QApplication, QMainWindow, QWidget, QTextEdit, QDialog)
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from questions import quiz_proverbes 
from questions import quiz_proverbes_propositions
import random
from playsound import playsound
import Bonnerep
import Mauvaiserep
import Musique_chanteurs
liste_prov=[1,2,3,4,5,6,7,8,9,10,11]

class Window(QWidget):
    """Choisit aléatoirement une musique parmi celles enregistrées 
    et réagit en fonction de l'exactitude de la réponse.
    La réponse sera le proverbe complété """
    
    
    def __init__(self):
        super().__init__() #Constructeur 
        
        #choix aléatoire de la musique 
        self.a= random.choice(liste_prov)
        self.proverbe= quiz_proverbes[self.a]
        
        #titre de la fenetre 
        self.title = "QUIZ - Residence AMARAGGI"
        
        # Geometrie et place de la fenetre a l'ouverture 
        self.setGeometry(137,62,697,392)
        
        self.setStyleSheet("background-color: lavenderblush;")
        
        self.texte = QLabel("Complétez le proverbe suivant: ")
        self.texte.setAlignment(QtCore.Qt.AlignCenter) #alignement au centre 
        self.texte.setStyleSheet("background-color: lavenderblush;font-size:18px;font-family:Times New Roman;")
        # setting font and size
        self.texte.setFont(QFont('Times', 20))
        
        self.citation = QLabel(self.proverbe)
        self.citation.setStyleSheet("background-color: lavenderblush;font-size:18px;font-family:Times New Roman;")
        #self.play.setStyleSheet("background-image : url(C:\\Users\\yonau\\Desktop\\EPISEN\\S2\\ECUE 261 Stage\\EHPAD\\play-button.png);")
        #self.play.setStyleSheet("QPushButton{border-image: url(C:\\Users\\yonau\\Desktop\\EPISEN\\S2\\ECUE 261 Stage\\EHPAD\\play2.png);")
        self.bonnerep=QPushButton(quiz_proverbes_propositions[self.a]['bonnerep'])
        self.prop2=QPushButton(quiz_proverbes_propositions[self.a]['prop2'])
        self.prop3=QPushButton(quiz_proverbes_propositions[self.a]['prop3'])
        self.prop4=QPushButton(quiz_proverbes_propositions[self.a]['prop4'])
        
        self.bonnerep.setStyleSheet("background-color: lightpink;font-size:18px;font-family:Times New Roman;")
        self.prop2.setStyleSheet("background-color: lightpink;font-size:18px;font-family:Times New Roman;")
        self.prop3.setStyleSheet("background-color: lightpink;font-size:18px;font-family:Times New Roman;")
        self.prop4.setStyleSheet("background-color: lightpink;font-size:18px;font-family:Times New Roman;")
        
        self.next= QPushButton('Suivant')
        self.next.setStyleSheet("background-color: hotpink;font-size:18px;font-family:Times New Roman;")
        
        self.maliste=[self.bonnerep, self.prop2, self.prop3, self.prop4]
        
        self.InitUI() #Appel de la fonction pour organser la fenetre 
        
    def InitUI(self):
        
        self.setWindowTitle(self.title)

        h_box = QHBoxLayout()
        h_box.addWidget(self.texte)
        
        h0_box = QHBoxLayout() #Organisation horizontale 
        h0_box.addWidget(self.citation)
        
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
        
        self.bonnerep.clicked.connect(self.bonnerep_click)
        self.prop2.clicked.connect(self.prop2_click)
        self.prop3.clicked.connect(self.prop3_click)
        self.prop4.clicked.connect(self.prop4_click)
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
       self.mydialog3= QMainWindow()
       self.ui=Musique_chanteurs.Window()
       self.ui.InitUI(self.mydialog3)
       self.mydialog3.show() 


        
if __name__=="__main__":
    App= QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec())