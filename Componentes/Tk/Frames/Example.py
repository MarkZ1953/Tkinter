import tkinter as tk

class Frame:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.config(bg="red")
        self.crear_frame()

    def crear_frame(self):
        self.frame = tk.Frame(self.root,width=650,height=350,bg="blue",relief="groove",bd=10,cursor="hand2")
        self.frame.pack(fill="y",expand=True) 
        """
        ----------------------------
        side = bottom,left,right,top
        ----------------------------
        Anchor	Description
        N	| North or Top Center
        S	| South or Bottom Center
        E	| East or Right Center
        W	| West or Left Center
        NW	| North West or Top Left
        NE	| North East or Top Right
        SE	| South East or Bottom Right
        SW	| South West or Bottom Left
        _________________________________     
        fill = x,y,both,none
        ---------------------------------
        expand = True o False
        Sirve para permitir que se expanda de la forma en la
        que queremos que lo haga.
        -----------------------------------------------------
        relief = sunken,groove
        Esto es el tipo de borde
        --------------------------
        bd = 10
        Tamaño del borde (Valor entero)
        ---------------------------------
        cursor = "hand2"
        Cambia el tipo de cursor cuanto el mouse se encuentra en el frame.
        -------------------------------------------------------------------
        """
    
if __name__ == "__main__":
    app = Frame()
    app.root.mainloop()