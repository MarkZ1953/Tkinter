import tkinter as tk
from tkinter import ttk
from Info import * #Module Info.py
from tkinter import messagebox

class Tree:
    def __init__(self) -> None:
        self.root = tk.Tk() 
        self.root.config(bd=10)
        self.root.title("Update Records")
        self.create_tree()
        self.create_entries()
        self.create_buttons()
    

    def create_entries(self):
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0,columnspan=4)

        texts = ["Id :","Name :","Last Name :","Age :"]
        self.my_entries = []

        for i in range(4):
            
            self.label = ttk.Label(self.frame,text=texts[i])
            self.label.grid(row = i,column=0,sticky="e",padx=10)
            
            self.entry = ttk.Entry(self.frame)
            self.entry.grid(row=i,column=1,pady=10)

            if i == 1:
                self.entry.focus()

            self.my_entries.append(self.entry)
        
        self.id = self.my_entries[0]
        self.id.config(state=["readonly"])

    def create_tree(self):

        self.tree = ttk.Treeview(self.root,columns=("#1","#2","#3")) 
        self.tree.grid(row=1,column=0,padx=10,pady=10) #Configure the grid layout

        name_heads = ["#0","#1","#2","#3"]
        name_column = ["Id","Name","Last Name","Age"]

        for i in range(4):
            self.tree.heading(name_heads[i],text=name_column[i],anchor="center")
            self.tree.column(name_heads[i],anchor="center")
   
        #-------Adding Information from module Info.py----------#

        for person in persons:
            self.tree.insert("","end",text=person[0],values=(person[1],person[2],person[3]))

        self.tree.bind("<ButtonRelease-1>",self.click)

        #--------------------------------------------------------#
    
    def create_buttons(self):
        self.btondel = ttk.Button(self.root,cursor="hand2",text="Update",command=lambda:self.update())
        self.btondel.grid(row=2,column=0)

    def update(self):
        info = []
        selected = self.tree.focus()
        for entry in self.my_entries:
            info.append(entry.get())
        self.tree.item(selected,text=info[0],values=(info[1],info[2],info[3]))
        self.clean()
        self.id.config(state=["readonly"])
    
    def click(self,event):
        selected = self.tree.focus()
        records = self.tree.item(selected,"values")
        id = self.tree.item(selected,"text")

        self.clean()
        i = 0

        for entry in self.my_entries:
            if i > 0:
                entry.insert(0,records[i-1])
            else:
                entry.insert(0,id)
                entry.config(state=["readonly"])
            i += 1

    def clean(self):
        for entry in self.my_entries:
            entry.config(state=["normal"])
            entry.delete(0,"end")

app = Tree()
app.root.mainloop()