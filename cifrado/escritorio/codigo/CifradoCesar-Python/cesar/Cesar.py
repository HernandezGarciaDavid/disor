from desplazamiento.Desplazamiento import Desplazamiento

class Cesar():
	def __init__(self,alfabeto):
		self.alfabeto=alfabeto

	def cifrado(self,desplazamiento,mensaje,mensajeCifrado):
		if len(mensaje)==0:
			return mensajeCifrado
		mensajeCifrado += Desplazamiento().desplazar(desplazamiento,mensaje[0],self.alfabeto)
		return self.cifrado(desplazamiento,mensaje[1:],mensajeCifrado)

	def desCifrar(self,desplazamiento,mensajeCifrado,mensaje):
		if len(mensajeCifrado)==0:
			return mensaje
		mensaje += Desplazamiento().desplazarInverso(desplazamiento,mensajeCifrado[0],self.alfabeto)
		return self.desCifrar(desplazamiento,mensajeCifrado[1:],mensaje)