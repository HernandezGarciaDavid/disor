from buscador2.Buscador import Buscador

class Playfair():
	def algoritmo(self,matriz,mensaje,mensajeCifrado):
		if len(mensaje)==0:
			return mensajeCifrado
		mensajeCifrado+=Buscador().buscar(mensaje[0:2],matriz)
		return self.algoritmo(matriz,mensaje[2:],mensajeCifrado)