import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Remove_Labels:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Remove Labels")
        self.root.geometry("360x360")
        self.crear_entry()
        self.crear_frame()
        self.crear_boton()

    def crear_label(self):
        self.label = tk.Label(self.root,text="")
        self.label.pack()
    
    def crear_entry(self):
        self.entry = ttk.Entry(self.root)
        self.entry.pack(pady=5,padx=5)
        self.entry.focus()

    def crear_frame(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=5)    

    def crear_boton(self):
        self.boton = ttk.Button(self.frame,text="Aceptar",cursor="hand2",command=lambda:self.mostrar())
        self.boton.grid(row=0,column=0,padx=5)

        self.boton_forget = ttk.Button(self.frame,text="Borrar",cursor="hand2",command=lambda:self.borrar())
        self.boton_forget.grid(row=0,column=1)

        self.boton_destroy = ttk.Button(self.frame,text="Destuir",cursor="hand2",command=lambda:self.destruir_label())
        self.boton_destroy.grid(row=0,column=2,padx=5)

    def mostrar(self):
        self.crear_label()
        self.label.config(text=self.entry.get())
        print(self.label.winfo_exists())

    def borrar(self):
        if self.label.winfo_exists():
            self.label.pack_forget()
        else:
            messagebox.showerror("Error","Primero debes ingresar un texto")
    
    def destruir_label(self):
        if self.label.winfo_exists():
            self.label.destroy()
        else:
            messagebox.showerror("Informacion","Primero debes ingresar un texto")
    
if __name__ == "__main__":
    app = Remove_Labels()
    app.root.mainloop()