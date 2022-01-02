"""
TODO
"""

class SokobanController:
    """
    Cette classe gère les déplacements du joueur, les regles du jeu et les conditions de victoire
    """

    def __init__(self):
        """
        Dans ce construsteur on initialise le model et la view ainsi qu'un boolean qui servira à savoir si le joueur à gagner (condition de victoire TODO)
        """
        self.__model = None
        self.__view = None
    
    def setModel(self, model):
        """
        set le model
        """
        self.__model = model

    def setView(self, view):
        """
        set la view
        """
        self.__view = view

    def move(self, direction):
        """
        Cette méthode gère les déplacements du joueur
        (vide = 0, mur = 1, caisse = 3, trou = 4)
        On effectue pour chaque direction donnée par le keyPressEvent:
            Le joueur peut se déplacer si il n'y a pas de mur
            Le joueur peut se déplacer et déplacer la caisse si il y a une caisse dans la direction ou il va ET si derrière il n'y a pas de mur
            Dans les autres cas le joueur ne se déplace pas
        """
        map = self.__model.getMap()
        l,c = self.__model.getPlayer()
        if direction == "haut":
            assert l>0
            if map[l-1][c] == 0:
                self.__model.setPlayer(l-1,c)
            elif map[l-1][c] == 3:
                assert l>1
                if map[l-2][c] == 0:
                    self.__model.setMap(l-2,c,3) # move la caisse si rien derriere
                    self.__model.setMap(l-1,c,0)
                    self.__model.setPlayer(l-1,c)
                elif map[l-2][c] == 3:
                    self.__model.setMap(l-2,c,4) # move la caisse si rien derriere
                    self.__model.setMap(l-1,c,0)
                    self.__model.setPlayer(l-1,c)
                
                self.verifWin()
            
            elif map[l-1][c] == 4:
                assert l>1
                if map[l-2][c] == 0:
                    self.__model.setMap(l-2,c,4) # move la caisse si rien derriere
                    self.__model.setMap(l-1,c,0)
                    self.__model.setPlayer(l-1,c)
                elif map[l-2][c] == 4:
                    self.__model.setMap(l-2,c,5) # move la caisse si rien derriere
                    self.__model.setMap(l-1,c,0)
                    self.__model.setPlayer(l-1,c)
                self.verifWin()
            elif map[l-1][c] == 5:
                assert l>1
                if map[l-2][c] == 0:
                    self.__model.setMap(l-2,c,5) # move la caisse si rien derriere
                    self.__model.setMap(l-1,c,0)
                    self.__model.setPlayer(l-1,c)
                self.verifWin()
        
        elif direction == "droit":
            assert c+1<= len(map[0])
            if map[l][c+1] == 0:
                self.__model.setPlayer(l,c+1)
            elif map[l][c+1] == 3:
                assert c+2<= len(map[0])
                if map[l][c+2] == 0:
                    self.__model.setMap(l,c+2,3) # move la caisse si rien derriere
                    self.__model.setMap(l,c+1,0)
                    self.__model.setPlayer(l,c+1)
                elif map[l][c+2] == 3:
                    self.__model.setMap(l,c+2,4) # move la caisse si rien derriere
                    self.__model.setMap(l,c+1,0)
                    self.__model.setPlayer(l,c+1)
                self.verifWin()
            elif map[l][c+1] == 4:
                assert c+2<= len(map[0])
                if map[l][c+2] == 0:
                    self.__model.setMap(l,c+2,4) # move la caisse si rien derriere
                    self.__model.setMap(l,c+1,0)
                    self.__model.setPlayer(l,c+1)
                elif map[l][c+2] == 4:
                    self.__model.setMap(l,c+2,5) # move la caisse si rien derriere
                    self.__model.setMap(l,c+1,0)
                    self.__model.setPlayer(l,c+1)
                self.verifWin()
            elif map[l][c+1] == 5:
                assert c+2<= len(map[0])
                if map[l][c+2] == 0:
                    self.__model.setMap(l,c+2,5) # move la caisse si rien derriere
                    self.__model.setMap(l,c+1,0)
                    self.__model.setPlayer(l,c+1)
                self.verifWin()
        

        elif direction == "bas":
            assert l+1<= len(map)
            if map[l+1][c] == 0:
                self.__model.setPlayer(l+1,c)
            elif map[l+1][c] == 3:
                assert l+2<= len(map)
                if map[l+2][c] == 0:
                    self.__model.setMap(l+2,c,3) # move la caisse si rien derriere
                    self.__model.setMap(l+1,c,0)
                    self.__model.setPlayer(l+1,c)
                elif map[l+2][c] == 3:
                    self.__model.setMap(l+2,c,4) # move la caisse si rien derriere
                    self.__model.setMap(l+1,c,0)
                    self.__model.setPlayer(l+1,c)
                self.verifWin()
            elif map[l+1][c] == 4:
                assert l+2<= len(map)
                if map[l+2][c] == 0:
                    self.__model.setMap(l+2,c,4) # move la caisse si rien derriere
                    self.__model.setMap(l+1,c,0)
                    self.__model.setPlayer(l+1,c)
                elif map[l+2][c] == 4:
                    self.__model.setMap(l+2,c,5) # move la caisse si rien derriere
                    self.__model.setMap(l+1,c,0)
                    self.__model.setPlayer(l+1,c)
                self.verifWin()
            elif map[l+1][c] == 5:
                assert l+2<= len(map)
                if map[l+2][c] == 0:
                    self.__model.setMap(l+2,c,5) # move la caisse si rien derriere
                    self.__model.setMap(l+1,c,0)
                    self.__model.setPlayer(l+1,c)
                self.verifWin()
            
        
        elif direction == "gauche":
            assert c>0
            if map[l][c-1] == 0:
                self.__model.setPlayer(l,c-1)
            elif map[l][c-1] == 3:
                assert c-2>=0
                if map[l][c-2] == 0:
                    self.__model.setMap(l,c-2,3) # move la caisse si rien derriere
                    self.__model.setMap(l,c-1,0)
                    self.__model.setPlayer(l,c-1)
                elif map[l][c-2] == 3:
                    self.__model.setMap(l,c-2,4) # move la caisse si rien derriere
                    self.__model.setMap(l,c-1,0)
                    self.__model.setPlayer(l,c-1)
                self.verifWin()
            elif map[l][c-1] == 4:
                assert c-2>=0
                if map[l][c-2] == 0:
                    self.__model.setMap(l,c-2,4) # move la caisse si rien derriere
                    self.__model.setMap(l,c-1,0)
                    self.__model.setPlayer(l,c-1)
                elif map[l][c-2] == 4:
                    self.__model.setMap(l,c-2,5) # move la caisse si rien derriere
                    self.__model.setMap(l,c-1,0)
                    self.__model.setPlayer(l,c-1)
                self.verifWin()
            elif map[l][c-1] == 5:
                assert c-2>=0
                if map[l][c-2] == 0:
                    self.__model.setMap(l,c-2,5) # move la caisse si rien derriere
                    self.__model.setMap(l,c-1,0)
                    self.__model.setPlayer(l,c-1)
                self.verifWin()
    
    def verifWin(self):
        posTrou = self.__model.getTrou()
        compteur = 0
        for pos,weight in posTrou.items():
            if weight == 0:
                if self.__model.getPosMap(pos[0],pos[1]) == 3: # Si il y a une caisse sur le trou
                    compteur+=1
            elif weight == 1:
                if self.__model.getPosMap(pos[0],pos[1]) == 4: # Si il y a une caisse sur le trou
                    compteur+=1
            elif weight == 2:
                if self.__model.getPosMap(pos[0],pos[1]) == 5: # Si il y a une caisse sur le trou
                    compteur+=1
        if compteur == len(posTrou):
            self.__view.winner()