import tkinter as tk
from tkinter import ttk

class RadioButton:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.crear_radiobuttons()
        self.crear_etiqueta()

    def crear_radiobuttons(self):
        self.opcion = tk.IntVar()

        self.hombre = ttk.Radiobutton(text="Hombre",variable=self.opcion,value=1,command=self.eleccion)
        self.hombre.pack()

        self.mujer = ttk.Radiobutton(text="Mujer",variable=self.opcion,value=2,command=self.eleccion)
        self.mujer.pack()

    def crear_etiqueta(self):
        self.label = ttk.Label(self.root,text="")
        self.label.pack()

    def eleccion(self):
        if self.opcion.get() == 1:
            self.label.config(text="Has elegido Hombre")
        else:
            self.label.config(text="Has elegido Mujer")

if __name__ == "__main__":
    app = RadioButton()
    app.root.mainloop()