import tkinter as tk  #Librerias predeterminadas de Python

class Primera_Inferfaz():
    def __init__(self):
        self.root = tk.Tk()
        #self.root.iconbitmap("Aqui va la ruta de la Imagen") #Para insertar iconos 
        self.root.title("Calculadora") # Sirve para cambiar el nombre
        self.root.resizable(1,1) # Sirve para que la gente pueda redimensionar alto y ancho, 0 para falso y 1 para verdadero
        #self.root.geometry("650x350") # Dar el tamaño de la ventana 
        self.root.config(bg="red") # Sirve para dar el color del fondo
        self.root.mainloop() # IMPORTANTE : Siempre debe quedar de ultimas, sirve para ejecutar la ventana
    
    def crear_frame(self):
        self.miframe = tk.Frame(self.root)
        self.miframe.pack(side="right",anchor="s") #left, right,top,bottom, s o n para redireccionar a las esquinas
        self.miframe.config(bg="blue",width="650",height="350")

Primera_Inferfaz()