import tkinter as tk
from tkinter import ttk

class Entry_Defecto:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("300x300")
        self.root.config(bd=10)
        self.crear_labels()
        self.crear_entries()
        self.crear_botones()
    
    def crear_entries(self):
        self.entry1 = ttk.Entry(self.root)
        self.entry1.grid(row=0,column=1)

        self.entry2 = tk.Entry(self.root)
        self.entry2.grid(row=1,column=1)

    def crear_labels(self):
        self.label1 = ttk.Label(self.root,text="Metodo Insert (ttk,tk): ")
        self.label1.grid(row=0,column=0)
        self.label2 = ttk.Label(self.root,text="Metodo Set (tk): ")
        self.label2.grid(row=1,column=0)
    
    def crear_botones(self):
        self.boton1 = ttk.Button(self.root,text="Insert",command=lambda:self.metodo_insert())
        self.boton1.grid(row=2,column=0)
        self.boton2 = ttk.Button(self.root,text="Set",command=lambda:self.metodo_set())
        self.boton2.grid(row=2,column=1)

    def metodo_insert(self):
        self.entry1.insert(0,"Texto Por Defecto")
        self.entry2.insert(0,"Texto Por Defecto")

    def metodo_set(self):
        textEntry = tk.StringVar()
        textEntry.set("Texto por Defecto")
        self.entry2.config(textvariable=textEntry)

if __name__ == "__main__":
    app = Entry_Defecto()
    app.root.mainloop()