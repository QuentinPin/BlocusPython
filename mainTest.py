# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 08:50:28 2019

@author: quent
"""

def affichePlateau (tableauDeJeuPreview):
		for ligne in range (10):
		    for colonne in range (10):
		        print (tableauDeJeuPreview[ligne][colonne],end="")
		    print(" ")

def placer(matrice, piece):
	px = 2
	py = 2
	x = px
	y = py
	for i in range(len(piece)):
		for j in range(len(piece)):
			if piece[i][j] != " ":
				matrice[x][y] = piece[i][j]
			y += 1
		y = py
		x +=1
	return matrice

matrice = [[0,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0,0]]


matriceACopier = [[" ", "1","1"],
				  [" ", "1"," "],
				  ["1", "1"," "]]

affichePlateau(placer(matrice, matriceACopier))