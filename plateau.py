class Plateau:
	def __init__(self):
		self.taille = 22
		self.tableauJeu = [[' ' for i in range(self.taille)] for j in range(self.taille)]	

	def effaceEcran ():
		for i in range (1,100) :
		    print("\n")
	
	def initPlateau(self):
		for i in range(self.taille):
			self.tableauJeu[0][i] = '*'
			self.tableauJeu[i][0] = '*'
			self.tableauJeu[self.taille-1][i] = '*'
			self.tableauJeu[i][self.taille-1] = '*'

	def affichePlateau (self):
		for ligne in range (self.taille):
		    for colonne in range (self.taille):
		        print (self.tableauJeu[ligne][colonne],end="")
		    print(" ")

	


#put piece, vérification si placement 
#						->oui alors la placé
#							-> vérifier si game fini
