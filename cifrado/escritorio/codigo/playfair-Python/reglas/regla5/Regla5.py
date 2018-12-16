from posicion.Posicion import Posicion

class Regla5():
	def aplicar(self,mensaje,matriz,resultado):
		if Posicion().devolverPosicion(mensaje[0],matriz,0)[0]-1 >= 0:# len(matriz):
			resultado+=matriz[Posicion().devolverPosicion(mensaje[0],matriz,0)[0]-1][Posicion().devolverPosicion(mensaje[0],matriz,0)[1]]
		else:
			resultado+=matriz[len(matriz)-1][Posicion().devolverPosicion(mensaje[0],matriz,0)[1]]
		if Posicion().devolverPosicion(mensaje[1],matriz,0)[0]-1 >= 0:#< len(matriz):
			resultado+=matriz[Posicion().devolverPosicion(mensaje[1],matriz,0)[0]-1][Posicion().devolverPosicion(mensaje[1],matriz,0)[1]]
		else:
			resultado+=matriz[len(matriz)-1][Posicion().devolverPosicion(mensaje[1],matriz,0)[1]] 
		return resultado