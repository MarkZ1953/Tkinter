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
            "C": (0, 0),
            "C": (0, 0),
            "C": (0, 0),
            "C": (0, 0),
            "C": (0, 0),
            "C": (0, 0),
            "C": (0, 0),
            "C": (0, 0),
            "C": (0, 0),
            "C": (0, 0),
        }

        for texto_boton, posicion in botones.items():
            boton = ctk.CTkButton(self.frame2, text=texto_boton)

        for i in range(2):
            bton = ctk.CTkButton(self.frame2, text=nom_botones[i], cursor="hand2", corner_radius=0, border_width=1,
                                 border_color="white", fg_color="#eee", text_color="grey", font=("Calibri", 25),
                                 hover_color="#eee", command=lambda k=nom_botones[i]: self.boton_pulsado(k))
            if i == 0:
                bton.grid(row=0, columnspan=3, sticky="nswe", padx=1, pady=1)
            else:
                bton.grid(row=0, column=3, sticky="nswe", padx=1, pady=1)

        for i in range(3):
            for j in range(4):
                bton = ctk.CTkButton(self.frame2, text=nom_botones[c], cursor="hand2", corner_radius=0, border_width=1,
                                     border_color="white", fg_color="white", text_color="grey", font=("Calibri", 25),
                                     hover_color="#eee", command=lambda k=nom_botones[c]: self.boton_pulsado(k))
                bton.grid(row=i + 1, column=j, sticky="nswe", padx=1, pady=1)
                if j == 3:
                    bton.configure(fg_color="#eee")
                c += 1
        c = 14
        for i in range(3):
            bton = ctk.CTkButton(self.frame2, text=nom_botones[c], cursor="hand2", corner_radius=0, border_width=1,
                                 border_color="white", fg_color="white", text_color="grey", font=("Calibri", 25),
                                 hover_color="#eee", command=lambda k=nom_botones[c]: self.boton_pulsado(k))
            if i == 0:
                bton.grid(row=4, columnspan=2, sticky="nswe", padx=1, pady=1)
            else:
                bton.grid(row=4, column=i + 1, sticky="nswe", padx=1, pady=1)
            c += 1

            if c == 17:
                bton.configure(fg_color="#084474", text_color="white", hover_color="#1c5484")
            elif c == 16:
                bton.configure(fg_color="#eee")
