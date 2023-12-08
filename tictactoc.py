
class Game():
    def __init__(self):
        self.jeu = [[0,0,0],[0,0,0],[0,0,0]]

    def afficher(self):
        print(self.jeu)

    def jouer(self, joueur):
        jeu_valide = False
        while jeu_valide:
            self.afficher()
            print("Vous pouvez jouer que sur une case non jouée")
            x,y = -1, -1
            while y >= 0 and y < 3 and isinstance(y,int):
                print("Jouer sur la ligne? (ex: ligne 1, y = 0)")
                y = input("y=")
            while x >= 0 and x < 3 and isinstance(x,int):
                print("Jouer sur la colonne (ex: colonne 3, x = 2)")
                x = input("y=")
            
            if self.jeu[x][y] == 0:
                self.jeu[x][y] = joueur
            else: 
                print("Un joueur à déjà jouer ici")

        def check_fin(self):
            transposed_jeu = [list(row) for row in zip(*self.jeu)]
            if self.jeu[0] == [1,1,1] or self.jeu[1] == [1,1,1] or self.jeu[2] == [1,1,1]:
                return 1 
            elif self.jeu[0] == [2,2,2] or self.jeu[1] == [2,2,2] or self.jeu[2] == [2,2,2]:
                return 2
            
            elif transposed_jeu[0] == [1,1,1] or transposed_jeu[1] == [1,1,1] or transposed_jeu[2] == [1,1,1]:
                return 1 
            elif transposed_jeu[0] == [2,2,2] or transposed_jeu[1] == [2,2,2] or transposed_jeu[2] == [2,2,2]:
                return 2    
            elif self.jeu[0][0] == 1 and self.jeu[1][1] == 1 and self.jeu[2][2] == 1:
                return 1
            elif self.jeu[0][2] == 1 and self.jeu[1][1] == 1 and self.jeu[2][0] == 1:
                return 1
            elif self.jeu[0][0] == 1 and self.jeu[1][1] == 1 and self.jeu[2][2] == 1:
                return 2
            elif self.jeu[0][2] == 1 and self.jeu[1][1] == 1 and self.jeu[2][0] == 1:
                return 2
            else:
                return 0 
        
        

