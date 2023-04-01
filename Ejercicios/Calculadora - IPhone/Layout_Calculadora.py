import customtkinter as ctk
from tkinter import ttk
import tkinter as tk

class Layout_Calculadora:
    """
    Esta clase solo tiene el layout de la calculadora de Iphone pero no tiene ninguna funcionalidad.
    """
    def colores(self):
        self.color_naranja = "#f89c04"
        self.color_gris = "#383434"
        self.color_gris_claro = "#9c9c9c"

    def __init__(self) -> None:
        self.root = ctk.CTk()
        self.colores()
        self.root.geometry("400x635")
        self.root.config(background="black",bd=10)
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure([0,1],weight=1)
        self.crear_frame1()
        self.crear_frame2()
        self.crear_pantalla()
        self.crear_botones()
        self.root.mainloop()
    
    def crear_frame1(self):
        pass

    def crear_frame2(self):
        self.frame2 = ctk.CTkFrame(self.root,fg_color="black",bg_color="black")
        self.frame2.grid(row=1,column=0,sticky="news")
        self.frame2.columnconfigure([0,1,2,3],weight=1)
        self.frame2.rowconfigure([0,1,2,3,4],weight=1)

    def crear_pantalla(self):
        pass
    
    def crear_botones(self):
        text_btons = ["AC","+/-","%","÷","7","8","9","x","4","5","6","-","1","2","3","+","0","0",",","="]
        c = 0
        for row in range(5):
                for col in range(4):
                    if row == 4 and col == 1:
                        bton.grid(row=row,columnspan=2,sticky="news",padx=5,pady=5)
                    else:
                        bton = ctk.CTkButton(self.frame2,text=text_btons[c],corner_radius=200,width=80,height=28,border_width=0,border_spacing=0,cursor="hand2",fg_color=self.color_gris,font=("Calibri",35))
                        bton.grid(row=row,column=col,sticky="news",padx=5,pady=5)

                    if col == 3:
                        bton.configure(fg_color=self.color_naranja) 
                    if row == 0 and col <= 2:
                        bton.configure(fg_color=self.color_gris_claro) 
                    if row == 0 and col <= 2:
                        bton.configure(text_color="black")
                      
                    c += 1 

Layout_Calculadora()