import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

class Scrolled_Text:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.config(bd=10)
        self.crear_label()
        self.crear_scrolledtext()
    
    def crear_label(self):
        self.label = ttk.Label(self.root,text="Ingrese un texto : ")
        self.label.grid(row=0,column=0)

    def crear_scrolledtext(self):
        self.scroll_text = ScrolledText(self.root,width = 30,height = 10)
        self.scroll_text.grid(row=0,column=1)

if __name__ == "__main__":
    app = Scrolled_Text()
    app.root.mainloop()