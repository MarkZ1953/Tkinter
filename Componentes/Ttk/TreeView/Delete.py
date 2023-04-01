import tkinter as tk
from tkinter import ttk
from Info import * #Module Info.py
from tkinter import messagebox

class Tree:
    def __init__(self) -> None:
        self.root = tk.Tk() 
        self.root.config(bd=10)
        self.root.title("Delete Records")
        
        #--------------------- TreeView -----------------------#

        self.tree = ttk.Treeview(self.root,columns=("#1","#2","#3")) 
        self.tree.grid(row=0,column=0,padx=10,pady=10) #Configure the grid layout

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

        #----------- Create a Frame and Buttons ---------#

        self.frame = tk.Frame(self.root)
        self.frame.grid(row=1,columnspan=3)

        self.btondel = ttk.Button(self.frame,cursor="hand2",text="Delete",command=lambda:self.delete())
        self.btondel.grid(row=0,column=0)

        self.btondelmany = ttk.Button(self.frame,cursor="hand2",text="Delete Many",command=lambda:self.delete_many())
        self.btondelmany.grid(row=0,column=1,padx=10)

        self.btondelall = ttk.Button(self.frame,cursor="hand2",text="Delete All",command=lambda:self.delete_all())
        self.btondelall.grid(row=0,column=2)

        self.btondelall = ttk.Button(self.frame,cursor="hand2",text="Restart Records",command=lambda:self.reset_table())
        self.btondelall.grid(row=0,column=3,padx=10)

        #------------------------------------------------#

        self.root.mainloop()

    def delete(self):
        try:
            selected = self.tree.selection()
            self.tree.delete(selected)
        except :
            messagebox.showerror("Error","If you select many records, you should use Delete Many")

    def delete_many(self):
        selected = self.tree.selection()
        #When you press and the row is blue, you are generating an event calling onclick(), we get this using the method .selection()
        #It gets an id of the row.

        for record in selected: #Selected contains the id of the rows that the user selected and delete or remove the 
            #records one by one with a for.
            self.tree.delete(record)

    def delete_all(self):
        records = self.tree.get_children()
        for record in records:
            self.tree.delete(record)

    def reset_table(self):
        if len(self.tree.get_children()) == 0:
            for person in persons:
                self.tree.insert("","end",text=person[0],values=(person[1],person[2],person[3]))

app = Tree()