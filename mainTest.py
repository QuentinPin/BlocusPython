# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 17:57:50 2019

@author: quent
"""


print("\033[37m  quentin")

"""
data = [
    [1,0,0,0,0,1,1,1,1,0],
    [0,0,0,0,0,1,0,0,1,0],
    [0,0,1,0,1,0,1,1,0,0],
    [0,0,1,0,0,1,1,0,1,0],
    [0,0,1,0,1,0,0,1,1,0],
    [1,0,0,1,0,1,0,0,1,0],
    [0,1,0,0,0,1,1,1,1,1],
    [0,1,0,0,0,0,1,1,1,1],
    [1,0,0,0,1,1,1,0,1,0],
    [1,1,1,1,0,0,0,1,1,1]
]

from matplotlib import pyplot as plt
from matplotlib import colors
cmap = colors.ListedColormap(['Blue','red','black', 'yellow', 'white'])
plt.figure(figsize=(6,6))
plt.pcolor(data[::-1],cmap=cmap,edgecolors='k', linewidths=3)
plt.show()"""
"""

import tkinter as tk

windows = tk.Tk()
windows.title("Blocus")

canvas = tk.Canvas(width=400, height=400, bg='white')

heightA = 0
widhtA = 0
heightB = 30
widhtB = 30
dictionnaire={}
dictionnaire[0] = "blue"
dictionnaire[1] = "red"


for i in range(len(matrix)):
	for y in range(len(matrix)):
		canvas.create_rectangle(widhtA,heightA,widhtB,heightB, fill=dictionnaire[matrix[i][y]])
		widhtA += 30
		widhtB += 30
	widhtA = 0
	widhtB = 30
	heightA += 30
	heightB += 30

canvas.delete("all")

canvas.pack()



windows.mainloop()"""