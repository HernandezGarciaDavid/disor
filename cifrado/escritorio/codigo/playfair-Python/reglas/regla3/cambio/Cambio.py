class Cambio():
	def cambiar(self,posicion1,posicion2,matriz,resultado):
		resultado+=matriz[posicion1[0]][posicion2[1]]
		resultado+=matriz[posicion2[0]][posicion1[1]]
		return resultado