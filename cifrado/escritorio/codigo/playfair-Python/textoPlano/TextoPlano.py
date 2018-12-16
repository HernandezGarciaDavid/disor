class TextoPlano():
	def devolverPares(self,mensaje):
		if len(mensaje) % 2 != 0:
			mensaje+='X'
		return mensaje
