from textoPlano.TextoPlano import TextoPlano
from matriz.Matriz import Matriz
from playfair.Playfair import Playfair 
from minusculas.Minusculas import Minusculas

class Cifrado():
	def cifrar(self,clave,mensaje,alfabeto):
		return Minusculas().transformar(Playfair().algoritmo(Matriz().creaMatriz(clave.upper(),alfabeto),TextoPlano().devolverPares(mensaje.upper()),""),mensaje,"")
