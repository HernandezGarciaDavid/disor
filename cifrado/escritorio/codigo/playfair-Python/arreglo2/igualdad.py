#from comparacion.Comparacion import Comparacion

class Iguales():
	def sonIguales(self,caracter,matriz):
		if len(matriz) == 0:
			return False
		if caracter in matriz[0]:
			return True
		return self.sonIguales(caracter,matriz[1:])