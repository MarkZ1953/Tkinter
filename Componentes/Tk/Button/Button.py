from tkinter import Tk, Button


class Botones(Tk):
    def __init__(self):
        super().__init__()

        # Algunas configuraciones para la ventana principal
        self.geometry("245x245")
        self.config(border=10, background="black")
        self.title("Botones")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        """
        ------------------------------------
        Algunas propiedades de los Botones:
        ------------------------------------
        cursor: Sirve para agregarle el tipo de mano del cursor que se pondra cuando el cursor pase encima del boton
        command: Sirve para agregarle una funcion cuando se presiona el boton 
        text: Agrega el texto que va a tener el boton 
        anchor: Configura la posicion del texto
        """

        # Creamos el boton
        boton = Button(self, text="Presiona el Boton", command=self.boton_presionado, cursor="hand2", anchor="n")
        # Ubicamos el boton usando grid y lo expandimos por toda la ventana
        boton.grid(row=0, column=0, sticky="news")

    def boton_presionado(self):
        print("Has presionado el boton...")


if __name__ == '__main__':
    app = Botones()
    app.mainloop()
