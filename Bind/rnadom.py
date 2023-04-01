import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class AppPulsar:
    def __init__(self) -> None:
        self.root = tk.Tk()

        self.root.bind("<Delete>",self.click)

        self.root.mainloop()
    
    def click(self,event):
        print(event.char)

app = AppPulsar()