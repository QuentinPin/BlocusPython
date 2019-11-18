import numpy as np

class Plateau:
	def __init__(self):
		self.taille = 22
		self.tableauJeu = [[' ' for i in range(self.taille)] for j in range(self.taille)]
		self.tableauDeJeuPreview = None

	def effaceEcran ():
		for i in range (1,100) :
		    print("\n")

	def initPlateau(self):
		for i in range(self.taille):
			self.tableauJeu[0][i] = '*'
			self.tableauJeu[i][0] = '*'
			self.tableauJeu[self.taille-1][i] = '*'
			self.tableauJeu[i][self.taille-1] = '*'
		self.tableauDeJeuPreview = np.copy(self.tableauJeu)

	def affichePlateau (self):
		for ligne in range (self.taille):
		    for colonne in range (self.taille):
		        print (self.tableauDeJeuPreview[ligne][colonne],end="")
		    print(" ")

	# Permet d'ajouter la pièce au plateau
	def putPieceOnPreview(self, piece):
		self.tableauDeJeuPreview = np.copy(self.tableauJeu)
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

	def setPlateau(self, matrice):
		self.tableauDeJeuPreview = matrice
		self.tableauJeu = matrice

	def validerPiece(self):
		#On deoit d'abord faire la vérification
		self.tableauJeu = np.copy(self.tableauDeJeuPreview)
		#On devra metre un return pour dire que le pour dire si la pièce a bien été placé