from textoPlano.TextoPlano import TextoPlano
from matriz.Matriz import Matriz
from playfair2.Playfair import Playfair
from minusculas.Minusculas import Minusculas

class Descifrador():
	def descifrar(self,clave,mensaje,alfabeto):
		#return Playfair().algoritmo(Matriz().creaMatriz(clave,alfabeto),TextoPlano().devolverPares(mensaje),"")
		return Minusculas().transformar(Playfair().algoritmo(Matriz().creaMatriz(clave.upper(),alfabeto),TextoPlano().devolverPares(mensaje.upper()),""),mensaje,"")
