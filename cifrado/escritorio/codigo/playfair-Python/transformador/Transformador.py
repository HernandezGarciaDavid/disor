from posicion.Posicion import Posicion
from reglas.regla1.Regla1 import Regla1
from reglas.regla2.Regla2 import Regla2
from reglas.regla3.Regla3 import Regla3
#Codigo idiomaticco 
#lenguajes idiosincracioas cosas que no deberian de pasar
#inoterfaz grafica de usuario para los 4 lenguajes
class Transformador():
	def convierte(self,mensaje,matriz):
		if Posicion().devolverPosicion(mensaje[0],matriz,0)[0] == Posicion().devolverPosicion(mensaje[0],matriz,0)[0]:
			return Regla1().aplicar(mensaje,matriz,"")
		if Posicion().devolverPosicion(mensaje[0],matriz,0)[1] == Posicion().devolverPosicion(mensaje[0],matriz,0)[1]:
			return Regla2().aplicar(mensaje,matriz,"")
		return Regla3().aplicar(mensaje,matriz)