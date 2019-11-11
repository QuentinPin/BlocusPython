# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 08:50:28 2019

@author: quent
"""

from piece import Piece

matrice = [[" ", " ","1"],
		   ["1", "1","1"],
		   [" ", " "," "]]

unePiece = Piece(matrice)

unePiece.afficher()



unePiece.rotation()
unePiece.rotation()

unePiece.afficher()