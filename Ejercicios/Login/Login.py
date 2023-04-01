from tkinter import Tk
from tkinter.ttk import Label, Button, Entry
from tkinter import messagebox


class Login(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.my_entries = []

        # Algunas configuraciones de la ventana principal
        self.title("Login")
        self.geometry("300x130")
        self.config(bd=10)
        self.resizable(False, False)

        # Llamamos al método que crea los widgets
        self.create_widgets()

    def create_widgets(self):

        texts = ["User :", "Password :"]

        for i in range(2):
            Label(self, text=texts[i]).grid(row=i, column=0, sticky="e", padx=10, pady=5)

            entry = Entry(self, show="*", width=28)
            entry.grid(row=i, column=1, padx=10, pady=5)

            if i == 0:
                entry.config(show="")

            self.my_entries.append(entry)

        Button(self, cursor="hand2", text="Login", command=self.showinfo).grid(row=3, columnspan=3,
                                                                               padx=10, pady=5)

    def showinfo(self):
        info = []

        for entry in self.my_entries:
            info.append(entry.get())

        self.limpiar_campos()
        messagebox.showinfo(title="Information", message=f"User : {info[0]}\nPassword : {info[1]}")

    def limpiar_campos(self):
        for entry in self.my_entries:
            entry.delete(0, "end")


if __name__ == "__main__":
    app = Login()
    app.mainloop()
