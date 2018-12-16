from cifrado.cifrado import Cifrado
from descifrador.Descifrador import Descifrador
from tkinter import Tk, Label, Entry, StringVar,Button,Radiobutton,IntVar
abecedearioEspañol=['A', 'Á', 'B', 'C', 'D', 'E', 'É', 'F', 'G', 'H', 'I', 'Í', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'Ó', 'P', 'Q', 'R', 'S', 'T', 'U', 'Ú', 'V', 'W', 'X', 'Y', 'Z']

def ok():
 if v.get() ==1:
 	mensaje=Descifrador().descifrar(directory.get(),directory2.get(),abecedearioEspañol)
 	directoryResultado.set(mensaje)
 else:
 	mensaje=Cifrado().cifrar(directory.get(),directory2.get(),abecedearioEspañol)
 	directoryResultado.set(mensaje)

root = Tk()
root.title("Cifrador Playfair")
root.geometry("400x400+0+0")

labelClave=StringVar()
labelClave.set("Introduce la clave: ")
labelDir=Label(root, textvariable=labelClave, height=4)
labelDir.pack()

directory=StringVar(None)
dirname=Entry(root,textvariable=directory,width=50)
dirname.pack()

labelMensaje=StringVar()
labelMensaje.set("Introduce el mensaje: ")
labelDir=Label(root, textvariable=labelMensaje, height=4)
labelDir.pack()

directory2=StringVar(None)
dirname=Entry(root,textvariable=directory2,width=50)
dirname.pack()

v = IntVar()

Radiobutton(root, text="Descifrado", variable=v, value=1).pack()
Radiobutton(root, text="Cifrado", variable=v, value=2).pack()


boton = Button(root, text="OK", command=ok)
boton.pack()

labelResultado=StringVar()
labelResultado.set("Resultado: ")
labelDir=Label(root, textvariable=labelResultado, height=4)
labelDir.pack()

directoryResultado=StringVar(None)
dirname=Entry(root,textvariable=directoryResultado,width=50)
dirname.pack()
root.mainloop()

