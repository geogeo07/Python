from tkinter import *
from tkinter import ttk
#from PIL import ImageTk, Image

v0=Tk()
#imagen1 = ImageTk.PhotoImage(Image.open("chavito.jpg"))
#label1 = Label(v0, image=imagen1)
#label1.grid(row=1,column=1)



def imprimir(texto):
     print (texto)

def mostrar(ventana):
     return ventana.deiconify # Muestra una ventana

def ocultar(ventana):
     return ventana.withdraw() # Oculta una ventana

def ejecutar(f): 
    v0.after(100, f)

def abrirVentana3(etiqueta):
    #Caracteristicas de la ventana inicial
    mainMenu=Toplevel(v0)
    mainMenu.title("Main menu")
    mainMenu.geometry("568x516")

    Label(mainMenu,text=etiqueta,bg="black",fg="white",font=(15)).pack()
    Label(mainMenu,text="BIENVENIDO A NUESTRA APLICACIÓN",bg="black",fg="white",font=(15)).pack()
    Label(mainMenu,text="BIENVENIDO A NUESTRA APLICACIÓN",bg="black",fg="white",font=(15)).pack()



menu1 = Menu(v0)
v0.config(menu=menu1)
menu1_1 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="AMARILLO", menu=menu1_1)
menu1_1_1 = Menu(menu1_1, tearoff=0)
menu1_1.add_cascade(label="FRUTAS", menu=menu1_1_1)
menu1_1_1.add_command(label="BANANO",command=lambda: imprimir("BANANO"))
menu1_1_1.add_command(label="PIÑA",command=lambda: imprimir("PIÑA"))

menu1_2 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="ROJO", menu=menu1_2)
menu1_2.add_command(label="SANGRE",command=lambda: imprimir("SANGRE"))
menu1_2.add_separator()
menu1_2_1 = Menu(menu1_2, tearoff=0)
menu1_2.add_cascade(label="FRUTAS", menu=menu1_2_1)
menu1_2_1.add_command(label="FRESA",command=lambda: imprimir("FRESA"))
menu1_2_1.add_command(label="MANZANA",command=lambda: abrirVentana3("Platano") )

v1=Toplevel(v0)
s = ttk.Style()
s.theme_use('clam')

v1.geometry("400x200")
v1.config(bg="black")
v1.protocol("WM_DELETE_WINDOW", "onexit")
v1.resizable(0,0)

ocultar(v0)
def cerrar_splashscreen():
    ejecutar(ocultar(v1))
    ejecutar(mostrar(v0))

def progress(currentValue): #Llama
    progressbar["value"]=currentValue


    
v1.after(4000,cerrar_splashscreen)
Label(v1,text="BIENVENIDO A NUESTRA APLICACIÓN",bg="black",fg="white",font=(15)).pack()
Label(v1,text="BIENVENIDO A NUESTRA APLICACIÓN",bg="black",fg="white",font=(15)).pack()
Label(v1,text="BIENVENIDO A NUESTRA APLICACIÓN",bg="black",fg="white",font=(15)).pack()
Label(v1,text="BIENVENIDO A NUESTRA APLICACIÓN",bg="black",fg="white",font=(15)).pack()
Label(v1,text="BIENVENIDO A NUESTRA APLICACIÓN",bg="black",fg="white",font=(15)).pack()

maxValue=100
progressbar=ttk.Progressbar(v1,orient="horizontal",length=300,mode="determinate")
progressbar.pack(side=BOTTOM)
currentValue=0
progressbar["value"]=currentValue
progressbar["maximum"]=maxValue
divisions=10
for i in range(divisions):
    currentValue=currentValue+20
    progressbar.after(500, progress(currentValue))
    # Force an update of the GUI
    progressbar.update()

v0.mainloop()
