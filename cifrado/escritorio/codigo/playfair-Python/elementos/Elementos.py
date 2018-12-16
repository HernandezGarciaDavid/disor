class Elementos():
	def revision(self,caracter,alfabeto,resultado):
		if caracter in alfabeto and not caracter in resultado:
			resultado.append(caracter)
		return resultado