from tkinter import Tk, Menu


class Menus(Tk):
    def __init__(self) -> None:
        super().__init__()

        # Agregamos algunas configuraciones a la ventana principal
        self.title("Menus")
        self.geometry("300x300")

        # Llamamos al metodo para crear los menus
        self.crear_menus()

    def crear_menus(self):
        # Creamos la Barra del Menu
        barramenu = Menu(self)

        # Agregamos el menu a la ventana principal
        self.config(menu=barramenu)

        # Creamos el Menu Archivo
        archivomenu = Menu(barramenu)

        # Creamos el Menu Edicion
        menuedicion = Menu(barramenu)

        # Creamos el Menu Herramientras
        menuherramientas = Menu(barramenu)

        # Creamos el Menu Ayuda
        menuayuda = Menu(barramenu)

        # Agregamos el Menu archivomenu a la barramenu
        barramenu.add_cascade(label="Archivo", menu=archivomenu)

        archivo_menu_textos_comandos = \
            {"Nuevo": "funcion",
             "Guardar": "funcion",
             "Guardar Como...": "funcion",
             "Salir": "funcion"
             }

        # Desactivamos el tearoff del archivomenu
        archivomenu.config(tearoff=False)

        i = 0

        # Creamos opciones de menu para archivomenu
        # Se pueden añadir metodos al gusto, que se ponen en el diccionario
        for texto, funcion in archivo_menu_textos_comandos.items():
            archivomenu.add_cascade(label=texto)
            if i in [0, 2]:
                archivomenu.add_separator()
            i += 1

        # Agregamos el Menu menuedicion a la barramenu
        barramenu.add_cascade(label="Edicion", menu=menuedicion)

        # Agregamos el Menu menuherramientas a la barramenu
        barramenu.add_cascade(label="Herramientas", menu=menuherramientas)

        # Agregamos el Menu menuayuda a la barramenu
        barramenu.add_cascade(label="Ayuda", menu=menuayuda)


if __name__ == "__main__":
    # Instanciamos la clase y ejecutamos la ventana
    app = Menus()
    app.mainloop()
