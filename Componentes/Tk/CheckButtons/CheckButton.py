import tkinter as tk
from tkinter import ttk

class App :
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.config(bd=10)
        self.root.title("Ingredients")
        self.root.resizable(0,0)

        label = ttk.Label(self.root,text="How do you want the Pizza?")
        label.grid(row=0,column=0)

        self.create_checkbuttons() 
        self.temp_label = ttk.Label(self.root,text="Ingredients : ")
        self.temp_label.grid(row=2,column=0)
        
    def create_checkbuttons(self):
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=1,columnspan=3)

        self.wpep = tk.IntVar()
        self.wche = tk.IntVar()
        self.wchick = tk.IntVar()

        self.pepperoni = ttk.Checkbutton(self.frame,text="Pepperoni",variable=self.wpep,onvalue=1,offvalue=0,command=lambda:self.selected()).grid(row=0,column=0)
        self.chesee = ttk.Checkbutton(self.frame,text="Chesee",variable=self.wche,onvalue=1,offvalue=0,command=lambda:self.selected()).grid(row=1,column=0)
        self.chicken = ttk.Checkbutton(self.frame,text="Chicken",variable=self.wchick,onvalue=1,offvalue=0,command=lambda:self.selected()).grid(row=2,column=0)

        """
        ¿What are the CheckButtons?
        ----------------------------
        Check buttons are multi-choice buttons for multiple answers

        onvalue
        -------

        When the checkbutton is on, or when is active.

        offvalue
        --------

        When the checkbutton is off, or when is not active

        ---------------------------------------------------------------------------------------
        We have to declare a variable that contain the number when the checkbutton is on or off.

        You have to use tk.IntVar() or Could be tk.StringVar() if you want contain a stringvar when the checkbutton is on or off. 
        But is easier with numbers.

        Like :

        wpep = tk.IntVar()
        wche = tk.IntVar()
        wchick = tk.IntVar()

        """

    def selected(self):
        
        ingredients = ""

        if self.wpep.get() == 1:
            ingredients += " Pepperoni"
        
        if self.wche.get() == 1:
            ingredients += " Chesee"

        if self.wchick.get() == 1:
            ingredients += " Chicken"
        
        self.temp_label.config(text="Ingredients : " + ingredients)
  
app = App()
app.root.mainloop()