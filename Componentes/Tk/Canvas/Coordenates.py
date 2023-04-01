import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root,width=600,height=400,background="black")
        self.canvas.grid(row=0,column=0)
        self.canvas.bind("<Motion>",self.mover_mouse)
        self.canvas.bind("<Double-Button-1>",self.presion_mouse) #<Button-1>
    
    def mover_mouse(self,evento):
        self.root.title(str(evento.x) + " - " + str(evento.y))
    
    def presion_mouse(self,evento):
        self.canvas.create_oval(evento.x-5,evento.y-5,evento.x+5,evento.y+5,fill="red")

app = App()
app.root.mainloop()