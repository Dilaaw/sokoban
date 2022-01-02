from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QWidget, QPushButton,QLabel
from PyQt5.QtGui import QPainter, QPen, QPixmap, QImage, QIcon,QBrush
from PyQt5.QtCore import QSize, Qt
from view.champSelect import champSelect

class startScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__view= None 
        self.setWindowTitle("Sokoban Impact")
        screen = self.screen().availableGeometry()
        self.move((screen.width()/2)-self.width()/4,screen.height()/2-(self.height()/2)) # Centrer la Window
        conteneur = QWidget() # Widget conteneur de TOUT
        boxV = QVBoxLayout() # Box Vertical
        self.__img = QPixmap(QImage('texture/jeu')) #Image Sokoban Impact
        conteneurImage = QLabel()
        conteneurImage.setPixmap(self.__img)
        bouton = QPushButton("Jouer")
        boxV.addWidget(conteneurImage) #Ajout de l'image PUIS du bouton
        boxV.addWidget(bouton)
        conteneur.setLayout(boxV) #Ajout de la box vertical dans le conteneur
        self.setCentralWidget(conteneur) # Widget est l'objet pricipal de la page
        bouton.clicked.connect(self.playChampSelect)
        
    
    def playChampSelect(self):
        self.__champSelect = champSelect()
        self.__champSelect.setView(self.__view)
        self.__champSelect.show()
        self.close()

    def setView(self,view):
        self.__view = view