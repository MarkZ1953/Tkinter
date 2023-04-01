import tkinter as tk

class LabelFrame:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Label Frame")
        self.root.resizable(0,0)
        self.root.rowconfigure([0,1],weight=1)
        self.root.columnconfigure(0,weight=1)
        self.crear_marco1()
        self.crear_marco2()
        self.crear_marco3()
        self.crear_entry()
        self.crear_boton()
        self.root.mainloop()

    def crear_marco1(self):
        self.marco_1 = tk.LabelFrame(self.root,text="Entrada de datos", padx=20, pady=20)
        self.marco_1.grid(row=0, column=0,padx=15, pady=15)

    def crear_marco2(self):
        self.marco_2 = tk.LabelFrame(self.root,text="Enviar", padx=20, pady=20)
        self.marco_2.grid(row=1, column=0, padx=5, pady=15)

    def crear_marco3(self):
        self.marco_3 = tk.LabelFrame(self.root,text="Resultado", padx=20, pady=20)
        self.marco_3.grid(row=0, column=1, padx=5, pady=15)

    def crear_entry(self):
        self.entrada = tk.Entry(self.marco_1,background="springgreen",border=5,foreground="red",width=30)
        self.entrada.pack()
        self.entrada.insert(0,"Escriba su nombre...")
        self.entrada.bind("<Button-1>", lambda e: self.entrada.delete(0,"end"))

    def crear_boton(self):       
        self.boton = tk.Button(self.marco_2,text="Enviar",command=self.enviar,background="deepskyblue",border=3,width=26,cursor="hand2").pack()

    def enviar(self):
        self.nombre = self.entrada.get() 
        tk.Label(self.marco_3,text=f"Hola {self.nombre}",background="skyblue",width=27).pack()
        self.entrada.delete(0,"end")
        self.entrada.insert(0,"Escriba su nombre...")

LabelFrame()