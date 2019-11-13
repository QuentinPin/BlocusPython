# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:08:31 2019

@author: quent
"""
from plateau import Plateau
from factoryPiece import FactoryPiece

class Game:


	def __init__(self, listeDeJoueur):
		self.plateau = Plateau()
		self.listDeJoueur = listeDeJoueur
		# Ajout de toutes les pièce au joueur
		for i in range(len(self.listDeJoueur)):
			self.listDeJoueur[i].setPieces(FactoryPiece.createAllPiece(self.listDeJoueur[i].couleur))
		self.joueurEnCours = None
		self.pieceEnCours = None

	def start(self):
		self.joueurEnCours = self.listDeJoueur[1]
		self.pieceEnCours = self.joueurEnCours.getPremierePiece()
		self.plateau.initPlateau()
		self.plateau.affichePlateau()
		print("Que le jeux commence !!")
		self.deroulementDuJeu()

	def deroulementDuJeu(self):
		while(True): #Tant que la partie n'est pas fini
			self.plateau.affichePlateau()
			self.pieceEnCours.afficher()
			self.afficheMenu()
			saisie = input()
			self.action(saisie)



	def afficheMenu(self):
		print("Choisissez une action : ")
		print("\t- (Z) pour monter la pièce")
		print("\t- (S) pour déscendre la pièce")
		print("\t- (Q) pour décaler la pièce à gauche")
		print("\t- (D) pour décaler la pièce à droite")
		print("")
		print("\t- (R) pour tourner la pièce")
		print("\t- (T) pour retourner la pièce")
		print("\t- (m) pièce suivante")
		print("\t- (l) pièce précédente")
		print("\t- (V) pour valider (placer la pièce)")

	def joueurSuivant(self):
		self.joueurEnCours = self.listDeJoueur[1 - self.listDeJoueur.index(self.joueurEnCours)]

	def action(self, saisie):
		if saisie == "z":
			print()
		elif saisie == "s":
			print()
		elif saisie == "q":
			print()
		elif saisie == "d":
			print()
		elif saisie == "r":
			self.pieceEnCours.rotation()
		elif saisie == "t":
			self.pieceEnCours.retourner()
		elif saisie == "m":
			self.pieceEnCours = self.joueurEnCours.getPieceSuivante()
		elif saisie == "l":
			self.pieceEnCours = self.joueurEnCours.getPiecePrecedente()
		elif saisie == "v":
			print()
		else:
			print("Commande non autorisé")