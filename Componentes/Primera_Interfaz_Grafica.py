# Librerias predeterminadas de Python (tk, ttk)

"""
Se puede importar toda la libreria entera de tk, pero no es tan eficiente al momento de convertir el archivo
a una aplicacion real, ya que importaria toda la libreria y volveria más lento el programa. Es recomendable
solo importar lo que se va a utilizar a medida que se vaya realizando la aplicacion.
"""

# import tkinter as tk
from tkinter import Tk, Frame, Label

"""
- Las diferencias entre usar ttk y tk, son mas que todo el estilo.
Tk tiene un estilo mas clasico y ttk es mas moderno y tiene algunos widgets 
y opciones mas para ofrecer que Tk. 
- El uso de estas dependera del programador.
"""


class Primera_Inferfaz(Tk):
    def __init__(self):
        # Aplicamos la POO, cuando usamos super().__init__(), estamos llamando a los atributos de la clase Tk,
        # ósea estamos heredando lo que tiene la clase para manejarlo a nuestro gusto, no tenemos que instanciar
        # la clase directamente, sino que puede ser llamada desde nuestra misma clase.
        super().__init__()

        # Podemos agregar un Icono
        # self.root.iconbitmap("Aqui va la ruta de la Imagen")

        # Cambiamos el nombre de la ventana
        self.title("Calculadora")

        # Configurar el redimensionamiento de la ventana (True, False) o (1, 0) | (Ancho, Alto)
        self.resizable(True, True)

        # Configuraciones del tamaño de la ventana (Ancho, Alto)
        self.minsize(300, 300)

        # Son algunas configuraciones para la ventana puedes ver más en: "Layout Managements"
        self.rowconfigure([0, 1], weight=1)
        self.columnconfigure(0, weight=1)

        # Predeterminar el tamaño de la ventana principal
        # self.root.geometry("650x350")

        # Podemos usar config para cambiar las propiedades de los widgets
        # Cambiamos el color de fondo y el borde de la ventana
        self.config(bg="red", border=20)

        # Llamamos al método que nos crea el frame
        self.crear_frame()

        # Agregamos una etiqueta para la ventana padre
        Label(self, text="¡Esta es la ventana padre!", background="red").grid(row=0, column=0, sticky="ew")

        # mainloop(), se puede llamar desde la misma clase o afuera de esta misma
        # IMPORTANTE: Siempre debe quedar de últimas, sirve para ejecutar la ventana
        # self.mainloop()

    def crear_frame(self):
        # Creamos un Frame que está dentro de la ventana padre o ventana principal (self)
        # También le damos color al Frame
        mi_frame = Frame(self, background="blue")

        # Son algunas configuraciones para la ventana puedes ver más en: "Layout Managements"
        mi_frame.grid(row=1, column=0, sticky="news")
        mi_frame.columnconfigure(0, weight=1)
        mi_frame.rowconfigure(0, weight=1)

        # Agregamos una etiqueta para el Frame
        Label(mi_frame, text="¡Este es un Frame!", background="blue").grid(row=0, column=0, sticky="news")


# El __name__ == "__main__", significa que solo se ejecutara si estamos en esta ventana
if __name__ == '__main__':
    # Instanciamos nuestra interfaz
    app = Primera_Inferfaz()
    # IMPORTANTE: Siempre debe quedar de últimas, sirve para ejecutar la ventana
    app.mainloop()
