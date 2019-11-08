# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 08:26:25 2019

@author: quent
"""

#permet de récupéré a partir d'un fichier
import numpy as np

class Piece:

	# Constructeur de ma pièce. On lui donne en param sa pièce
	def __init__(self, matrice):
		self.matrice = matrice
		self.positionX = 0
		self.positionY = 0

	# Permet d'afficher uniquement la pièce
	def afficher(self):
		ligne = ""
		for i in range(len(self.matrice)):
			ligne = ""
			for y in range(len(self.matrice)):
				ligne += "|" + self.matrice[i][y]
			ligne += "|"
			print(ligne)

	# Fait une rotation par la gauche de la pièce
	def rotation(self):
		nouvelleMatrice = []
		matriceTempo = []
		numLigne = 0
		for x in range(len(self.matrice)):
			for y in range(len(self.matrice)):
				matriceTempo.append(self.matrice[y][len(self.matrice) -1 - numLigne])
			nouvelleMatrice.append(matriceTempo)
			matriceTempo = []
			numLigne += 1
		self.matrice = nouvelleMatrice

	# Return la plus grande longueur de la pièce (taille de la matrice)
	def getSizeMatrice(self):
		return len(self.matrice)

	# Return la couleur de la pièce a cette coordonné (la matrice de la pièce
	# a quand même des zone vide, ne fesant pas partie de la pièce)
	def getColorAtThisPoint(self, x, y):
		return self.matrice[x, y]