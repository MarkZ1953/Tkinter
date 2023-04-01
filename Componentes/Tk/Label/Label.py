import tkinter as tk
from tkinter import ttk
import os

class Label:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.rowconfigure([0,1],weight=1)
        self.root.title("Label")
        self.crear_frame()
        self.crear_label()

    def crear_frame(self):
        self.frame = tk.Frame(self.root)
        self.frame.grid(sticky="news")
    
    def crear_label(self):
        self.label = tk.Label(self.frame,text="Hola este es un texto en Python",fg="red",font=("Comic Sans MS",18))
        self.label.grid(row=0,column=0,sticky="news")
    
if __name__ == "__main__":
    app = Label()
    app.root.mainloop()