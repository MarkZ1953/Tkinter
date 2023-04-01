def centrar(r):
    altura = r.winfo_reqheight()
    anchura = r.winfo_reqwidth()
    altura_pantalla = r.winfo_screenheight()
    anchura_pantalla = r.winfo_screenwidth()
    x = (anchura_pantalla // 2) - (anchura//2)
    y = (altura_pantalla//2) - (altura//2)
    r.geometry(f"+{x}+{y}")