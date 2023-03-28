import tkinter as tk
import customtkinter as ctk


def centerwindows(ventana, width, height):
    width_window = ventana.winfo_screenwidth()
    height_window = ventana.winfo_screenheight()

    x = int((width_window // 2) - (width // 2))
    y = int((height_window // 2) - (height // 2))

    ventana.geometry("{}x{}+{}+{}".format(width, height, x, y))


class Layout_Calculadora:
    def __init__(self) -> None:
        self.root = ctk.CTk()
        self.root.title("Calculadora")
        centerwindows(self.root, 400, 635)
        self.root.config(bd=5)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure([0, 1], weight=1)
        self.text_btons = tk.StringVar()
        self.temp = ""
        self.crear_frame1()
        self.crear_frame2()
        self.crear_botones()
        self.crear_pantalla()
        self.root.mainloop()

    def crear_frame1(self):
        self.frame1 = ctk.CTkFrame(self.root, fg_color="black")
        self.frame1.grid(row=0, column=0, sticky="news")
        self.frame1.columnconfigure(0, weight=1)
        self.frame1.rowconfigure(0, weight=1)

    def crear_pantalla(self):
        self.pantalla = ctk.CTkEntry(self.frame1, corner_radius=0, justify="right", font=("Calibri", 40),
                                     textvariable=self.text_btons, state=["readonly"])
        self.pantalla.grid(row=0, column=0, sticky="nswe")

    def crear_frame2(self):
        self.frame2 = ctk.CTkFrame(self.root, fg_color="grey")
        self.frame2.grid(row=1, column=0, sticky="nswe")
        self.frame2.columnconfigure([0, 1, 2, 3], weight=1)
        self.frame2.rowconfigure([0, 1, 2, 3, 4], weight=1)

    def crear_botones(self):
        nom_botones = ["C", "/", "7", "8", "9", "*", "4", "5", "6", "-", "1", "2", "3", "+", "0", ".", "="]
        c = 2

        botones = {
            "C": (0, 0),
            "/": (0, 3),
            "7": (1, 0),
            "8": (1, 1),
            "9": (1, 2),
            "*": (1, 3),
            "4": (2, 0),
            "5": (2, 1),
            "6": (2, 2),
            "-": (2, 3),
            "1": (3, 0),
            "2": (3, 1),
            "3": (3, 2),
            "+": (3, 3),
            "0": (4, 0),
            ".": (4, 2),
            "=": (4, 3)
        }

        for texto_boton, posicion in botones.items():
            # Creamos los botones
            boton = ctk.CTkButton(self.frame2, text=texto_boton, cursor="hand2", corner_radius=0, border_width=1,
                                  border_color="white", fg_color="white", text_color="grey", font=("Calibri", 25),
                                  hover_color="#eee", command=lambda k=texto_boton: self.boton_pulsado(k))

            # Se hace eso para aplicar los colores respectivos a cada boton
            if texto_boton in ["C", "/", "*", "-", "+", "."]:
                boton.configure(fg_color="#eee")
            elif texto_boton == "=":
                boton.configure(fg_color="#084474", text_color="white", hover_color="#1c5484")

            # Se separan los grid ya que el boton "C" y "0" son mas grandes que los demas
            if texto_boton == "C":
                boton.grid(row=0, columnspan=3, sticky="news", padx=1, pady=1)
            elif texto_boton == "0":
                boton.grid(row=4, columnspan=2, sticky="news", padx=1, pady=1)
            else:
                boton.grid(row=posicion[0], column=posicion[1], sticky="news", padx=1, pady=1)
