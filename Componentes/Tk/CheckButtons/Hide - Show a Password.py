import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Login:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("400x130")
        self.root.config(bd=10)
        self.root.title("Login")
        self.root.resizable(0,0)
        self.create_widgets()

    def create_widgets(self):
        
        texts = ["User :","Password :"]
        self.my_entries = []

        for i in range(2):
            self.label = ttk.Label(self.root,text=texts[i])
            self.label.grid(row=i,column=0,sticky="e",padx=10,pady=5)

            self.entry = ttk.Entry(self.root,show="*",width=28)
            self.entry.grid(row=i,column=1,padx=10,pady=5)

            self.vsoh = tk.IntVar()
            self.password = self.entry

            if i == 0:
                self.entry.config(show="")

            self.my_entries.append(self.entry)

        self.sohpassw = ttk.Checkbutton(self.root,text="Show Password",variable=self.vsoh,onvalue=1,offvalue=0,command=lambda:self.show_hide()).grid(row=1,column=2)

        self.bton = ttk.Button(self.root,cursor="hand2",text="Login",command=lambda:self.showinfo())
        self.bton.grid(row=3,columnspan=3,padx=10,pady=5)

    def showinfo(self):
        info = []
        
        for entry in self.my_entries:
            info.append(entry.get())
            
        self.clean()
        messagebox.showinfo("Information","User : {}\nPassword : {}".format(info[0],info[1]))

    def clean(self):
        for entry in self.my_entries:
            entry.delete(0,"end")

    def show_hide(self):
        if self.vsoh.get() == 1:
            self.password.config(show="")

        if self.vsoh.get() == 0:
            self.password.config(show="*")

if __name__ == "__main__":
    login = Login()
    login.root.mainloop()