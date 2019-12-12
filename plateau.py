import sys
import numpy as np
import copy

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

	# Permet d'ajouter la pièce au plateau
	def putPieceInMatrice(self, piece, matrice):
		self.copyTableauJeu()
		x = piece.positionX
		y = piece.positionY
		for i in range(len(piece.matrice)):
			for j in range(len(piece.matrice)):
				if y < self.taille-1 and y > 0 and x < self.taille-1 and x > 0:
					if piece.matrice[i][j] != " ":
						matrice[x][y] = piece.matrice[i][j]
				y += 1
			y = piece.positionY
			x +=1

	def validerPiece(self, pieceEnCours, joueur, joueurs):
		#On doit d'abord faire la vérification
		if (self.verifierPlacement(pieceEnCours, joueur, joueurs, False) == True):
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

	def tabEgal(self, tab1, tab2):
		for i in range(len(tab1)):
			for j in range(len(tab1)):
				if(tab1[i][j] != tab2[i][j]):
					return False
		return True

	def bot(self, joueur, joueurs):
		copyTableauJeu = [[' ' for i in range(self.taille)] for j in range(self.taille)]
		tableauTemp = [[' ' for i in range(self.taille)] for j in range(self.taille)]
		for i in range(self.taille):
			for j in range(self.taille):
				copyTableauJeu[i][j] = self.tableauJeu[i][j]
				tableauTemp[i][j] = self.tableauJeu[i][j]
		if (len(joueur.listDePiece) == 0):
			return
		for piece in joueur.listDePiece:
			copyPiece = None 
			copyPiece = copy.copy(piece)
			for x in range(22):
				for y in range(22):
					if (copyTableauJeu[x][y] != '*'):
						copyPiece.positionX = x
						copyPiece.positionY = y
						for a in range (2):
							for b in range (4):
								for p in range(self.taille):
									for m in range(self.taille):
										tableauTemp[p][m] = self.tableauJeu[p][m]
								self.putPieceInMatrice(copyPiece, tableauTemp)
								if (self.tabEgal(tableauTemp, copyTableauJeu)):
									copyPiece.rotation()
									break
								if (self.verifierPlacement(copyPiece, joueur, joueurs, True) == True):
									self.putPieceInMatrice(copyPiece, self.tableauJeu)
									self.putPieceInMatrice(copyPiece, self.tableauDeJeuPreview)
									joueur.listDePiece.remove(piece)
									return
								copyPiece.rotation()
							if(a == 0):
								copyPiece.retourner()
#TODO VERIF LISTE JOUEUR 
	def verifierFinPartie(self, joueur, joueurs):
		copyTableauJeu = [[' ' for i in range(self.taille)] for j in range(self.taille)]
		tableauTemp = [[' ' for i in range(self.taille)] for j in range(self.taille)]
		for i in range(self.taille):
			for j in range(self.taille):
				copyTableauJeu[i][j] = self.tableauJeu[i][j]
				tableauTemp[i][j] = self.tableauJeu[i][j]
		if (len(joueur.listDePiece) == 0):
			return True
		for piece in joueur.listDePiece:
			copyPiece = None 
			copyPiece = copy.copy(piece)
			for x in range(22):
				for y in range(22):
					if (copyTableauJeu[x][y] != '*'):
						copyPiece.positionX = x
						copyPiece.positionY = y
						for a in range (2):
							for b in range (4):
								for p in range(self.taille):
									for m in range(self.taille):
										tableauTemp[p][m] = self.tableauJeu[p][m]
								self.putPieceInMatrice(copyPiece, tableauTemp)
								if (self.tabEgal(tableauTemp, copyTableauJeu)):
									copyPiece.rotation()
									break
								if (self.verifierPlacement(copyPiece, joueur, joueurs, True) == True):
									return False
								copyPiece.rotation()
							if(a == 0):
								copyPiece.retourner()
		return True

	def verifierPlacement(self, lastPiece, joueur, joueurs, isTest):
		copyTableauJeu = [[' ' for i in range(self.taille)] for j in range(self.taille)]
		listSquarePlacer = []
		verif = False
		for i in range(self.taille):
			for j in range(self.taille):
				copyTableauJeu[i][j] = self.tableauJeu[i][j]
		if ((copyTableauJeu == self.tableauDeJeuPreview) and (isTest == False)):
			if isTest == False:
				print("\033[31m", "ERREUR impossible de placer la piece")
				print("\033[37m")
			return False
		for i in range(len(lastPiece.matrice)):
			for j in range(len(lastPiece.matrice)):
				for player in joueurs:
					if((lastPiece.matrice[i][j] != ' ') and (lastPiece.positionX+i < 22 and lastPiece.positionY+j < 22)):
						if ((joueur.couleur != player.couleur) and (copyTableauJeu[lastPiece.positionX+i][lastPiece.positionY+j] == player.couleur) and (lastPiece.matrice[i][j] != ' ')):
							if isTest == False:
								print("\033[31m", "ERREUR impossible de placer la piece")
								print("\033[37m")
							return False
						if ((copyTableauJeu[lastPiece.positionX+i][lastPiece.positionY+j] == '*') and (lastPiece.matrice[i][j] != ' ')):
							if isTest == False:
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
								if isTest == False:
									print("\033[31m", "ERREUR impossible de placer la piece")
									print("\033[37m")
								return False
		if((verif == False) and (isTest == False)):
			print("\033[31m", "ERREUR impossible de placer la piece")
			print("\033[37m")
		return verif
