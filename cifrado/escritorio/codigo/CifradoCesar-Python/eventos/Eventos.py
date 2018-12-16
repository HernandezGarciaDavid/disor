from cesar.Cesar import Cesar 

class Eventos():

	def __init__(self,mensaje,desplazamiento,resultado):
		self.mensaje=mensaje
		self.desplazamiento=desplazamiento
		self.resultado=resultado
		abecedearioEspañol=['A', 'Á', 'B', 'C', 'D', 'E', 'É', 'F', 'G', 'H', 'I', 'Í', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'Ó', 'P', 'Q', 'R', 'S', 'T', 'U', 'Ú', 'V', 'W', 'X', 'Y', 'Z']
		self.cifrador = Cesar(abecedearioEspañol)

	def accionCifrado(self,event):
		if len( self.desplazamiento.get())>0:
			self.resultado.set( self.cifrador.cifrado(int( self.desplazamiento.get()), self.mensaje.get(),""))

	def accionDescifrado(self,event):
		if len( self.desplazamiento.get())>0:
			self.mensaje.set( self.cifrador.desCifrar(int( self.desplazamiento.get()), self.resultado.get(),""))
		

	def accionCambioDeDesplazamiento(self,event):
		if len( self.desplazamiento.get())==0:
			return
		self.accionCifrado(event)
	