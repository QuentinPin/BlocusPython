# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:22:43 2019

@author: quent
"""

class Joueur:

	def __init__(self, nom, couleur):
		self.nom = nom
		self.couleur = couleur
		self.listDePiece = None
		self.indexDeLaPiece = 0

	def getPieces(self):
		return self.listDePiece

	def setPieces(self, listDePiece):
		self.listDePiece = listDePiece

	def getNbPieceRestante(self):
		return len(self.listDePiece)

	def getNom(self):
		return self.nom

	def getPremierePiece(self):
		self.indexDeLaPiece = 0
		return self.listDePiece[self.indexDeLaPiece]

	def getPieceSuivante(self):
		if self.indexDeLaPiece < len(self.listDePiece)-1:
			self.indexDeLaPiece += 1
		else:
			self.indexDeLaPiece = 0
		return self.listDePiece[self.indexDeLaPiece]

	def getPiecePrecedente(self):
		if self.indexDeLaPiece == 0:
			self.indexDeLaPiece = len(self.listDePiece) - 1
		else:
			self.indexDeLaPiece -= 1
		return self.listDePiece[self.indexDeLaPiece]
	
	def removePiece(self, piece):
		print(self.listDePiece)
		self.listDePiece.remove(piece)
