from tkinter import Tk
from entrada.Input import Input
from opciones.Opciones import Opciones
from cesar.Cesar import Cesar
from eventos.Eventos import Eventos


root = Tk()
root.title("Cifrador Playfair")
root.geometry("400x160+0+0")
mensaje=Input(root=root,titulo="Mensaje")#,accion=Eventos.accionCifrado)
desplazamiento=Input(titulo="Desplazamiento",root=root)#,accion=Eventos.accionCambioDeDesplazamiento)
resultado=Input(root=root,titulo="resultado Cesar")#,accion=Eventos.accionDescifrado)
resultadoT=Input(root=root,titulo="resultado Transpuesta")
resultadoT3=Input(root=root,titulo="resultado Transpuesta3")
grupo=Input(root=root,titulo="grupo transpuesta")
resultadoTg=Input(root=root,titulo="resultado Transpuesta por grupo")
Eventos = Eventos(mensaje,desplazamiento,resultado)
mensaje.setEvent(Eventos.accionCifrado)
desplazamiento.setEvent(Eventos.accionCambioDeDesplazamiento)
resultado.setEvent(Eventos.accionDescifrado)
root.mainloop()
