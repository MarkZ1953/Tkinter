from tkinter.ttk import Button, Label, Entry, Frame
from tkinter import Tk, messagebox
from MLRSOFT import MLRSOFT


def centrar_ventana(root):
    window_width = root.winfo_reqwidth()
    window_height = root.winfo_reqheight()
    position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
    root.geometry("+{}+{}".format(position_right, position_down))


class Empleados(Tk):
    """
    Esta clase crea una ventana encargada de recolectar la cantidad de empleados
    para poder contabilizar la cantidad de empleados.
    """
    def __init__(self) -> None:
        super().__init__()
        # Agregamos algunas configuraciones a la ventana
        self.cant = None
        self.title("Cantidad de Empleados")
        self.geometry("360x100")
        self.resizable(False, False)
        self.configure(border=15)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.columnconfigure(0, weight=1)
        centrar_ventana(self)

        # Llamamos al metodo que crea los widgets
        self.crear_widgets()

    def crear_widgets(self):
        # Creamos un frame
        frame = Frame(self)
        frame.grid(row=0, column=0, sticky="news")
        frame.columnconfigure([0, 1], weight=1)

        # Creamos una etiqueta
        Label(frame, text="Ingrese la cantidad de empleados ").grid(row=0, column=0)

        # Creamos un frame
        frame = Frame(self)
        frame.grid(row=0, column=0, sticky="news")
        frame.columnconfigure([0, 1], weight=1)

        # Creamos una etiqueta
        Label(frame, text="Ingrese la cantidad de empleados ").grid(row=0, column=0)

        # Creamos una caja de texto, que recoge la cantidad de empleados
        self.cant = Entry(frame)
        self.cant.grid(row=0, column=1)
        self.cant.focus()
        self.cant.bind("<Return>", self.aceptar)

        Button(self, text="Aceptar", command=self.abrir_ventana, cursor="hand2").grid(row=1, column=0)

    def aceptar(self, e):
        self.abrir_ventana()

    def abrir_ventana(self):
        if self.cant.get().isdigit():
            MLRSOFT(self.cant.get(), self)
        else:
            messagebox.showerror("Error", "Debes ingresar un numero entero.")


if __name__ == '__main__':
    # Instanciamos nuestra clase y creamos la ventana
    app = Empleados()
    app.mainloop()
