import tkinter as tk
from tkinter import ttk
import time

class Button:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.crear_label()
        self.crear_boton()

    def crear_boton(self):
        self.boton = ttk.Button(self.root,text="Presioname",cursor="hand2",command=lambda:self.saludar())
        self.boton.pack()
    
    def crear_label(self):
        self.label = ttk.Label(self.root,text="")
        self.label.pack()

    def saludar(self):
        self.label.config(text="Hola como estas?")       

if __name__ == "__main__":
    app = Button()
    app.root.mainloop()