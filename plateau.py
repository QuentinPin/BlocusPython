import numpy as np

class Plateau:
	def __init__(self):
		self.taille = 22
		self.tableauJeu = [[' ' for i in range(self.taille)] for j in range(self.taille)]
		self.tableauDeJeuPreview = [[' ' for i in range(self.taille)] for j in range(self.taille)]

	def setPlateau(self, matrice):
		self.tableauDeJeuPreview = np.copy(matrice)
		self.tableauJeu = np.copy(matrice)

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
				if self.tableauDeJeuPreview[ligne][colonne] == 1 or self.tableauDeJeuPreview[ligne][colonne] =="1":
					print("\033[41m", " ", end="") #rouge
					print("\033[0m", end="")
				elif self.tableauDeJeuPreview[ligne][colonne] == 2  or self.tableauDeJeuPreview[ligne][colonne] =="2":
					print("\033[42m", " ", end="") #vert
					print("\033[0m", end="")
				elif self.tableauDeJeuPreview[ligne][colonne] == 3 or self.tableauDeJeuPreview[ligne][colonne] =="3":
					print("\033[45m", " ", end="") #magenta
					print("\033[0m", end="")
				elif self.tableauDeJeuPreview[ligne][colonne] == 4 or self.tableauDeJeuPreview[ligne][colonne] =="4":
					print("\033[46m", " ", end="") #bleu
					print("\033[0m", end="")
				else:
					print(self.tableauDeJeuPreview[ligne][colonne] + " ", end="")
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

	def validerPiece(self, pieceEnCours, joueur, nextJoueur):
		#On doit d'abord faire la vérification
		if (self.verifierPlacement(pieceEnCours, joueur, nextJoueur) == True):
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

	def	partieFini(self, joueur):
		if(len(joueur.listDePiece) <= 0):
			return True
		else:
			return False

	def verifierPlacement(self, lastPiece, joueur, nextJoueur):
		copyTableauJeu = [[' ' for i in range(self.taille)] for j in range(self.taille)]
		listSquarePlacer = []
		verif = False
		for i in range(self.taille):
			for j in range(self.taille):
				copyTableauJeu[i][j] = self.tableauJeu[i][j]
		for i in range(len(lastPiece.matrice)):
			for j in range(len(lastPiece.matrice)):
				if ((copyTableauJeu[lastPiece.positionX+i][lastPiece.positionY+j] == nextJoueur.couleur) and (lastPiece.matrice[i][j] != ' ')):
					print("\033[31m", "ERREUR impossible de placer la piece")
					print("\033[37m")
					return False
				if ((copyTableauJeu[lastPiece.positionX+i][lastPiece.positionY+j] == '*') and (lastPiece.matrice[i][j] != ' ')):
					print("\033[31m", "ERREUR impossible de placer la piece")
					print("\033[37m")
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
						print("\033[37m")
						return False
		if(verif == False):
			print("\033[31m", "ERREUR impossible de placer la piece")
			print("\033[37m")
		return verif
