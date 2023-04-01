import tkinter as tk

def centerwindows(ventana,width,height):

    width_window = ventana.winfo_screenwidth()
    height_window = ventana.winfo_screenheight()

    x = int((width_window // 2) - (width // 2))
    y = int((height_window // 2) - (height // 2))

    ventana.geometry("{}x{}+{}+{}".format(width,height,x,y))
