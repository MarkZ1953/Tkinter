import tkinter as tk
from tkinter import ttk
from Info import * #Module Info.py
from tkinter import messagebox

class Tree:
    def __init__(self) -> None:
        self.root = tk.Tk() 
        self.root.config(bd=10)
        self.root.title("Scroll Bar")
        
        #--------------------- TreeView -----------------------#

        self.tree = ttk.Treeview(self.root,columns=("#1","#2","#3")) 
        self.tree.grid(row=0,column=0,padx=10,pady=10) 

        name_heads = ["#0","#1","#2","#3"]
        name_column = ["Id","Name","Last Name","Age"]

        for i in range(4):
            self.tree.heading(name_heads[i],text=name_column[i],anchor="center")
            self.tree.column(name_heads[i],anchor="center")

        #-------------------------------------------------------#

        #-------Adding Information from module Info.py----------#

        for person in persons:
            self.tree.insert("","end",text=person[0],values=(person[1],person[2],person[3]))

        #-------------------------------------------------------#

        #---------- Configure the ScrollBar in the TreeView -----#

        scroll = ttk.Scrollbar(self.root,command=self.tree.yview) #This scrollbar is vertical, with the option .yview or .xview
        scroll.grid(row=0,column=2,sticky="nsew",pady=10) #Put the scrollbar on the right of the Treeview
        self.tree.config(yscrollcommand=scroll.set) #The scrollbar follow the cursor, when we scroll up or down

        #--------------------------------------------------------#

        self.root.mainloop()

app = Tree()