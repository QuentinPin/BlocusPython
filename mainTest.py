# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 08:50:28 2019

@author: quent
"""

from enregistrement import Enregistrement

maMatrice = [["0","0","0","0","0","0"],
			 ["0","0","0","0","0","0"],
			 ["0","0","0","0","0","0"],
			 ["0","0","0","0","0","0"],
			 ["0","1","0","0","0","0"],
			 ["0","0","0","0","0","0"]]

temp = Enregistrement(maMatrice)

temp.enregistrer()