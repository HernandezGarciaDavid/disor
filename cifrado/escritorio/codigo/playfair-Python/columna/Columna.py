class Columna():
	def index(self,caracter,fila,indice):
		if caracter == fila[0]:
			return indice
		indice+=1
		return self.index(caracter,fila[1:],indice)
