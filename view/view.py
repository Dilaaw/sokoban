"""
TODO
"""

from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QGridLayout, QVBoxLayout, QWidget, QPushButton, QMenu, QAction, QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QUrl, Qt,QDir
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist

class SokobanView(QMainWindow):
    """
    Cette classe permet d'afficher le jeu et de capturer les events
    """

    def __init__(self,model,controller):
        """
        """
        super().__init__()

        self.__model = model

        self.__controller = controller


        self.__music=QMediaPlaylist()
        self.__music.addMedia(QMediaContent(QUrl.fromLocalFile(QDir.current().absoluteFilePath("sound/genshin.wav"))))
        self.__music.setPlaybackMode(QMediaPlaylist.Loop)
        self.__volume=QMediaPlayer()
        self.__volume.setPlaylist(self.__music)
        self.__volume.setVolume(5)
        self.__volume.play()
        

        self.setWindowTitle("Sokoban Impact")
        self.statusBar().showMessage("Nombre de pas: 0")

        self.__window= QWidget()
        self.__window.setFixedSize(72*len(self.__model.getMap()[0]),72*len(self.__model.getMap())) # Taile du Widget = Taille image * colonne matrix, taille image * ligne
        self.setCentralWidget(self.__window)

        self.__grid_layout = QGridLayout() # Tableau de Layout qui va contenir et afficher les labels
        self.__grid_layout.setContentsMargins(0,0,0,0)
        self.__grid_layout.setSpacing(0)
        self.__window.setLayout(self.__grid_layout)
        self.__gridLayout = [] # Tableau de Label qu'on va parcourir pour acceder au label pour les modif
        self.__gridPerso = [] #[[label,label,label],[label,label,label]]
        
        for i in range(len(self.__model.getMap())):
            tmp = []
            tmpPerso =[]
            for j in range(len(self.__model.getMap()[0])):
                label = QLabel("")
                labelPerso = QLabel()
                tmp.append(label)
                tmpPerso.append(labelPerso)
                self.__grid_layout.addWidget(label,i,j) # Tableau de Label pour afficher
                self.__grid_layout.addWidget(labelPerso,i,j)
            self.__gridLayout.append(tmp)
            self.__gridPerso.append(tmpPerso)
        
        self.__winner = False

        self.__mur = QPixmap(QImage('texture/mur1').scaled(72,72))
        self.__sol = QPixmap(QImage('texture/sol1.png').scaled(72,72))
        self.__coffreBois = QPixmap(QImage('texture/coffre0.png').scaled(72,72))
        self.__coffreArgent = QPixmap(QImage('texture/coffre.png').scaled(72,72))
        self.__coffreGold = QPixmap(QImage('texture/coffre2.png').scaled(72,72))
        self.__coffreBoisV = QPixmap(QImage('texture/coffre0V.png').scaled(72,72))
        self.__coffreArgentV = QPixmap(QImage('texture/coffreV.png').scaled(72,72))
        self.__coffreGoldV = QPixmap(QImage('texture/coffre2V.png').scaled(72,72))
        self.__trou = QPixmap(QImage('texture/bois.png').scaled(72,72))
        self.__trou1 = QPixmap(QImage('texture/fer.png').scaled(72,72))
        self.__trou2 = QPixmap(QImage('texture/gold.png').scaled(72,72))

        self.__nbPas = 0

        menuBar = self.menuBar()
        gameMenu = QMenu("&Jeu", self)
        menuBar.addMenu(gameMenu)

        restartProgram = QAction(self)
        restartProgram.setText("&Restart")
        gameMenu.addAction(restartProgram)
        restartProgram.triggered.connect(self.restart)

        exitProgram = QAction(self)
        exitProgram.setText("&Quit")
        gameMenu.addAction(exitProgram)
        exitProgram.triggered.connect(self.close)

        if self.__model.getSpritePlayer() != None:
            self.__charac = self.__model.getSpritePlayer()
            self.__volume.stop()
            self.updateView()
        else:
            self.__charac=None
        
        screen = self.screen().geometry()
        self.move((screen.width()/2)-self.geometry().width()/2,(screen.height()/2)-self.geometry().height()/2) # Centre la fenêtre au milieu de l'écran


    def setNbCharac(self,nbCharac):
        """
        Methode qui intervient qu'au niveau 1 et qui set le sprite du perso choisit
        """
        if nbCharac == 0:
            self.__charac = QPixmap(QImage('texture/keqing').scaled(72,72))
        elif nbCharac == 1:
            self.__charac = QPixmap(QImage('texture/mona').scaled(72,72))
        elif nbCharac == 2:
            self.__charac = QPixmap(QImage('texture/venti').scaled(72,72))
        elif nbCharac == 3:
            self.__charac = QPixmap(QImage('texture/tagliatel').scaled(72,72))
        self.__model.setSpritePlayer(self.__charac)
        self.updateView()
            
    
    def addNbPas(self):
        """
        Methode qui ajoute un pas et l'affiche dans la statusBar (Bar en bas de la fenetre)
        """
        self.__nbPas += 1
        self.statusBar().showMessage("Nombre de pas: " + str(self.__nbPas))
    
    def keyPressEvent(self, event):
        """
        Cet event s'active à chaque touche appuyé
        Les touches q et fleche de Gauche font aller le personnage à gauche
        Les touches d et fleche de Droite font aller le personnage à droite
        Les touches z et fleche de Haut font aller le personnage à haut
        Les touches s et fleche de Bas font aller le personnage à bas
        """
        if(not self.__winner):
            key = event.key()
            if key == Qt.Key_Left or key == Qt.Key_Q:
                self.__controller.move("gauche")
                self.addNbPas()
            elif key == Qt.Key_Right or key == Qt.Key_D:
                self.__controller.move("droit")
                self.addNbPas()
            elif key == Qt.Key_Up or key == Qt.Key_Z:
                self.__controller.move("haut")
                self.addNbPas()
            elif key == Qt.Key_Down or key == Qt.Key_S:
                self.__controller.move("bas")
                self.addNbPas()

    def updateView(self):
        """
        Cette méthode actualise la vue

        On utilise la map pour afficher les sprites dans des QLabel qu'on ajoute aux bonnes coordonées dans le QGridLayout (Tableau de QLabel)
        (sol = 0, caisse = 3)
        puis on affiche le joueur par dessus aux coordonnées du joueur

        Cette methode est similaire à view mais n'actualise pas les murs et les trou qui ne change pas peut importe les actions du joueur
        """

        map = self.__model.getMap()
        x,y = self.__model.getPlayer()
        posTrou = self.__model.getTrou()

        for i in range(len(map)):
            for j in range(len(map[0])):

                if map[i][j] == 0 and (i,j) not in posTrou:
                    self.__gridLayout[i][j].setPixmap(self.__sol)
                
                elif map[i][j]==1:
                    self.__gridLayout[i][j].setPixmap(self.__mur)
                
                elif map[i][j] == 3:
                    self.__gridLayout[i][j].setPixmap(self.__coffreBois)
                elif map[i][j] == 4:
                    self.__gridLayout[i][j].setPixmap(self.__coffreArgent)
                elif map[i][j] == 5:
                    self.__gridLayout[i][j].setPixmap(self.__coffreGold)
                
                else:
                    self.__gridLayout[i][j].setPixmap(QPixmap())
                
                for pos,weight in posTrou.items():
                    if map[pos[0]][pos[1]] !=3 and map[pos[0]][pos[1]] !=4 and map[pos[0]][pos[1]] !=5:
                        if weight == 0:
                            self.__gridLayout[pos[0]][pos[1]].setPixmap(self.__trou)
                        elif weight == 1:
                            self.__gridLayout[pos[0]][pos[1]].setPixmap(self.__trou1)
                        elif weight == 2:
                            self.__gridLayout[pos[0]][pos[1]].setPixmap(self.__trou2)
                    elif map[pos[0]][pos[1]] == 3:
                        if weight == 0:
                            self.__gridLayout[pos[0]][pos[1]].setPixmap(self.__coffreBoisV)
                    elif map[pos[0]][pos[1]] == 4:
                        if weight == 1:
                            self.__gridLayout[pos[0]][pos[1]].setPixmap(self.__coffreArgentV)
                    elif map[pos[0]][pos[1]] == 5:
                        if weight == 2:
                            self.__gridLayout[pos[0]][pos[1]].setPixmap(self.__coffreGoldV)
                if i == x and j == y:
                    self.__gridPerso[i][j].setPixmap(self.__charac)
                else:
                    self.__gridPerso[i][j].setPixmap(QPixmap())
        
    
    def winner(self):
        self.__winner = True #Permet de blocker le keypressEvent
        if(self.__model.getLastLevel()):
            self.__winnerWindow = QWidget()
            conteneur = QVBoxLayout()
            label = QLabel()
            label.setPixmap(QPixmap(QImage('texture/win')))
            label.setAlignment(Qt.AlignCenter)
            conteneur.addWidget(label)
            quitButton = QPushButton("Quitter")
            conteneur.addWidget(quitButton)
            self.__winnerWindow.setLayout(conteneur)
            self.setCentralWidget(self.__winnerWindow)
            self.setFixedSize(self.geometry().width(),self.geometry().height())
            quitButton.clicked.connect(self.close)
        else:
            self.__winnerWindow = QWidget()
            conteneur = QVBoxLayout()
            label = QLabel()
            label.setPixmap(QPixmap(QImage('texture/win')))
            conteneur.addWidget(label)
            hConteneur = QHBoxLayout()
            nextButton= QPushButton("Niveau suivant")
            quitButton = QPushButton("Quitter")
            hConteneur.addWidget(nextButton)
            hConteneur.addWidget(quitButton)
            conteneur.addLayout(hConteneur)
            self.__winnerWindow.setLayout(conteneur)
            self.setCentralWidget(self.__winnerWindow)
            self.setFixedSize(self.geometry().width(),self.geometry().height())
            nextButton.clicked.connect(self.nextLevel)
            quitButton.clicked.connect(self.close)

    def nextLevel(self):
        self.__model.addLevel()
        self.__view = SokobanView(self.__model,self.__controller)
        self.__model.addView(self.__view)
        self.__controller.setView(self.__view)
        self.__view.show()
        self.close()
        
    
    def restart(self):
        if not self.__winner:
            self.__model.restart()
            self.__nbPas =0
            self.updateView()
        else:
            self.__model.restart()
            self.__view = SokobanView(self.__model,self.__controller)
            self.__model.addView(self.__view)
            self.__controller.setView(self.__view)
            self.__view.show()
            self.close()