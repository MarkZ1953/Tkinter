from tkinter import Tk, Menu


class Menu_Contextual(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.menu = None

        # Agregamos algunas configuraciones a la ventana
        self.title("Menu Contextual")
        self.geometry("360x360")

        # Llamamos a el metodo que crea el menu
        self.create_menu()

        # Creamos un evento en la ventana padre, que se active con el boton derecho del mouse
        self.bind("<Button-3>", self.display_menu)

    def create_menu(self):
        # Creamos el menu y lo agregamos a la ventana principal
        self.menu = Menu(self, tearoff=False)

        # Se crea un diccionario que contiene los textos que llevaran los labels, pero también se pueden
        # agregar comandos, reemplazándolos por las cadenas vacías.
        menu_contextual_textos_comandos = \
            {"Copiar": "",
             "Cortar": "",
             "Pegar": "",
             "Recargar": "",
             "Renombrar": ""
             }

        i = 0

        # Agregamos opciones al menu
        for texto, funcion in menu_contextual_textos_comandos.items():
            self.menu.add_command(label=texto)
            if i in [3]:
                self.menu.add_separator()
            i += 1

    def display_menu(self, event):
        """
        tk_popup: Toma las coordenadas X y Y del raton (en píxeles) en la pantalla y muestra el menu
        en esa ubicación.
        grab_release: Libera el control de los eventos del menu para que la ventana principal pueda volver
        a recibir eventos.
        """
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()


if __name__ == '__main__':
    # Instanciamos la clase y ejecutamos la ventana
    app = Menu_Contextual()
    app.mainloop()
