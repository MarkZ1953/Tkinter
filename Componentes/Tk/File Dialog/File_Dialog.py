import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class FileDialog:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.create_button()

    def create_button(self):
        self.bton = ttk.Button(self.root,text="Open Dialog",command=lambda:self.open())
        self.bton.grid(row=0,column=0)

    def open(self):
        file = filedialog.askopenfilename(title="Open",initialdir="Desktop",
        filetypes=(
            ("Archivos Excel","*.xlsx"),
            ("Arhivos de Texto","*.txt"),
            ("Todos los Arhivos","*.*")
            ))
        print(file)

app = FileDialog()
app.root.mainloop()