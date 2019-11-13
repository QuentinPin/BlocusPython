from piece import Piece

class FactoryPiece:
	def createAllPiece(couleur):
		listeAllPiece = []
		Piece1 = [[' ' for i in range(1)] for j in range(1)]
		Piece1[0][0] = couleur

		Piece2 = [[' ' for i in range(2)] for j in range(2)]
		Piece2[0][0] = couleur
		Piece2[1][0] = couleur

		Piece3 = [[' ' for i in range(3)] for j in range(3)]
		Piece3[0][0] = couleur
		Piece3[1][0] = couleur
		Piece3[2][0] = couleur

		Piece4 = [[' ' for i in range(2)] for j in range(2)]
		Piece4[0][0] = couleur
		Piece4[1][0] = couleur
		Piece4[1][1] = couleur

		Piece5 = [[' ' for i in range(4)] for j in range(4)]
		Piece5[0][0] = couleur
		Piece5[1][0] = couleur
		Piece5[2][0] = couleur
		Piece5[3][0] = couleur

		Piece6 = [[' ' for i in range(3)] for j in range(3)]
		Piece6[0][1] = couleur
		Piece6[1][1] = couleur
		Piece6[2][1] = couleur
		Piece6[2][0] = couleur

		Piece7 = [[' ' for i in range(3)] for j in range(3)]
		Piece7[0][0] = couleur
		Piece7[1][0] = couleur
		Piece7[1][1] = couleur
		Piece7[2][0] = couleur

		Piece8 = [[' ' for i in range(2)] for j in range(2)]
		Piece8[0][0] = couleur
		Piece8[0][1] = couleur
		Piece8[1][0] = couleur
		Piece8[1][1] = couleur

		Piece9 = [[' ' for i in range(3)] for j in range(3)]
		Piece9[0][0] = couleur
		Piece9[0][1] = couleur
		Piece9[1][1] = couleur
		Piece9[1][2] = couleur

		Piece10 = [[' ' for i in range(5)] for j in range(5)]
		Piece10[0][0] = couleur
		Piece10[1][0] = couleur
		Piece10[2][0] = couleur
		Piece10[3][0] = couleur
		Piece10[4][0] = couleur

		Piece11 = [[' ' for i in range(4)] for j in range(4)]
		Piece11[0][1] = couleur
		Piece11[1][1] = couleur
		Piece11[2][1] = couleur
		Piece11[3][1] = couleur
		Piece11[3][0] = couleur

		Piece12 = [[' ' for i in range(4)] for j in range(4)]
		Piece12[0][1] = couleur
		Piece12[1][1] = couleur
		Piece12[2][1] = couleur
		Piece12[2][0] = couleur
		Piece12[3][0] = couleur

		Piece13 = [[' ' for i in range(3)] for j in range(3)]
		Piece13[0][1] = couleur
		Piece13[1][1] = couleur
		Piece13[2][1] = couleur
		Piece13[1][0] = couleur
		Piece13[2][0] = couleur

		Piece14 = [[' ' for i in range(3)] for j in range(3)]
		Piece14[0][0] = couleur
		Piece14[0][1] = couleur
		Piece14[1][1] = couleur
		Piece14[2][0] = couleur
		Piece14[2][1] = couleur

		Piece15 = [[' ' for i in range(4)] for j in range(4)]
		Piece15[0][0] = couleur
		Piece15[1][0] = couleur
		Piece15[1][1] = couleur
		Piece15[2][0] = couleur
		Piece15[3][0] = couleur

		Piece16 = [[' ' for i in range(3)] for j in range(3)]
		Piece16[0][1] = couleur
		Piece16[1][1] = couleur
		Piece16[2][0] = couleur
		Piece16[2][1] = couleur
		Piece16[2][2] = couleur

		Piece17 = [[' ' for i in range(3)] for j in range(3)]
		Piece17[0][0] = couleur
		Piece17[1][0] = couleur
		Piece17[2][0] = couleur
		Piece17[2][1] = couleur
		Piece17[2][2] = couleur

		Piece18 = [[' ' for i in range(3)] for j in range(3)]
		Piece18[0][0] = couleur
		Piece18[0][1] = couleur
		Piece18[1][1] = couleur
		Piece18[1][2] = couleur
		Piece18[2][2] = couleur

		Piece19 = [[' ' for i in range(3)] for j in range(3)]
		Piece19[0][0] = couleur
		Piece19[1][0] = couleur
		Piece19[1][1] = couleur
		Piece19[1][2] = couleur
		Piece19[2][2] = couleur

		Piece20 = [[' ' for i in range(3)] for j in range(3)]
		Piece20[0][0] = couleur
		Piece20[1][0] = couleur
		Piece20[1][1] = couleur
		Piece20[1][2] = couleur
		Piece20[2][1] = couleur

		Piece21 = [[' ' for i in range(3)] for j in range(3)]
		Piece21[0][1] = couleur
		Piece21[1][0] = couleur
		Piece21[1][1] = couleur
		Piece21[1][2] = couleur
		Piece21[2][1] = couleur

		listeAllPiece.append(Piece(Piece1))
		listeAllPiece.append(Piece(Piece2))
		listeAllPiece.append(Piece(Piece3))
		listeAllPiece.append(Piece(Piece4))
		listeAllPiece.append(Piece(Piece5))
		listeAllPiece.append(Piece(Piece6))
		listeAllPiece.append(Piece(Piece7))
		listeAllPiece.append(Piece(Piece8))
		listeAllPiece.append(Piece(Piece9))
		listeAllPiece.append(Piece(Piece10))
		listeAllPiece.append(Piece(Piece11))
		listeAllPiece.append(Piece(Piece12))
		listeAllPiece.append(Piece(Piece13))
		listeAllPiece.append(Piece(Piece14))
		listeAllPiece.append(Piece(Piece15))
		listeAllPiece.append(Piece(Piece16))
		listeAllPiece.append(Piece(Piece17))
		listeAllPiece.append(Piece(Piece18))
		listeAllPiece.append(Piece(Piece19))
		listeAllPiece.append(Piece(Piece20))
		listeAllPiece.append(Piece(Piece21))

		return listeAllPiece


	def affichePieces(pieces):
		for piece in pieces:
			for ligne in range (len(piece)):
				for colonne in range (len(piece)):
					print (piece[ligne][colonne],end="")
				print(" ")
			print(" ")