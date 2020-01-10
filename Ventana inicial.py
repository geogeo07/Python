import tkinter as tk
from tkinter import messagebox

def validar():
    if entrada1.get()=='lili':
        abrirVentana2()
    else:
        messagebox.showwarning("Cuidado", "Password incorrecto")

def abrirVentana2():
    ventana.withdraw()
    win=tk.Toplevel()
    win.geometry('380x300+1900+100')
    win.configure(background='dark turquoise')
    e3=tk.Label(win,text="Bienvenido a la segundo ventana",bg="pink",fg="white")
    e3.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
    boton2=tk.Button(win, text='OK', command=win.destroy)
    boton2.pack(side=tk.TOP)

def cerrarVentana():
    ventana,destroy()

ventana=tk.Tk()
ventana.title("Ventana 1")
ventana.geometry('380x380')
ventana.configure(background='dark turquoise')
e1=tk.Label(ventana, text="Password:" , bg="pink", fg= "white")
e1.pack(padx=5, pady=5, ipadx=5, ipady=5)
entrada1=tk.Entry(ventana)
entrada1.pack(fill=tk.X,padx=5,pady=58,ipadx=5, ipady=5)
boton=tk.Button(ventana,text="Nueva ventana", fg="blue", command=abrirVentana2)
boton.pack(side=tk.TOP)
boton3=tk.Button(ventana,text="Validar password", fg="blue", command=validar)
boton3.pack(side=tk.TOP)
ventana.mainloop()


