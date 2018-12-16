from tkinter import Frame,Radiobutton,IntVar

class Opciones(object):
	def __init__(self,**kwargs):
		self.frame=Frame(kwargs.pop('root'))
		self.frame.pack()
		self.opcionSeleccionada=IntVar()
		self.__creaOpciones(kwargs.pop('opciones'),0)

	def __creaOpciones(self,opciones,valor):
		if len(opciones)==0:
			return 
		Radiobutton(self.frame, text=opciones[0], variable=self.opcionSeleccionada, value=valor).pack()
		return self.__creaOpciones(opciones[1:],valor+1)

	def get(self):
		return self.opcionSeleccionada.get()