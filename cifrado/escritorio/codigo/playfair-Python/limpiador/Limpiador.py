from elementos.Elementos import Elementos

class Limpiador():
	def limpiar(self,elementos,alfabeto,resultado):
		if len(elementos)==0:
			return resultado
		resultado=Elementos().revision(elementos[0],alfabeto,resultado)
		return self.limpiar(elementos[1:],alfabeto,resultado)
		
		