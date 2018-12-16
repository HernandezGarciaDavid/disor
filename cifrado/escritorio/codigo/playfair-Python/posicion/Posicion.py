from columna.Columna import Columna

class Posicion():
	def devolverPosicion(self,caracter,matriz,i):
		if caracter in matriz[i]:
			return (i,Columna().index(caracter,matriz[i],0))
		i+=1
		return self.devolverPosicion(caracter,matriz,i)
