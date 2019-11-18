# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:31:38 2019

@author: quent
"""

from joueur import Joueur
from game import Game
from enregistrement import Enregistrement
from plateau import Plateau

 # Programme principale du blocus

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
	print("Choisissez la partie que vous voulez charger : ")
	fichiers = Enregistrement.getFichierSauvegarde()
	for i in range(len(fichiers)):
		print("\t - (" + str(i) + ") " + fichiers[i])
	saisie = input()
	fileToLoad = Enregistrement.loadFile(fichiers[int(saisie)])
	listDeJoueur.append(Joueur("X"))
	listDeJoueur.append(Joueur("O"))
	game = Game(listDeJoueur)
	plateau = Plateau()
	plateau.setPlateau(fileToLoad["plateau"])
	game.setPlateau(plateau)
	game.start()
