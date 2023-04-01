import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class Entries:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Ejemplo Entries")
        self.root.columnconfigure(0,weight=1)
        self.crear_frame()
        self.crear_entries_y_labels()
        self.crear_boton()
        self.crear_scrollbar()
        self.root.mainloop()

    def crear_frame(self):
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0,column=0)

    def crear_entries_y_labels(self):
        textos_labels = ["Nombre","Direccion","Telefono","Correo Electronico","Contraseña","Comentarios"]
        self.entries = []

        for i in range(5):
            tk.Label(self.frame,text=textos_labels[i]).grid(row=i,column=0,padx=10,pady=10,sticky="e")

            entry = tk.Entry(self.frame,width=30)
            entry.grid(row=i,column=1,padx=10,pady=10)

            self.entries.append(entry)
        
        self.entries[0].config(justify="center",foreground="red")
    
    def crear_boton(self):
        boton = tk.Button(self.root,text="Enviar",cursor="hand2",command=lambda:self.codigo_boton())
        boton.grid(row=1,column=0,padx=10,pady=10)

    def codigo_boton(self):
        for entry in self.entries:
            entry.delete(0,tk.END)
        self.scroll.delete(1.0,tk.END)
        
    def crear_scrollbar(self):
        label = tk.Label(self.frame,text="Comentarios")
        label.grid(row=5,column=0,padx=10,pady=10,sticky="e")

        self.scroll=ScrolledText(self.frame)
        self.scroll.grid(row=5,column=1)
        self.scroll.config(width=20,height=5)

Entries()