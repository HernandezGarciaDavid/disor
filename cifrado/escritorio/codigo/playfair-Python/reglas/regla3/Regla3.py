from reglas.regla3.cambio.Cambio import Cambio
from posicion.Posicion import Posicion

class Regla3():
	def aplicar(self,mensaje,matriz):
		return Cambio().cambiar(Posicion().devolverPosicion(mensaje[0],matriz,0),Posicion().devolverPosicion(mensaje[0],matriz,0),matriz,"")