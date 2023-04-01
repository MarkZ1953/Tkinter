from io import open
import customtkinter as ctk
from tkinter import filedialog

class Layout_Editor:
    def __init__(self) -> None:
        self.root = ctk.CTk()
        self.root.title("Editor de Texto")
        self.root._set_appearance_mode("dark")
        self.root.config(border=20)
        self.root.minsize(500,500)
        self.centerwindows(800,500)
        self.root.columnconfigure(0,weight=0)
        self.root.columnconfigure(1,weight=1)
        self.root.rowconfigure(0,weight=1)
        self.crear_menu()
        self.crear_frame()
        self.crear_frame2()
        self.crear_botones()
        self.crear_caja()
        self.root.mainloop()
    
    def crear_frame(self):
        self.frame = ctk.CTkFrame(self.root,bg_color="#282424",corner_radius=10,fg_color="#eee")
        self.frame.grid(row=0,column=0,sticky="news",padx=10)
        self.frame.columnconfigure(0,weight=1)
        self.frame.rowconfigure([0,1,2],weight=0)
    
    def crear_botones(self):
        k = ""
        textos = ["Abrir","Guardar","Guardar Como..."]
        for i in range(3):
            bton = ctk.CTkButton(self.frame,text=textos[i],cursor="hand2",corner_radius=10,command=lambda k = textos[i]:self.funciones(k))
            bton.grid(row=i,column=0,pady=20,padx=20,sticky="ew")
    
    def crear_menu(self):
        pass
    
    def crear_frame2(self):
        self.frame2 = ctk.CTkFrame(self.root,bg_color="#282424",corner_radius=10)
        self.frame2.grid(row=0,column=1,sticky="news",padx=10)
        self.frame2.columnconfigure(0,weight=1)
        self.frame2.rowconfigure(0,weight=1)
    
    def crear_caja(self):
        self.caja_texto = ctk.CTkTextbox(self.frame2,bg_color="#282424",corner_radius=10,font=("sans serif",20))
        self.caja_texto.grid(row=0,column=0,sticky="news")
        self.caja_texto.bind("<Any-KeyPress>",self.evento)

    def centerwindows(self,width,height):
        width_window = self.root.winfo_screenwidth()
        height_window = self.root.winfo_screenheight()

        x = int((width_window // 2) - (width // 2))
        y = int((height_window // 2) - (height // 2))

        self.root.geometry("{}x{}+{}+{}".format(width,height,x,y))

class Editor(Layout_Editor):
    def __init__(self) -> None:
        super().__init__()
        self.archivo_abierto = False
        self.archivo = None

    def funciones(self,opcion):
        if opcion == "Abrir":
            self.abrir()
        elif opcion == "Guardar":
            try:
                self.guardar()
            except AttributeError:
                self.guardar_como()
        else:
            self.guardar_como()

    def guardar_como(self):

        self.archivo = filedialog.asksaveasfilename(title="Guardar",defaultextension="txt",filetypes=[
            ("Arhivos de Texto(.txt)","*.txt"),
            ("Todos los Archivos","*.*")
            ])

        if not self.archivo:
            return
        
        with open(self.archivo,"w") as self.archivo:
            texto = self.caja_texto.get(1.0,"end")
            self.archivo.write(texto)
            self.root.title(f"Editor de Texto - {self.archivo.name}")

    def evento(self,e):
        try:
            self.root.title(f"Editor de Texto - {self.archivo.name}")
        except AttributeError:
            self.root.title("*Editor de Texto")
    
    def guardar(self):
        if self.archivo_abierto:
            with open(self.archivo_abierto.name,"w") as self.archivo:
                texto = self.archivo.write(f"{self.caja_texto.get(1.0,'end')}")
                self.root.title(f"Editor de Texto - {self.archivo.name}")
                self.archivo.close()
        else:
            self.guardar_como()
    
    def abrir(self):
        self.archivo_abierto = filedialog.askopenfile(mode="r+")
        self.caja_texto.delete("1.0","end")

        if not self.archivo_abierto:
            return

        with open(self.archivo_abierto.name,"r+") as self.archivo:
            self.caja_texto.insert("1.0",self.archivo.read())
            self.root.title(f"Editor de Texto - {self.archivo.name}")

Editor()    