# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:31:38 2019

@author: quent
"""

from joueur import Joueur
from game import Game

 # Programme principale du blocus
listDeJoueur = []
for i in range(2):
	print("Quel est le nom du joueur " + str(i + 1) + " ?")
	nomJoueur = input()
	print("Quel est la couleur (charactère) du joueur  " + str(i + 1) + "  ?")
	couleurJoueur = input();
	listDeJoueur.append(Joueur(nomJoueur, couleurJoueur))

game = Game(listDeJoueur)
game.start()

