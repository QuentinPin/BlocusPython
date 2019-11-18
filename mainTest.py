# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 08:50:28 2019

@author: quent
"""

from enregistrement import Enregistrement
from plateau import Plateau

saveFile = Enregistrement.loadFile("test1.npz")

plateau = Plateau()
plateau.setPlateau(saveFile["plateau"])
plateau.affichePlateau()