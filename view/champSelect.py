from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QMainWindow, QWidget, QPushButton,QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QDir, QUrl, Qt

class champSelect(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__view= None
        self.setWindowTitle("Sokoban Impact")
        screen = self.screen().availableGeometry()
        self.move(screen.width()/4,screen.height()/4)
        conteneur = QWidget() # Main Widget
        conteneurText = QVBoxLayout() 
        miniConteneur = QHBoxLayout()
        text = QLabel("Choisissez votre personnage !")
        text.setAlignment(Qt.AlignCenter) # Aligner le text
        conteneurText.addWidget(text)
        
        charac1 = QVBoxLayout()

        self.__img = QPixmap(QImage('texture/keqingPreview'))

        conteneurImage = QLabel()

        conteneurImage.setPixmap(self.__img)

        bouton = QPushButton("Keqing")

        charac1.addWidget(conteneurImage)

        charac1.addWidget(bouton)

        #############################################

        charac2 = QVBoxLayout()

        self.__img2 = QPixmap(QImage('texture/monaPreview'))

        conteneurImage2 = QLabel()

        conteneurImage2.setPixmap(self.__img2)

        bouton2 = QPushButton("Mona")

        charac2.addWidget(conteneurImage2)

        charac2.addWidget(bouton2)

        #############################################
        charac3 = QVBoxLayout()

        self.__img3 = QPixmap(QImage('texture/ventiPreview'))

        conteneurImage3 = QLabel()

        conteneurImage3.setPixmap(self.__img3)

        bouton3 = QPushButton("Venti")

        charac3.addWidget(conteneurImage3)

        charac3.addWidget(bouton3)

        #############################################
        charac4 = QVBoxLayout()

        self.__img4 = QPixmap(QImage('texture/tagliatelPreview'))

        conteneurImage4 = QLabel()

        conteneurImage4.setPixmap(self.__img4)

        bouton4 = QPushButton("Tartaglia")

        charac4.addWidget(conteneurImage4)

        charac4.addWidget(bouton4)

        #############################################

        miniConteneur.addLayout(charac1)
        miniConteneur.addLayout(charac2)
        miniConteneur.addLayout(charac3)
        miniConteneur.addLayout(charac4)
        conteneurText.addLayout(miniConteneur)
        conteneur.setLayout(conteneurText) # Set le Layout du QWidget

        self.setCentralWidget(conteneur)

        bouton.clicked.connect(lambda x:self.play(0))
        bouton2.clicked.connect(lambda x:self.play(1))
        bouton3.clicked.connect(lambda x:self.play(2))
        bouton4.clicked.connect(lambda x:self.play(3))
    
    def play(self,perso):
        if perso == 0:
            self.__music=QMediaPlaylist()
            self.__music.addMedia(QMediaContent(QUrl.fromLocalFile(QDir.current().absoluteFilePath("sound/Keqing.wav"))))
            self.__music.setPlaybackMode(QMediaPlaylist.Sequential)
            self.__volume=QMediaPlayer()
            self.__volume.setPlaylist(self.__music)
            self.__volume.setVolume(5)
            self.__volume.play()
        elif perso == 1:
            self.__music=QMediaPlaylist()
            self.__music.addMedia(QMediaContent(QUrl.fromLocalFile(QDir.current().absoluteFilePath("sound/Mona.wav"))))
            self.__music.setPlaybackMode(QMediaPlaylist.Sequential)
            self.__volume=QMediaPlayer()
            self.__volume.setPlaylist(self.__music)
            self.__volume.setVolume(5)
            self.__volume.play()
        elif perso == 2:
            self.__music=QMediaPlaylist()
            self.__music.addMedia(QMediaContent(QUrl.fromLocalFile(QDir.current().absoluteFilePath("sound/Venti.wav"))))
            self.__music.setPlaybackMode(QMediaPlaylist.Sequential)
            self.__volume=QMediaPlayer()
            self.__volume.setPlaylist(self.__music)
            self.__volume.setVolume(5)
            self.__volume.play()
        elif perso == 3:
            self.__music=QMediaPlaylist()
            self.__music.addMedia(QMediaContent(QUrl.fromLocalFile(QDir.current().absoluteFilePath("sound/Tartaglia.wav"))))
            self.__music.setPlaybackMode(QMediaPlaylist.Sequential)
            self.__volume=QMediaPlayer()
            self.__volume.setPlaylist(self.__music)
            self.__volume.setVolume(5)
            self.__volume.play()

        self.__view.setNbCharac(perso) 
        self.__view.show()
        self.close()
    
    def setView(self,view):
        self.__view = view