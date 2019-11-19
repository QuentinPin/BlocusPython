# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:31:38 2019

@author: quent
"""

from joueur import Joueur
from game import Game
from enregistrement import Enregistrement
from plateau import Plateau
from factoryPiece import FactoryPiece

 # Programme principale du blocus
def suprimerPièceDejasPlacer(joueur, tableauId):
	pieceSuprimer = []
	for i in joueur.getPieces():
		if str(i.getId()) not in list(tableauId):
			pieceSuprimer.append(i)
	for i in pieceSuprimer:
		 joueur.getPieces().remove(i)

print("Choisissez une action : ")
print("\t - (1) Nouvelle partie")
print("\t - (2) Charger une partie")

action = input()
if action == "1":
	listDeJoueur = []
	for i in range(2):
		couleurJoueur = ""
		while couleurJoueur == "":
			print("Quel est la couleur (caractère) du joueur  " + str(i + 1) + "  ?")
			couleurJoueur = input()
		listDeJoueur.append(Joueur(couleurJoueur))
	game = Game(listDeJoueur)
	game.start()
elif action == "2":
	listDeJoueur = []
	fichiers = Enregistrement.getFichierSauvegarde()
	if len(fichiers) > 0:
		print("Choisissez la partie que vous voulez charger : ")
		for i in range(len(fichiers)):
			print("\t - (" + str(i) + ") " + fichiers[i])
		saisie = input()
		fileToLoad = Enregistrement.loadFile(fichiers[int(saisie)])
		plateau = Plateau()
		plateau.setPlateau(fileToLoad["plateau"])
		joueur1 = Joueur(fileToLoad["pieceJoueur1"][0])
		joueur2 = Joueur(fileToLoad["pieceJoueur2"][0])
		joueur1.setPieces(FactoryPiece.createAllPiece(joueur1.couleur))
		joueur2.setPieces(FactoryPiece.createAllPiece(joueur2.couleur))
		suprimerPièceDejasPlacer(joueur1, fileToLoad["pieceJoueur1"])
		suprimerPièceDejasPlacer(joueur2, fileToLoad["pieceJoueur2"])
		if len(fileToLoad["pieceJoueur2"]) > len(fileToLoad["pieceJoueur1"]):
			listDeJoueur.append(joueur1)
			listDeJoueur.append(joueur2)
		else:
			listDeJoueur.append(joueur2)
			listDeJoueur.append(joueur1)
		game = Game(listDeJoueur)
		game.setPlateau(plateau)
		game.start()
	else:
		print("Il n'y a aucun fichier de sauvegarde")
