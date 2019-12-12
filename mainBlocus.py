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
def suprimerPieceDejasPlacer(joueur, tableauId):
	pieceSuprimer = []
	for i in joueur.getPieces():
		if str(i.getId()) not in list(tableauId[1:]):
			pieceSuprimer.append(i)
	for i in pieceSuprimer:
		 joueur.getPieces().remove(i)

print("Choisissez une action : ")
print("\t - (1) Nouvelle partie")
print("\t - (2) Charger une partie")

action = input()
if action == "1":
	listDeJoueur = []
	nombreDeJoueurSaisie = 0
	while nombreDeJoueurSaisie != '2' and nombreDeJoueurSaisie != "4":
		nombreDeJoueurSaisie = input("Entrer le nombre de joueur (2 ou 4) :" )
	nombreDeJoueurSaisie = int(nombreDeJoueurSaisie)
	for i in range(nombreDeJoueurSaisie):
		listDeJoueur.append(Joueur(str(i + 1)))
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
		joueur1 = Joueur(str(fileToLoad["pieceJoueur1"][0]))
		joueur2 = Joueur(str(fileToLoad["pieceJoueur2"][0]))
		joueur1.setPieces(FactoryPiece.createAllPiece(joueur1.couleur))
		joueur2.setPieces(FactoryPiece.createAllPiece(joueur2.couleur))
		suprimerPieceDejasPlacer(joueur1, fileToLoad["pieceJoueur1"])
		suprimerPieceDejasPlacer(joueur2, fileToLoad["pieceJoueur2"])
		if "pieceJoueur3" in fileToLoad.files:
			joueur3 = Joueur(str(fileToLoad["pieceJoueur3"][0]))
			joueur3.setPieces(FactoryPiece.createAllPiece(joueur3.couleur))
			suprimerPieceDejasPlacer(joueur3, fileToLoad["pieceJoueur3"])
		if "pieceJoueur4" in fileToLoad.files:
			joueur4 = Joueur(str(fileToLoad["pieceJoueur4"][0]))
			joueur4.setPieces(FactoryPiece.createAllPiece(joueur4.couleur))
			suprimerPieceDejasPlacer(joueur4, fileToLoad["pieceJoueur4"])
		if joueur2.getNbPieceRestante() > joueur1.getNbPieceRestante():
			listDeJoueur.append(joueur2)
			listDeJoueur.append(joueur3)
			listDeJoueur.append(joueur4)
			listDeJoueur.append(joueur1)
		if joueur3.getNbPieceRestante() > joueur2.getNbPieceRestante():
			listDeJoueur.append(joueur3)
			listDeJoueur.append(joueur4)
			listDeJoueur.append(joueur1)
			listDeJoueur.append(joueur2)
		if joueur4.getNbPieceRestante() > joueur3.getNbPieceRestante():
			listDeJoueur.append(joueur4)
			listDeJoueur.append(joueur1)
			listDeJoueur.append(joueur2)
			listDeJoueur.append(joueur3)
		else :
			listDeJoueur.append(joueur1)
			listDeJoueur.append(joueur2)
			listDeJoueur.append(joueur3)
			listDeJoueur.append(joueur4)
		game = Game(listDeJoueur)
		game.setPlateau(plateau)
		game.start()
	else:
		print("Il n'y a aucun fichier de sauvegarde")