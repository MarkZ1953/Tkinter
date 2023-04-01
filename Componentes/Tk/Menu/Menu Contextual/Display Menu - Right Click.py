import tkinter as tk

class App:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("360x360")
        self.create_menu()
        self.root.bind("<Button-3>",self.display_menu) 

    def create_menu(self):
        self.m = tk.Menu(self.root, tearoff = 0) 
        self.m.add_command(label ="Cut") 
        self.m.add_command(label ="Copy") 
        self.m.add_command(label ="Paste") 
        self.m.add_command(label ="Reload") 
        self.m.add_separator() 
        self.m.add_command(label ="Rename") 
    
    def display_menu(self,event): 
        try: 
            self.m.tk_popup(event.x_root, event.y_root) 
        finally: 
            self.m.grab_release() 

app = App()
app.root.mainloop()