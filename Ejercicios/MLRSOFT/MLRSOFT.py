from tkinter import Tk, Entry, Label, Button, messagebox
from tkinter.ttk import Treeview
from Pedir_Empleados import centrar_ventana


class MLRSOFT:
    contador_empleados = 1
    AUXILIAR_TRANSPORTE = 117_172
    SALARIO_MINIMO = 1_000_000

    def salir(self):
        if messagebox.askyesno("Informacion", "¿Esta seguro de salir?"):
            self.root.destroy()

    def __init__(self, cantidad_empleados, ventana_emp) -> None:
        self.root = Tk()
        self.root.title("Registro - MLR SOFT")
        self.root.config(border=10)

        self.n_hombres = 0
        self.n_mujeres = 0
        self.textos_tabla_resultados = ["Id", "Nombre", "Cedula", "Salario", "Auxilio Transporte", "Total Deducciones",
                                        "Neto Pagar"]
        self.textos_entries = ["Nombre", "Cedula", "Sexo", "Edad", "Estatura", "Peso", "Cargo", "Salario"]
        self.textos_tabla_sub = ["Nombre Totales", "Totales"]
        self.id_empleado = MLRSOFT.contador_empleados
        self.cantidad_empleados = cantidad_empleados

        ventana_emp.destroy()

        self.entries_form_valores()
        self.tabla_resultados()
        self.tabla_subtotales()

        self.root.mainloop()

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_empleados += 1
        return cls.contador_empleados

    def tabla_subtotales(self):
        tabla_sub = Treeview(self.root, columns="#1")
        tabla_sub.place(x=360, y=120)
        for i in range(2):
            tabla_sub.heading(f"#{i}", text=self.textos_tabla_sub[i], anchor="center")
            tabla_sub.column(f"#{i}", anchor="center")

    def tabla_resultados(self):
        self.tabla_res = Treeview(self.root, columns=("#1", "#2", "#3", "#4", "#5", "#6"))
        self.tabla_res.grid(row=10, column=0, columnspan=8)
        configuracion_tabla = [50, 100, 100, 100, 120, 120, 100]

        for i in range(7):
            self.tabla_res.heading(f"#{i}", text=self.textos_tabla_resultados[i], anchor="center")
            self.tabla_res.column(f"#{i}", anchor="center", width=configuracion_tabla[i])

        self.btona = Button(self.root, text="Aceptar", bg="green", fg="white", width=8,
                            command=lambda: self.validar_empleados())
        self.btona.grid(row=0, column=2)

        bton = Button(self.root, text="Salir", bg="red", fg="white", width=8, command=lambda: self.salir())
        bton.grid(row=1, column=2)

    def entries_form_valores(self):
        self.datos = []
        for i in range(8):
            text = Label(self.root, text=self.textos_entries[i], font=("Helvica", 11), justify="right")
            text.grid(row=i, column=0, padx=10, pady=10)
            entry = Entry(self.root)
            entry.grid(row=i, column=1, padx=10, pady=10)
            self.datos.append(entry)

    def validar_empleados(self):
        if self.id_empleado == int(self.cantidad_empleados):
            self.btona["state"] = "disable"
            self.ingresar_datos_tabla_res()
            messagebox.showinfo("Informacion", "Se han evaluado a todos los empleados")
        else:
            if str(self.datos[2].get()).lower() == "hombre" or str(self.datos[2].get()).lower() == "masculino":
                self.n_hombres += 1
            else:
                if str(self.datos[2].get()).lower() == "mujer" or str(self.datos[2].get()).lower() == "femenimo":
                    self.n_mujeres += 1

            try:
                int(self.datos[1].get())
                # int(lista[3])
                # float(lista[4])
                # float(lista[5])
            except ValueError:
                messagebox.showerror("Informacion",
                                     "La cedula,la edad, la estatura y el peso deben ser valores numericos")

            self.ingresar_datos_tabla_res()
            self.id_empleado = MLRSOFT.generar_siguiente_valor()

    def ingresar_datos_tabla_res(self):
        # print(f"Hombres : {self.n_hombres}\nMujeres : {self.n_mujeres}")
        self.tabla_res.insert("", 0, text=self.id_empleado)

    def limpiar_entries(self):
        for entry in self.datos:
            entry.delete(0, "end")



        # #---------------------LISTAS---------------------------------------

