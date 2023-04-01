import tkinter as tk

class Imagenes:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=1)
        self.imagen1 = tk.PhotoImage(file="python.png")
        self.mostrar()
        self.root.mainloop()

    def mostrar(self):
        Label = tk.Label(self.root,image=self.imagen1)
        Label.grid(row=0,column=0,sticky="news")

#Tener en cuenta que para poder mostrar imagenes, las imagenes deben estar en el directorio correcto, de otra forma generara siempre un error.

app = Imagenes()