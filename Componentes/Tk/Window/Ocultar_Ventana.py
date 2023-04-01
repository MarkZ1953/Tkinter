import tkinter as tk
from tkinter import font

class Ocultar_Ventana:

    def __init__(self) -> None:

        self.root = tk.Tk()
        self.root.config(border=10)
        self.root.title("Ocultar Ventana")
        self.root.geometry("800x500+350+200")
        self.root.rowconfigure([0,1,2],weight=1)
        self.root.columnconfigure(0,weight=1)
        self.crear_frame()
        self.crear_widgets()
        self.root.mainloop()

    def crear_frame(self):
        
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=1,column=0)
        self.frame.rowconfigure(0,weight=0)
        self.frame.columnconfigure([0,1],weight=0)

    def crear_widgets(self):

        titulo = tk.Label(self.root, text="Ocultar Ventana", font=("Arial", 18))
        titulo.grid(row=0,columnspan=3,sticky="n",pady=10)

        btnadmin = tk.Button(self.frame, text="Administrador", command=self.admin,cursor="hand2")
        btnadmin.grid(row=0,column=0,pady=10,padx=10)

        btnencarg = tk.Button(self.frame, text="Encargado", command=self.encarg,cursor="hand2")
        btnencarg.grid(row=0,column=1,pady=10,padx=10)

        btnsalir = tk.Button(self.root, text="Salir", command=self.salir,cursor="hand2",width=10)
        btnsalir.grid(row=2,column=0,pady=10,padx=10,sticky="s")


    def admin(self):

        user1 = tk.Toplevel(self.root)
        user1.title("Administrador")
        user1.geometry("500x500+500+200")
        user1.resizable(0, 0)
        # ventana.destroy() No la destruyas, mejor ocultala
        self.root.withdraw()# Ocultala

        a_boton1 = tk.Button(user1, text="Ingresar")
        a_boton1.place(x=220, y=300)

        a_boton2 = tk.Button(user1, text="Regresar", command=lambda:self.atras(user1))
        a_boton2.place(x=220, y=400)

        t_user = tk.Entry(user1)
        t_user.place(x=180, y=100)
        l_user = tk.Label(user1, text="USUARIO:")
        l_user.place(x=210, y=70)

        t_pass = tk.Entry(user1)
        t_pass.place(x=180, y=200)
        l_pass = tk.Label(user1, text="CONTRASEÑA:")
        l_pass.place(x=200, y=170)


    def salir(self):
        self.root.destroy()

    def atras(self,ventana_a_cerrar):
        ventana_a_cerrar.destroy()
        self.root.deiconify()

    def admin(self):

        user1 = tk.Toplevel(self.root)
        user1.title("Administrador")
        user1.geometry("500x500+500+200")
        user1.resizable(0, 0)
        # ventana.destroy() No la destruyas, mejor ocultala
        self.root.withdraw()# Ocultala

        a_boton1 = tk.Button(user1, text="Ingresar")
        a_boton1.place(x=220, y=300)

        a_boton2 = tk.Button(user1, text="Regresar", command=lambda:self.atras(user1))
        a_boton2.place(x=220, y=400)

        t_user = tk.Entry(user1)
        t_user.place(x=180, y=100)
        l_user = tk.Label(user1, text="USUARIO:")
        l_user.place(x=210, y=70)

        t_pass = tk.Entry(user1)
        t_pass.place(x=180, y=200)
        l_pass = tk.Label(user1, text="CONTRASEÑA:")
        l_pass.place(x=200, y=170)

    def encarg(self):

        user2 = tk.Tk()
        user2.title("Encargado")
        user2.geometry("500x500+500+200")
        user2.resizable(0,0)
        # ventana.destroy() No la destruyas
        self.root.withdraw() # Ocultala

        e_a_boton1 = tk.Button(user2, text="Ingresar")
        e_a_boton1.place(x=220, y=300)

        e_a_boton2 = tk.Button(user2, text="Regresar",command=lambda:self.atras(user2))
        e_a_boton2.place(x=220, y=400)

        e_t_user = tk.Entry(user2)
        e_t_user.place(x=180, y=100)

        e_l_user = tk.Label(user2, text="USUARIO:")
        e_l_user.place(x=210, y=70)

        e_t_pass = tk.Entry(user2)
        e_t_pass.place(x=180, y=200)

        e_l_pass = tk.Label(user2, text="CONTRASEÑA:")
        e_l_pass.place(x=200, y=170)

Ocultar_Ventana()