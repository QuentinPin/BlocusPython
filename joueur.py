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

	def getPieces(self):
		return self.listDePiece

	def setPieces(self, listDePiece):
		self.listDePiece = listDePiece

	def getNbPieceRestante(self):
		return len(self.listDePiece)

	def getNom(self):
		return self.nom