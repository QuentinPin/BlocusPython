# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:31:38 2019

@author: quent
"""

from joueur import Joueur
from game import Game

 # Programme principale du blocus

print("Choisissez une action : ")
print("\t - (1) Nouvelle partie")
print("\t - (2) Charger une partie")

action = input()
if action == "1":
	listDeJoueur = []
	for i in range(2):
		nomJoueur = ""
		while nomJoueur == "":
			print("Quel est le nom du joueur " + str(i + 1) + " ?")
			nomJoueur = input()
		couleurJoueur = ""
		while couleurJoueur == "":
			print("Quel est la couleur (caractère) du joueur  " + str(i + 1) + "  ?")
			couleurJoueur = input();
		listDeJoueur.append(Joueur(nomJoueur, couleurJoueur))
	game = Game(listDeJoueur)
	game.start()
elif action == "2":
	print("salut")