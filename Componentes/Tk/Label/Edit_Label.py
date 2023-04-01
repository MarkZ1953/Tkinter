import tkinter as tk

class Edit_Label():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.minsize(120,120)
        self.root.config(bd=10)
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure([0,1,2],weight=1)
        self.crear_etiqueta()
        self.crear_boton()
        self.crear_entry()

    def crear_entry(self):
        self.entry = tk.Entry(self.root)
        self.entry.grid(row=0,column=0,padx=10,pady=10)
        self.entry.focus()

    def crear_boton(self):
        self.bton = tk.Button(self.root,text = "Aceptar",cursor="hand2",command=lambda:self.mostrar())
        self.bton.grid(row=1,column = 0)

    def crear_etiqueta(self):
        self.etiqueta = tk.Label(self.root,text="Etiqueta")
        self.etiqueta.grid(row=2,column = 0,pady=10,padx=10)

    def mostrar(self):
        self.etiqueta.config(text=f"Etiqueta\n{self.entry.get()}")

if __name__ == "__main__":
    app = Edit_Label()
    app.root.mainloop()