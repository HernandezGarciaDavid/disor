class Desplazamiento():
	def desplazar(self,desplazamiento,caracter,alfabeto):
		if not caracter in alfabeto:
			return caracter
		if alfabeto.index(caracter)+desplazamiento > len (alfabeto)-1:
			return alfabeto[alfabeto.index(caracter)+desplazamiento - len (alfabeto)-2]
		return alfabeto[alfabeto.index(caracter)+desplazamiento]

	def desplazarInverso(self,desplazamiento,caracter,alfabeto):
		if not caracter in alfabeto:
			return caracter
		if alfabeto.index(caracter)-desplazamiento < 0:
			return alfabeto[len (alfabeto)+alfabeto.index(caracter)-desplazamiento ]
		return alfabeto[alfabeto.index(caracter)-desplazamiento]