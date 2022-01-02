class SokobanGrid:
    """
    Cette classe sert à stocker les variables du jeu tel que la map et la position du joueur
    """
    def __init__(self):
        """
        On initialise la map et la position du joueur et la view
        """
        self.__level = 0
        self.__map = [["","",1 ,1 ,1 ,1 ,1 ,""],
        [1 ,1 ,1 ,0 ,0 ,0 ,1 ,""],
        [1, 0, 0, 3, 3, 0, 1 ,""],
        [1 ,1 ,1 ,0 ,0 ,0 ,1 ,""],
        [1, 0, 1, 1, 3, 0, 1 ,1],
        [1 ,0 ,0 ,0 ,3 ,0 ,0 ,1 ],
        [1, 0, 0, 0, 0, 0, 0 ,1 ],
        [1, 1, 1, 1, 1, 1, 1 ,1 ]] # 1=mur 0 = pas mur "" = hors map 3 = caisse(bois) 4 = caisse(fer) 5 = caisse(or)
        
        self.__player = (2,2)
        self.__trou = {(6,6):1}
        
        
        self.__view = None

        self.__spritePlayer = None
        self.__lastLevel = False

    def getLastLevel(self):
        return self.__lastLevel
    
    def setSpritePlayer(self,sprite):
        self.__spritePlayer=sprite

    def getSpritePlayer(self):
        return self.__spritePlayer

    def addView(self,view):
        """
        On ajoute une view
        """
        self.__view = view

    def restart(self):

        if self.__level == 0:
            self.__map = [["","",1 ,1 ,1 ,1 ,1 ,""],
            [1 ,1 ,1 ,0 ,0 ,0 ,1 ,""],
            [1, 0, 0, 3, 3, 0, 1 ,""],
            [1 ,1 ,1 ,0 ,0 ,0 ,1 ,""],
            [1, 0, 1, 1, 3, 0, 1 ,1],
            [1 ,0 ,0 ,0 ,3 ,0 ,0 ,1 ],
            [1, 0, 0, 0, 0, 0, 0 ,1 ],
            [1, 1, 1, 1, 1, 1, 1 ,1 ]] # 1=mur 0 = pas mur "" = hors map 3 = caisse(bois) 4 = caisse(fer) 5 = caisse(or)
            
            self.__player = (2,2)
            self.__trou = {(6,6):1}

        elif self.__level == 1:
             self.__map =[[1 ,1 ,1 ,1 ,1 ,1 ,1 ,"",""],
             [1 ,0 ,0 ,0 ,0 ,0 ,1 ,"",""],
             [1, 0, 5, 0, 0, 0, 1 ,"",""],
             [1 ,1 ,0 ,1 ,1 ,0 ,1 ,"",""],
             [1, 0, 1, 1, 0, 0, 1 ,1 ,1],
             [1 ,0 ,0 ,0 ,5 ,0 ,0 ,0 ,1],
             [1, 0, 0, 0, 0, 0, 0 ,0 ,1],
             [1, 1, 1, 1, 1, 1, 1 ,1 ,1]]
             self.__player = (1,2)
             self.__trou = {(6,6):2,(6,2):2}
             
        elif self.__level == 2:
             self.__map =[[1 ,1 ,1 ,1 ,1 ,1 ,1 ,"",""],
             [1 ,0 ,0 ,0 ,0 ,0 ,1 ,"",""],
             [1, 0, 3, 0, 0, 0, 1 ,"",""],
             [1 ,1 ,0 ,1 ,1 ,0 ,1 ,"",""],
             [1, 0, 0, 0, 0, 0, 1 ,1 ,1],
             [1 ,1 ,1 ,3 ,3 ,0 ,0 ,0 ,1],
             [1, 0, 0, 0, 0, 1, 0 ,0 ,1],
             [1, 1, 1, 1, 1, 1, 1 ,1 ,1]]
             self.__player = (1,2)
             self.__trou = {(5,6):0,(6,2):1}

        elif self.__level == 3:
            self.__map =[["","" ,1 ,1 ,1 ,1 ,1,"",""],
            [1, 1, 1, 0, 0, 0, 1, "", ""],
            [1, 0, 0, 4, 0, 0, 1, "", ""],
            [1, 1, 1, 0, 4, 0, 1, "", ""],
            [1, 0, 1, 1, 4, 0, 1, "", ""],
            [1, 0, 1, 0, 0, 0, 1, 1, ""],
            [1, 4, 0, 4, 4, 4, 0, 1, ""],
            [1, 0, 0, 0, 0, 0, 0, 1, ""],
            [1, 1, 1, 1, 1, 1, 1, 1, ""]]
            self.__player = (2,2)
            self.__trou = {(2,1):1,(3,5):1,(4,1):1,(5,4):1,(6,6):1,(7,4):1}

        elif self.__level == 4 :
            self.__map = [["","","" ,1 ,1 ,1 ,1 ,1,"","",""],
            [1 ,1 ,1 ,1 ,0 ,0 ,0 ,1,"","",""],
            [1, 0, 0, 1, 3, 0, 0 ,1,1,1,1],
            [1 ,0 ,3 ,3 ,0 ,0 ,0 ,0,0,0,1],
            [1, 0, 0, 0, 1, 3, 0 ,3,1,0,1],
            [1, 1, 1, 0, 1, 0, 0, 0,1,0,1],
            ["", 1, 0, 0, 1, 1, 1 ,1,1,0,1],
            ["", 1, 0, 0, 0, 0, 0,0,0,0,1],
            ["", 1, 1, 1, 1, 1, 1 ,1,1,1,1]] # 1=mur 0 = pas mur "" = hors map 3 = caisse(bois) 4 = caisse(fer) 5 = caisse(or)
        
            
            self.__player = (2,5)
            self.__trou = {(7,5):1,(7,6):0,(7,7):1} # 0 : bois, 1 : argent, 2 : or
        
        elif self.__level == 5 :
            self.__map = [[1,1,1 ,1 ,1 ,1 ,1 ,1,1,1,1],
            [1,0,0 ,0 ,0 ,0 ,0 ,1,0,0,1],
            [1,0,4 , 1, 1, 0, 3 ,0, 0,0,1],
            [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 1, 5, 1, 0, 0, 0, 1, 0, 1, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0 ,0,0,0,1],
            [1, 0, 0, 1, 1, 1, 1 ,1,0,0,1],
            [1, 1, 1, 1, "", "", "" ,1,1,1,1]] # 1=mur 0 = pas mur "" = hors map 3 = caisse(bois) 4 = caisse(fer) 5 = caisse(or)
            
            self.__player = (1,5)
            self.__trou = {(3,4):0,(4,4):2,(3,6):1} # 0 : bois, 1 : argent, 2 : or

    def addLevel(self):
        self.__level+=1
        if self.__level == 1:
             self.__map =[[1 ,1 ,1 ,1 ,1 ,1 ,1 ,"",""],
             [1 ,0 ,0 ,0 ,0 ,0 ,1 ,"",""],
             [1, 0, 5, 0, 0, 0, 1 ,"",""],
             [1 ,1 ,0 ,1 ,1 ,0 ,1 ,"",""],
             [1, 0, 1, 1, 0, 0, 1 ,1 ,1],
             [1 ,0 ,0 ,0 ,5 ,0 ,0 ,0 ,1],
             [1, 0, 0, 0, 0, 0, 0 ,0 ,1],
             [1, 1, 1, 1, 1, 1, 1 ,1 ,1]]
             self.__player = (1,2)
             self.__trou = {(6,6):2,(6,2):2}

        elif self.__level == 2:
             self.__map =[[1 ,1 ,1 ,1 ,1 ,1 ,1 ,"",""],
             [1 ,0 ,0 ,0 ,0 ,0 ,1 ,"",""],
             [1, 0, 3, 0, 0, 0, 1 ,"",""],
             [1 ,1 ,0 ,1 ,1 ,0 ,1 ,"",""],
             [1, 0, 0, 0, 0, 0, 1 ,1 ,1],
             [1 ,1 ,1 ,3 ,3 ,0 ,0 ,0 ,1],
             [1, 0, 0, 0, 0, 1, 0 ,0 ,1],
             [1, 1, 1, 1, 1, 1, 1 ,1 ,1]]
             self.__player = (1,2)
             self.__trou = {(5,6):0,(6,2):1}

        elif self.__level == 3:
            self.__map =[["","" ,1 ,1 ,1 ,1 ,1,"",""],
            [1, 1, 1, 0, 0, 0, 1, "", ""],
            [1, 0, 0, 4, 0, 0, 1, "", ""],
            [1, 1, 1, 0, 4, 0, 1, "", ""],
            [1, 0, 1, 1, 4, 0, 1, "", ""],
            [1, 0, 1, 0, 0, 0, 1, 1, ""],
            [1, 4, 0, 4, 4, 4, 0, 1, ""],
            [1, 0, 0, 0, 0, 0, 0, 1, ""],
            [1, 1, 1, 1, 1, 1, 1, 1, ""]]
            self.__player = (2,2)
            self.__trou = {(2,1):1,(3,5):1,(4,1):1,(5,4):1,(6,6):1,(7,4):1}

        elif self.__level == 4 :
            self.__map = [["","","" ,1 ,1 ,1 ,1 ,1,"","",""],
            [1 ,1 ,1 ,1 ,0 ,0 ,0 ,1,"","",""],
            [1, 0, 0, 1, 3, 0, 0 ,1,1,1,1],
            [1 ,0 ,3 ,3 ,0 ,0 ,0 ,0,0,0,1],
            [1, 0, 0, 0, 1, 3, 0 ,3,1,0,1],
            [1, 1, 1, 0, 1, 0, 0, 0,1,0,1],
            ["", 1, 0, 0, 1, 1, 1 ,1,1,0,1],
            ["", 1, 0, 0, 0, 0, 0,0,0,0,1],
            ["", 1, 1, 1, 1, 1, 1 ,1,1,1,1]] # 1=mur 0 = pas mur "" = hors map 3 = caisse(bois) 4 = caisse(fer) 5 = caisse(or)
            
            self.__player = (2,5)
            self.__trou = {(7,5):1,(7,6):0,(7,7):1} # 0 : bois, 1 : argent, 2 : or
        
        elif self.__level == 5 :
            self.__map = [[1,1,1 ,1 ,1 ,1 ,1 ,1,1,1,1],
            [1,0,0 ,0 ,0 ,0 ,0 ,1,0,0,1],
            [1,0,4 , 1, 1, 0, 3 ,0, 0,0,1],
            [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 1, 5, 1, 0, 0, 0, 1, 0, 1, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0 ,0,0,0,1],
            [1, 0, 0, 1, 1, 1, 1 ,1,0,0,1],
            [1, 1, 1, 1, "", "", "" ,1,1,1,1]] # 1=mur 0 = pas mur "" = hors map 3 = caisse(bois) 4 = caisse(fer) 5 = caisse(or)
            
            self.__player = (1,5)
            self.__trou = {(3,4):0,(4,4):2,(3,6):1} # 0 : bois, 1 : argent, 2 : or
            self.__lastLevel = True
    

    def getMap(self):
        """
        Getter de la map (int[][])
        """
        return self.__map
    
    def getPosMap(self,x,y):
        return self.__map[x][y]

    def getPlayer(self):
        """
        Getter de la position du joueur (x,y)
        """
        return self.__player

    def getTrou(self):
        """
        Getter de la position des trou
        """
        return self.__trou
    
    def setPlayer(self,l,c):
        """
        Permet de changer la position du joueur
        puis update la view
        """
        self.__player=(l,c)
        self.__view.updateView()

    def setMap(self,l,c,n):
        """
        Permet de changer un élément de la map
        (vide = 0, mur = 1, caisse = 3, trou = 4)
        l = ligne
        c = colonne
        n = le nouvel élément de cette case
        """
        self.__map[l][c]=n