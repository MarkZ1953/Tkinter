import tkinter as tk
from tkinter import ttk

class Text:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.config(bd=10)
        self.crear_label()
        self.crear_text()
        self.crear_scrollbar()

    def crear_label(self):
        self.label = ttk.Label(self.root,text="Ingrese un texto : ")
        self.label.grid(row=0,column=0)

    def crear_text(self):
        self.text = tk.Text(self.root,font=("Arial",10),width=30,height=10)
        self.text.grid(row=0,column=1)
    
    def crear_scrollbar(self):
        self.scroll = tk.Scrollbar(self.root,command=self.text.yview)
        self.scroll.grid(row=0,column=2,sticky="nsew")
        self.text.config(yscrollcommand=self.scroll.set)

if __name__ == "__main__":
    app = Text()
    app.root.mainloop()