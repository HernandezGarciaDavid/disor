from posicion.Posicion import Posicion

class Regla4():
	def aplicar(self,mensaje,matriz,resultado):
		if Posicion().devolverPosicion(mensaje[0],matriz,0)[1]-1 >= 0:# len(matriz[Posicion().devolverPosicion(mensaje[0],matriz,0)[0]]):
			resultado+=matriz[Posicion().devolverPosicion(mensaje[0],matriz,0)[0]][Posicion().devolverPosicion(mensaje[0],matriz,0)[1]-1]
		else:
			resultado+=matriz[Posicion().devolverPosicion(mensaje[0],matriz,0)[0]][len(matriz[Posicion().devolverPosicion(mensaje[0],matriz,0)[0]])-1]
		if Posicion().devolverPosicion(mensaje[1],matriz,0)[1]-1 >= 0:#< len(matriz[Posicion().devolverPosicion(mensaje[1],matriz,0)[0]]):
			resultado+=matriz[Posicion().devolverPosicion(mensaje[1],matriz,0)[0]][Posicion().devolverPosicion(mensaje[1],matriz,0)[1]-1]
		else:
			resultado+=matriz[Posicion().devolverPosicion(mensaje[1],matriz,0)[0]][len(matriz[Posicion().devolverPosicion(mensaje[1],matriz,0)[0]])-1] 
		return resultado
