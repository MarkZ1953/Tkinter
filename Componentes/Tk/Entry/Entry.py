import tkinter as tk
from tkinter import ttk

class Entry:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("300x300")
        self.crear_entries()
        self.crear_boton()
        self.crear_etiqueta()
    
    def crear_entries(self):
        self.entry1 = ttk.Entry(self.root)
        self.entry1.pack(padx=10,pady=5)

        self.entry2 = ttk.Entry(self.root)
        self.entry2.pack(padx=10,pady=5)

    def crear_boton(self):
        boton1 = ttk.Button(self.root,text="Aceptar",cursor="hand2",command=lambda:self.informacion())
        boton1.pack()

        boton2 = ttk.Button(self.root,text="Enfocar 1",cursor="hand2",command=lambda:self.enfocar(1))
        boton2.pack()

        boton3 = ttk.Button(self.root,text="Enfocar 2",cursor="hand2",command=lambda:self.enfocar(2))
        boton3.pack()

        boton4 = ttk.Button(self.root,text="Insertar Textos",cursor="hand2",command=lambda:self.insertar())
        boton4.pack()

        boton5 = ttk.Button(self.root,text="Limpiar",cursor="hand2",command=lambda:self.limpiar_entries())
        boton5.pack()

    def crear_etiqueta(self):
        self.label = ttk.Label(self.root,text="")
        self.label.pack()

    def enfocar(self,val):
        if val == 1:
            self.entry1.focus()
        else:
            self.entry2.focus()

    def insertar(self):
        self.entry1.insert(0,"Esto es un")
        self.entry2.insert(0,"Texto insertado")

    def limpiar_entries(self):
        self.entry1.delete(0,"end")
        self.entry2.delete(0,"end")

    def informacion(self):
        self.label.config(text=f"Entry 1 : {self.entry1.get()}\nEntry 2 : {self.entry2.get()}")

if __name__ == "__main__":
    app = Entry()
    app.root.mainloop()