from tkinter import messagebox
from Layout_Calculadora import Layout_Calculadora


class Calculadora(Layout_Calculadora):
    def __init__(self) -> None:
        super().__init__()
        self.resultado = None

    def boton_pulsado(self, boton):
        if boton == "C":
            self.pantalla.delete(0, "end")
            self.temp = ""
            self.text_btons.set(self.temp)
        elif boton == "=":
            try:
                if self.temp:
                    self.resultado = str(eval(self.text_btons.get()))
                    self.text_btons.set(self.resultado)
            except Exception as e:
                messagebox.showerror("Error", f"Ha ocurrido un error : {e} ")
                self.text_btons.set("")
                self.pantalla.delete(0, "end")
            finally:
                self.temp = self.resultado
        else:
            self.temp = f"{self.temp}{boton}"
            self.text_btons.set(self.temp)
            #Comentario


if __name__ == "__main__":
    Calculadora()
