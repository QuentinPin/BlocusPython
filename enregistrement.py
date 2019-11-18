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
		pieceDuJoueur1 = self.createTableauPieceJoueur(self.listDejoueur[0].listDePiece)
		pieceDuJoueur2 = self.createTableauPieceJoueur(self.listDejoueur[1].listDePiece)
		np.savez(fileName, plateauDeJeu=self.plateau, pieceJoueur1=pieceDuJoueur1, pieceJoueur2=pieceDuJoueur2, plateau=self.plateau.tableauJeu)

	def createTableauPieceJoueur(self, listeDePiece):
		listePieceJoueur = []
		for i in range(len(listeDePiece)):
			listePieceJoueur.append(listeDePiece[i].pieceId)
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