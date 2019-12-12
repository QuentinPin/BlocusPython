# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:08:31 2019
@author: quent
"""
from plateau import Plateau
from factoryPiece import FactoryPiece
import keyboard
import time
from enregistrement import Enregistrement
from operator import itemgetter, attrgetter

class Game:


	def __init__(self, listeDeJoueur):
		self.plateau = Plateau()
		self.listDeJoueur = listeDeJoueur
		for i in range(len(self.listDeJoueur)):
			if self.listDeJoueur[i].getPieces() == None or len(self.listDeJoueur[i].getPieces()) == 0:
				self.listDeJoueur[i].setPieces(FactoryPiece.createAllPiece(self.listDeJoueur[i].couleur))
		self.joueursEnVie = []
		for p in self.listDeJoueur:
			self.joueursEnVie.append(p)
		self.joueurEnCours = None
		self.pieceEnCours = None
		self.runGame = True
		self.nbSurrender = 0
		self.classement = []

	def start(self):
		self.joueurEnCours = self.joueursEnVie[0]
		self.pieceEnCours = self.joueurEnCours.getPremierePiece()
		self.plateau.initPlateau()
		self.plateau.affichePlateau()
		print("Que le jeux commence !!")
		self.deroulementDuJeu()

	def deroulementDuJeu(self):
		while(self.runGame): #Tant que la partie n'est pas fini
			self.plateau.putPieceOnPreview(self.pieceEnCours)
			for i in range(10) : print()
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
		print("")
		print("\t- (B) pour sauvegarder et quitter la partie")

	def joueurSuivant(self):
		if (len(self.joueursEnVie) == 1):
			self.joueurEnCours = self.joueursEnVie[0]
		if self.joueursEnVie.index(self.joueurEnCours) == len(self.joueursEnVie)-1:
			self.joueurEnCours = self.joueursEnVie[0]
		else:
			self.joueurEnCours = self.joueursEnVie[self.joueursEnVie.index(self.joueurEnCours)+1]
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
					if(self.plateau.validerPiece(self.pieceEnCours, self.joueurEnCours, self.listDeJoueur)):
						self.joueurEnCours.removePiece(self.pieceEnCours)
						self.joueurEnCours.surrender = self.plateau.verifierFinPartie(self.joueurEnCours, self.listDeJoueur)
						for player in self.joueursEnVie:
							if (player.surrender == True):
								self.joueursEnVie.remove(player)
								self.classement.append(player)
								self.nbSurrender = self.nbSurrender + 1
						nbJoueur = len(self.joueursEnVie) + len(self.classement)
						if ((self.plateau.partieFini(self.joueurEnCours)) or (self.nbSurrender == nbJoueur)):
							self.runGame = False
							for player in self.classement:
								player.calculPoint()
							self.classement = sorted(self.classement, key=attrgetter('nbPoint'), reverse=False)
							for i in range(len(self.classement)):
								if (i == 0):
									print ("Le joueur " + str(self.classement[i].couleur) + " à gagner avec " + str(self.classement[i].nbPoint) + " points")
								else:
									print ("Le joueur " + str(self.classement[i].couleur) + " à perdu avec " + str(self.classement[i].nbPoint) + " points")
						self.joueurSuivant()
					break
				elif keyboard.is_pressed('b'):
					fileName = input("Saisissez le nom de votre partie : ")
					print("Enregistrement en cours....")
					save = Enregistrement(self.plateau, self.listDeJoueur)
					save.enregistrer(fileName)
					print("Enregistrement terminer....")
					self.runGame = False
					break
				elif keyboard.is_pressed('h'):
					self.plateau.bot(self.joueurEnCours, self.listDeJoueur)
					self.joueurEnCours.surrender = self.plateau.verifierFinPartie(self.joueurEnCours, self.listDeJoueur)
					for player in self.joueursEnVie:
						if (player.surrender == True):
							self.joueurSuivant()
							self.joueursEnVie.remove(player)
							self.classement.append(player)
							self.nbSurrender = self.nbSurrender + 1
					nbJoueur = len(self.joueursEnVie) + len(self.classement)
					if ((self.plateau.partieFini(self.joueurEnCours)) or (self.nbSurrender == nbJoueur)):
						self.runGame = False
						for player in self.classement:
							player.calculPoint()
						self.classement = sorted(self.classement,  key=attrgetter('nbPoint'), reverse=False)
						for i in range(len(self.classement)):
							if (i == 0):
								print ("Le joueur " + str(self.classement[i].couleur) + " à gagner avec " + str(self.classement[i].nbPoint) + " points")
							else:
								print ("Le joueur " + str(self.classement[i].couleur) + " à perdu avec " + str(self.classement[i].nbPoint) + " points")
					self.joueurSuivant()
					break
			except:
				break

	def setPlateau(self, plateau):
		self.plateau = plateau

	def setListeJoueur(self, listeDeJoueur):
		self.listDeJoueur = listeDeJoueur