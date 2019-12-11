# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:48:10 2019

@author: quent
"""
import numpy as np
import glob
import os

class Enregistrement:

	def __init__(self, plateau, listJoueur):
		self.plateau = plateau
		self.listDejoueur = listJoueur

	def enregistrer(self, fileName):
		if len(self.listDejoueur) == 2:
			pieceDuJoueur1 = self.createTableauPieceJoueur(0)
			pieceDuJoueur2 = self.createTableauPieceJoueur(1)
			np.savez(fileName, plateauDeJeu=self.plateau, pieceJoueur1=pieceDuJoueur1, pieceJoueur2=pieceDuJoueur2, plateau=self.plateau.tableauJeu)
		if len(self.listDejoueur) == 4:
			pieceDuJoueur1 = self.createTableauPieceJoueur(0)
			pieceDuJoueur2 = self.createTableauPieceJoueur(1)
			pieceDuJoueur3 = self.createTableauPieceJoueur(2)
			pieceDuJoueur4 = self.createTableauPieceJoueur(3)
			np.savez(fileName, plateauDeJeu=self.plateau, pieceJoueur1=pieceDuJoueur1, pieceJoueur2=pieceDuJoueur2, pieceJoueur3=pieceDuJoueur3, pieceJoueur4=pieceDuJoueur4, plateau=self.plateau.tableauJeu)

	def createTableauPieceJoueur(self, index):
		listePieceJoueur = []
		listePieceJoueur.append(self.listDejoueur[index].couleur)
		for i in range(len(self.listDejoueur[index].listDePiece)):
			listePieceJoueur.append(self.listDejoueur[index].listDePiece[i].pieceId)
		return listePieceJoueur

	def loadFile(fileName):
		b = np.load(fileName)
		return b

	def getFichierSauvegarde():
		fichier=[]
		l = glob.glob(os.getcwd() + '\\*')
		for i in l:
			fichier.append(i)
		fichiers = []
		for i in fichier:
			tempo = i.replace(os.getcwd()+'\\', "")
			if "npz" in tempo:
				fichiers.append(tempo)
		return fichiers