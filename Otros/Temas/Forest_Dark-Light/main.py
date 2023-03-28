from tkinter.ttk import Entry, LabelFrame, Style, Button, Spinbox, Treeview, Combobox, Checkbutton
from tkinter import Tk


class DarkLightForestWindow(Tk):
    def __init__(self):
        super().__init__()
        # Definimos el estilo de la ventana
        style = Style(self)
        self.call("source", "forest-dark.tcl")
        style.theme_use("forest-dark")

        # Agregamos algunas configuraciones a la ventana principal
        self.config(border=10)
        self.rowconfigure(0, weight=1)
        self.columnconfigure([0, 1], weight=1)

        # Creamos el LabelFrame para almacenar los demas widgets
        frame = LabelFrame(self, text="Ingresar Fila")
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="news")
        frame.columnconfigure(0, weight=1)

        # Creamos el Entry que captura el nombre
        self.nombre = Entry(frame)
        self.nombre.insert(0, "Nombre")
        self.nombre.bind("<FocusIn>", lambda e: self.nombre.delete("0", "end"))
        # self.nombre.bind("<FocusOut>", lambda e: self.validar_entry)
        self.nombre.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        # Creamos el SpinBox que captura la edad
        edad = Spinbox(frame, from_=18, to=100)
        edad.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

        # Creamos el ComboBox que captura la suscripcion
        suscripcion = Combobox(frame, state=["readonly"])
        suscripcion.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
        suscripcion["values"] = ("Suscrito", "No Suscrito", "Otro")

        # Creamos el CheckBox para saber si esta desempleado o no
        empleo = Checkbutton(frame, text="Empleado")
        empleo.grid(row=3, column=0, sticky="ew", padx=10, pady=10)

        # Creamos el Boton para insertar datos a la tabla
        boton_insertar = Button(frame, text="Insertar", command=self.ingresar_datos)
        boton_insertar.grid(row=4, column=0, sticky="ew", padx=10, pady=10)

        # Creamos el Treeview simulara una tabla
        self.tabla = Treeview(self, columns=("#1", "#2", "#3"))
        self.tabla.grid(row=0, column=1, padx=10, pady=10, sticky="news")

        # Añadimos las configuraciones a la tabla
        titulos = ["Nombre", "Edad", "Suscripcion", "Empleo"]

        for i in range(len(titulos)):
            self.tabla.heading(f"#{i}", text=titulos[i], anchor="center")
            self.tabla.column(f"#{i}", anchor="center")

    def ingresar_datos(self):
        self.tabla.insert("", "end", text=self.nombre.get())


if __name__ == '__main__':
    app = DarkLightForestWindow()
    app.mainloop()
