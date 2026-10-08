import tkinter

ventana = tkinter.Tk()
ventana.geometry("300x300")

boton1 = tkinter.Button(ventana, text="Botón 1")
boton2 = tkinter.Button(ventana, text="Botón 2")
boton3 = tkinter.Button(ventana, text="Botón 3")
boton1.grid(row=0, column=0)
boton2.grid(row=1, column=0)
boton3.grid(row=2, column=0)

ventana.mainloop()
