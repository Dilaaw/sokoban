"""
Main du projet Sokoban du Groupe de BG
"""

from view.startScreen import startScreen
from model.grid import SokobanGrid
from controller.ctrlMouvement import SokobanController
import sys
from view.view import SokobanView
from PyQt5.QtWidgets import QApplication

"""
Import les MCV
"""

app = QApplication(sys.argv)  #Creer une Application

screen = startScreen() # Créer l'Ecran d'accueil

model = SokobanGrid() #Créer le Model 
controller = SokobanController() #Créer le controller
view = SokobanView(model,controller) #Créer la view

model.addView(view) #add une view au model


screen.setView(view) # Set la view à l'écran d'accueil

controller.setModel(model) # set le model et la view au controller
controller.setView(view)

screen.show() #Show la view

sys.exit(app.exec_())