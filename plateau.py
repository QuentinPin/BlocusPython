import sys

class Plateau:
	def __init__(self):
		self.taille = 22
		self.tableauJeu = [[' ' for i in range(self.taille)] for j in range(self.taille)]
		self.tableauDeJeuPreview = [[' ' for i in range(self.taille)] for j in range(self.taille)]

	def initPlateau(self):
		for i in range(self.taille):
			self.tableauJeu[0][i] = '*'
			self.tableauJeu[i][0] = '*'
			self.tableauJeu[self.taille-1][i] = '*'
			self.tableauJeu[i][self.taille-1] = '*'
		self.copyTableauJeu()

	def affichePlateau (self):
		#self.effaceEcran()
		for ligne in range (self.taille):
		    for colonne in range (self.taille):
		        print (self.tableauDeJeuPreview[ligne][colonne],end="")
		    print(" ")

	# Permet d'ajouter la pièce au plateau
	def putPieceOnPreview(self, piece):
		self.copyTableauJeu()
		x = piece.positionX
		y = piece.positionY
		for i in range(len(piece.matrice)):
			for j in range(len(piece.matrice)):
				if y < self.taille-1 and y > 0 and x < self.taille-1 and x > 0:
					if piece.matrice[i][j] != " ":
						self.tableauDeJeuPreview[x][y] = piece.matrice[i][j]
				y += 1
			y = piece.positionY
			x +=1

	def validerPiece(self, pieceEnCours, joueur):
		#On doit d'abord faire la vérification
		if (self.verifierPlacement(pieceEnCours, joueur) == True):
			self.copyTableauPreview()
			return True
	
	def copyTableauJeu(self):
		for i in range(self.taille):
			for j in range(self.taille):
				self.tableauDeJeuPreview[i][j] = self.tableauJeu[i][j]

	def copyTableauPreview(self):
		for i in range(self.taille):
			for j in range(self.taille):
				self.tableauJeu[i][j] = self.tableauDeJeuPreview[i][j] 

	def verifierPlacement(self, lastPiece, joueur):
		copyTableauJeu = [[' ' for i in range(self.taille)] for j in range(self.taille)]
		listSquarePlacer = []
		verif = False
		for i in range(self.taille):
			for j in range(self.taille):
				copyTableauJeu[i][j] = self.tableauJeu[i][j]
		for i in range(len(lastPiece.matrice)):
			for j in range(len(lastPiece.matrice)):
				if ((copyTableauJeu[lastPiece.positionX+i][lastPiece.positionY+j] == '*') and (lastPiece.matrice[i][j] != ' ')):
					return False
				if (lastPiece.matrice[i][j] != ' ') and (copyTableauJeu[lastPiece.positionX+i][lastPiece.positionY+j] == ' '):
					copyTableauJeu[lastPiece.positionX+i][lastPiece.positionY+j] = lastPiece.matrice[i][j]
					listSquarePlacer.append(str(lastPiece.positionX+i)+";"+str(lastPiece.positionY+j))
					if (len(joueur.listDePiece) == 21) and (("1;1" in listSquarePlacer) or ("1;20" in listSquarePlacer) or ("20;1" in listSquarePlacer) or ("20;20" in listSquarePlacer)):
						verif = True
					if ((copyTableauJeu[lastPiece.positionX+i+1][lastPiece.positionY+j] != joueur.couleur) or (str(lastPiece.positionX+i+1)+";"+str(lastPiece.positionY+j) in listSquarePlacer)) and ((copyTableauJeu[lastPiece.positionX+i-1][lastPiece.positionY+j] != joueur.couleur) or (str(lastPiece.positionX+i-1)+";"+str(lastPiece.positionY+j) in listSquarePlacer)) and ((copyTableauJeu[lastPiece.positionX+i][lastPiece.positionY+j+1] != joueur.couleur) or (str(lastPiece.positionX+i)+";"+str(lastPiece.positionY+j+1) in listSquarePlacer)) and ((copyTableauJeu[lastPiece.positionX+i][lastPiece.positionY+j-1] != joueur.couleur) or (str(lastPiece.positionX+i)+";"+str(lastPiece.positionY+j-1) in listSquarePlacer)):
						if ((copyTableauJeu[lastPiece.positionX+i+1][lastPiece.positionY+j+1] == joueur.couleur) and (str(lastPiece.positionX+i+1)+";"+str(lastPiece.positionY+j+1) not in listSquarePlacer)) or ((copyTableauJeu[lastPiece.positionX+i-1][lastPiece.positionY+j-1] == joueur.couleur) and (str(lastPiece.positionX+i-1)+";"+str(lastPiece.positionY+j-1) not in listSquarePlacer)) or ((copyTableauJeu[lastPiece.positionX+i-1][lastPiece.positionY+j+1] == joueur.couleur) and (str(lastPiece.positionX+i-1)+";"+str(lastPiece.positionY+j+1) not in listSquarePlacer)) or ((copyTableauJeu[lastPiece.positionX+i+1][lastPiece.positionY+j-1] == joueur.couleur) and (str(lastPiece.positionX+i+1)+";"+str(lastPiece.positionY+j-1) not in listSquarePlacer)):
							verif = True
					else:
						print("\033[31m", "ERREUR impossible de placer la piece")
						return False
		if(verif == False):
			print("\033[31m", "ERREUR impossible de placer la piece")
			print("\033[37m")
		return verif				
		


































#boutiquer
#tarabiscotter
#bidouiller
