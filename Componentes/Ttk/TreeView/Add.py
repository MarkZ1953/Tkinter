import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Tree:
    def __init__(self) -> None:
        self.root = tk.Tk() 
        self.root.config(bd=10)
        self.root.title("Add Records")
        self.create_widgets()
        self.root.mainloop()
    
    def create_widgets(self):

        #---------------------- Create a Frame and Entrys ------------------------#

        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0,columnspan=4)

        texts = ["Id :","Name :","Last Name :","Age :"]
        my_entries = []

        for i in range(4):
            self.label = ttk.Label(self.frame,text=texts[i])
            self.label.grid(row = i,column=0,sticky="e",padx=10)

            self.entry = ttk.Entry(self.frame)
            self.entry.grid(row=i,column=1,pady=10)

            my_entries.append(self.entry)

        #------------------------------------------------------#

        #--------------------- TreeView -----------------------#

        self.tree = ttk.Treeview(self.root,columns=("#1","#2","#3")) 
        self.tree.grid(row=1,columnspan=4,padx=10,pady=10) #Configure the grid layout
        
        """
        hide a column
        -------------
        If you want to hide a column you could put :

        stretch = NO

        treeview head 
        --------------

        self.name_treeview.heading("name_column",text="name_head",anchor="center") <-- Center the head. you can use "center"

        treeview column
        ----------------

        self.name_treeview.column("name_column",anchor="center") <-- Center the records in the columns.

        Example : 

        self.tree.heading("#0",anchor="center",text="Id")  <-- We have to do this for put a name in the head of the column
        self.tree.column("#0",anchor="center") <-- With this we center the records of the column.
        
        """

        name_heads = ["#0","#1","#2","#3"]
        name_column = ["Id","Name","Last Name","Age"]

        #Add the head name and center the record of the columns with a for

        for i in range(4):
            self.tree.heading(name_heads[i],text=name_column[i],anchor="center")
            self.tree.column(name_heads[i],anchor="center")

        #-------------------------------------------------------#

        #---------------- Create Buttons ----------------#

        self.btondel = ttk.Button(self.root,cursor="hand2",text="Add Record",command=lambda:self.add(my_entries))
        self.btondel.grid(row=2,columnspan=4)

        #------------------------------------------------#

    def add(self,entries):
        info = []
        for entry in entries:
            info.append(entry.get())
        
        self.tree.insert("","end",text=info[0],values=(info[1],info[2],info[3]))

app = Tree()