# totales = ["Nomina","A.Salud","A.Pension","A.Solidarios","Auxilios Transporte","Hombres","Mujeres",
# "Promedio Estatura","Promedio Edad","Peso Mayor a 80 kg"] validar = False lista2 = []

# #-------------------CONTADOS Y ACUMULADORES-------------------------
# descsalud = 0
# descaport = 0
# sumatsalud = 0
# sumataport = 0
# fondos = 0
# sumafondos = 0
# nomina = 0
# deducciones = 0
# validar2 = False
# c2 = 0
# j = 0
# tauxt = 0
# nhombres = 0
# nmujeres = 0
# promest = 0
# promed = 0
# c1 = 0
# edad = 0
# salario = 0
# validar3 = False
# c = 0
# estatura = 0
# mpeso = 0
# c3 = 0
# #--------------------------------------------------------------------

# def aceptar2():

#     if validar3 == True:
#         ventana.destroy()

#     def aceptar():
#         global c3

#         c3 = c3 + 1

#         global j
#         global entries
#         global c1
#         global validar
#         global salariomin
#         global auxt
#         global salario
#         global descaport
#         global descsalud
#         global sumatsalud 
#         global sumataport 
#         global fondos
#         global sumafondos
#         global deducciones
#         global validar2
#         global nomina
#         global tauxt
#         global nhombres 
#         global nmujeres
#         global promest
#         global edad
#         global estatura
#         global c
#         global mpeso

#         lista2 = []
#         lista = []
#         validar = False
#         c1 = 0
#         salario = 0


#         for entries in datos:
#             if len(entries.get()):
#                 lista.append(entries.get())
#                 c1= c1 + 1
#                 if c1 == 8:
#                     validar = True  

#         if validar == True and validar2 == True:
#             j = j + 1
#             salario = 0
#             salario = int(lista[7])

#             if salario < salariomin*2:
#                 auxt = 117172
#                 tauxt = tauxt + auxt
#                 lista2.append(auxt)
#             else:
#                 auxt = 0
#                 lista2.append(auxt)

#             edad = edad + int(lista[3])
#             estatura = estatura + float(lista[4])
#             if float(lista[5]) > 80:
#                 mpeso = mpeso + 1

#             descsalud = salario*0.04
#             sumatsalud = sumatsalud + descsalud

#             descaport = salario*0.04
#             sumataport = sumataport + descaport

#             salario = salario - descsalud - descaport + auxt

#             if int(lista[7]) > salariomin*4:
#                 fondos = int(lista[7]) * 0.01
#                 sumafondos = sumafondos + fondos
#                 salario = salario - fondos
#             else:
#                 fondos = 0

#             deducciones = descaport + descsalud + fondos

#             nomina = nomina + float(lista[7]) + auxt

#             promed = edad/j
#             promest = estatura/j

#             lista2.append(deducciones)
#             lista2.append(salario)

# tabla.insert("",END,text=j,values=(lista[0],lista[1],"$" + lista[7],"$" + str(lista2[0]),"$" + str(int(lista2[1])),
# "$" + str(int(lista2[2]))))

#             valtotales = [nomina,sumatsalud,sumataport,sumafondos,tauxt,nhombres,nmujeres,promest,promed,mpeso]

#             registros = tabla2.get_children()

#             for registro in registros:
#                 tabla2.delete(registro)

#             for k in range(10):
#                 if k >= 0 and k<=4:
#                     tabla2.insert("",END,text=totales[k],values="$" + str(valtotales[k]))
#                 else:
#                     tabla2.insert("",END,text=totales[k],values=str(round(valtotales[k],2)))
#         else:
#             if validar == False:
#                 c3 = c3 - 1
#                 messagebox.showerror("Informacion","Debes ingresar todos los datos")

#         print(lista)
