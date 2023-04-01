import tkinter as tk

class App:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root,width=600,height=400,background="black")
        self.canvas.grid(row=0,column=0)
        self.canvas.bind("<ButtonPress-1>",self.boton_presion)
        self.canvas.bind("<Motion>",self.mover_mouse)
        self.canvas.bind("<ButtonRelease-1>",self.boton_soltar)
        self.presionado = False
    
    def boton_presion(self,evento):
        self.presionado = True
        self.origenx = evento.x
        self.origeny = evento.y
    
    def mover_mouse(self,evento):
        if self.presionado:
            self.canvas.create_line(self.origenx,self.origeny,evento.x,evento.y,fill="red")
            self.origenx = evento.x
            self.origeny = evento.y
    
    def boton_soltar(self,evento):
        self.presionado = False

app = App()
app.root.mainloop()