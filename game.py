# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:08:31 2019

@author: quent
"""
from plateau import Plateau
from factoryPiece import FactoryPiece
import keyboard
import time

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
			self.plateau.putPieceOnPreview(self.pieceEnCours)
			self.plateau.affichePlateau()
			self.pieceEnCours.afficher()
			self.afficheMenu()
			self.action()

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
		self.pieceEnCours = self.joueurEnCours.getPremierePiece()

	def action(self):
		time.sleep(.1)
		while True:
			try:
				if keyboard.is_pressed('z'):
					self.pieceEnCours.monter()
					break
				elif keyboard.is_pressed('s'):
					self.pieceEnCours.descendre()
					break
				elif keyboard.is_pressed('q'):
					self.pieceEnCours.gauche()
					break
				elif keyboard.is_pressed('d'):
					self.pieceEnCours.droite()
					break
				elif keyboard.is_pressed('r'):
					self.pieceEnCours.rotation()
					break
				elif keyboard.is_pressed('t'):
					self.pieceEnCours.retourner()
					break
				elif keyboard.is_pressed('m'):
					self.pieceEnCours.positionX = 10
					self.pieceEnCours.positionY = 10
					self.pieceEnCours = self.joueurEnCours.getPieceSuivante()
					break
				elif keyboard.is_pressed('l'):
					self.pieceEnCours.positionX = 10
					self.pieceEnCours.positionY = 10
					self.pieceEnCours = self.joueurEnCours.getPiecePrecedente()
					break
				elif keyboard.is_pressed('v'):
					self.plateau.validerPiece()
					self.joueurEnCours.removePiece(self.pieceEnCours)
					self.joueurSuivant()
					break
			except:
				break