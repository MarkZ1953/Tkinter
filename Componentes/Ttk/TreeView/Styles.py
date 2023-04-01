import tkinter as tk
from tkinter import ttk
from Info import*

class App:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.create_tree()
    
    def create_tree(self):
        style = ttk.Style()

        style.theme_use("winnative") #Clam,default,alt
        print(style.theme_names())

        """
            If you want to add all this changes, you have to use a theme
        """

        style.configure("Treeview",
            background = "#d6dce5",
            foreground = "black",
            rowheight = 25,
            fieldbackground = "#d6dce5"
        )
        
        style.map("Treeview",background = [("selected","#609cd4")])

        self.tree = ttk.Treeview(self.root,height=35,columns=("#1","#2","#3")) 
        self.tree.grid(row=0,column=0,padx=10,pady=10) 

        name_heads = ["#0","#1","#2","#3"]
        name_column = ["Id","Name","Last Name","Age"]

        for i in range(4):
            self.tree.heading(name_heads[i],text=name_column[i],anchor="center")
            self.tree.column(name_heads[i],anchor="center")

        for person in persons:
            self.tree.insert("","end",text=person[0],values=(person[1],person[2],person[3]))


app = App()
app.root.mainloop()