from tkinter import Frame,Label, Entry,StringVar

class Input(object):
	def __init__(self,**kwargs):
		print(kwargs)
		frame=Frame(kwargs.pop('root'))
		frame.pack()
		self.__label=Label(frame,text=kwargs.pop('titulo'))
		self.__label.grid(row=0,column=0)
		self.__entrada=StringVar(None)
		self.__texto=Entry(frame,textvariable=self.__entrada)
		#texto.bind('<Key>',kwargs.pop('accion'))
		self.__texto.grid(row=0,column=1)
	
	def get(self):
		return self.__entrada.get()

	def set(self,texto):
		return self.__entrada.set(texto)

	def setEvent(self,evento):
		self.__texto.bind('<Key>',evento)
