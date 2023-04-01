from tkinter import*

raiz=Tk()

#------------------ Frame------------------------------
miFrame = Frame(width=1200, height=600)
miFrame.pack()
#-----------------Caja y texto de Nombre--------------------------------

nombrelabel = Label(miFrame,text="Nombre:")
nombrelabel.grid(row=0,column=0,sticky="e",padx=10,pady=10) #row = filas y column = columnas las dos empiezan desde 0

minombre=StringVar()

cajanombre = Entry(miFrame,textvariable=minombre)
cajanombre.grid(row=0,column=1,padx=10,pady=10)
cajanombre.config(fg="red",justify="center")
#-----------------Caja y texto de Direccion--------------------------------
direcciontexto = Label(miFrame,text="Direccion:",padx=10,pady=10)
direcciontexto.grid(row=1,column=0,sticky="e") 

direccioncaja = Entry(miFrame)
direccioncaja.grid(row=1,column=1,padx=10,pady=10)

#-----------------Caja y texto de Telefono--------------------------------
telefonotexto = Label(miFrame,text="Telefono:")
telefonotexto.grid(row=2,column=0,sticky="e",padx=10,pady=10) 

telefonocaja = Entry(miFrame)
telefonocaja.grid(row=2,column=1,padx=10,pady=10)

#-----------------Caja y texto de Correo Electronico--------------------------------
correotexto = Label(miFrame,text="Correo Electronico:")
correotexto.grid(row=3,column=0,sticky="e",padx=10,pady=10) 

correocaja = Entry(miFrame)
correocaja.grid(row=3,column=1,padx=10,pady=10)
#-----------------Caja y texto de Contraseña--------------------------------
contraseñatexto = Label(miFrame,text="Contraseña :")
contraseñatexto.grid(row=4,column=0,sticky="e",padx=10,pady=10) 

contraseñacaja = Entry(miFrame)
contraseñacaja.grid(row=4,column=1,padx=10,pady=10)
contraseñacaja.config(show="*")

#----------------------Comentarios----------------------------------------
comentariotexto = Label(miFrame,text="Comentarios:")
comentariotexto.grid(row=5,column=0,sticky="e",padx=10,pady=10) 

comentariocaja = Text(miFrame,width=16,height=5)
comentariocaja.grid(row=5,column=1,padx=10,pady=10)

#----------------Scroll de Comentarios------------------------------------

scrollcom=Scrollbar(miFrame,command=comentariocaja.yview)
scrollcom.grid(row=5,column=2,sticky="nsew")
comentariocaja.config(yscrollcommand=scrollcom.set)

#------------------Boton------------------------------------------------

def codigoboton():
    minombre.set("")

botonenvio=Button(raiz,text="Enviar",command=codigoboton)
botonenvio.pack()

raiz.mainloop()