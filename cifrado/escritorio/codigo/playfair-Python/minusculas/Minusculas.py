class Minusculas():
	def transformar(self,texto,textoOriginal,resultado):
		if len(textoOriginal)==0:
			if len(texto)>0:
				resultado+=texto[0]
			return resultado
		if textoOriginal[0].islower():
			resultado+=texto[0].lower()
		else:
			resultado+=texto[0]
		return self.transformar(texto[1:],textoOriginal[1:],resultado)