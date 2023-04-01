import tkinter as tk
from tkinter import ttk, messagebox


class Tabuladores():
    def __init__(self) -> None:
        self.ventana = tk.Tk()
        self.ventana.geometry('600x400')
        self.ventana.title('Componentes')
        self.ventana.rowconfigure(0,weight=1)
        self.ventana.columnconfigure(0,weight=1)
        self.crear_tabs()
        self.crear_etiqueta()
        self.crear_boton()
        self.crear_entry()
        self.ventana.mainloop()

    def crear_tabs(self):
        self.control_tabulador = ttk.Notebook(self.ventana)
        self.control_tabulador.grid(row=0,column=0,sticky="news")

        self.tabulador1 = ttk.Frame(self.control_tabulador)
        self.control_tabulador.add(self.tabulador1, text='Tabulador 1')
        self.tabulador1.configure(borderwidth=10)
        self.tabulador1.rowconfigure([0,1],weight=1)
        self.tabulador1.columnconfigure([0,1],weight=1)

    def crear_etiqueta(self):
        self.etiqueta1 = ttk.Label(self.tabulador1, text='Nombre :')
        self.etiqueta1.grid(row=0, column=0, sticky=tk.E)

    def crear_entry(self):
        self.entrada1 = ttk.Entry(self.tabulador1, width=30)
        self.entrada1.grid(row=0, column=1, padx=5, pady=5,sticky="w")
        self.entrada1.bind("<Return>",self.evento)

    def evento(self,event):
        self.enviar()

    def crear_boton(self):
        self.boton1 = ttk.Button(self.tabulador1, text='Enviar', command=self.enviar,cursor="hand2")
        self.boton1.grid(row=1, column=0, columnspan=2,sticky="n")
    
    def enviar(self):
        if self.entrada1.get().strip():
            messagebox.showinfo('Mensaje', f'Nombre : {self.entrada1.get()}')
            self.entrada1.delete(0,"end")
        else:
            messagebox.showerror("Error","Debes ingresar un Nombre")

Tabuladores()