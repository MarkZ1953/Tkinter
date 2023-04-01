import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ComboBox:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("ComboBox")
        self.root.minsize(250,100)
        self.root.config(bd=10)
        self.root.columnconfigure([0,1],weight=1)
        self.root.rowconfigure([0,1],weight=1)
        self.crear_combobox()
        self.crear_label()
        self.crear_boton()

    def crear_label(self):
        opcion = tk.Label(self.root,text="Opcion")
        opcion.grid(row=0,column=0,sticky="e")

    def crear_combobox(self):
        self.seleccion = tk.StringVar()
        combo = ttk.Combobox(self.root,textvariable=self.seleccion,state=["readonly"])
        combo["values"] = ("a","b","c")
        combo.grid(row = 0,column=1,padx=10,pady=10)

    def crear_boton(self):
        bton = tk.Button(self.root,text="Aceptar",cursor="hand2",command=lambda:self.mostrar())
        bton.grid(row=1,columnspan=2,padx=10,pady=10)

    def mostrar(self):
        messagebox.showinfo("Informacion","Elegiste la opcion " + self.seleccion.get())

if __name__ == "__main__":
    app = ComboBox()
    app.root.mainloop()
