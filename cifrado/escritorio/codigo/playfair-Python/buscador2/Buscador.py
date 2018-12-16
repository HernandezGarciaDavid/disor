from arreglo2.igualdad import Iguales 
from transformador2.Transformador import Transformador

class Buscador():
	def buscar(self,mensaje,matriz):
		if Iguales().sonIguales(mensaje[0],matriz) and Iguales().sonIguales(mensaje[1],matriz):
			return Transformador().convierte(mensaje,matriz)
		return mensaje; 