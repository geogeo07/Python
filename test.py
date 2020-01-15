from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

import socket
from urllib.request import urlopen

#from PIL import ImageTk, Image

loginWindow=Tk()
mainMenu=Tk()

#imagen1 = ImageTk.PhotoImage(Image.open("chavito.jpg"))
#label1 = Label(loginWindow, image=imagen1)
#label1.grid(row=1,column=1)



def imprimir(texto):
     print (texto)

def mostrar(ventana):
     return ventana.deiconify # Muestra una ventana

def ocultar(ventana):
     return ventana.withdraw() # Oculta una ventana

def ejecutar(f): 
    loginWindow.after(100, f)


def cerrar_splashscreen():
    ejecutar(ocultar(splashScreen))
    ejecutar(mostrar(loginWindow))




def progress(currentValue): #Llama
    progressbar["value"]=currentValue

def validarContraseña(abrirVentana, usuarioLogin, contraLogin): #Valida la contra del login, cierra el login y abre el menu principal
    if usuarioLogin == '1' and contraLogin == '1':
       {
           abrirVentana.deiconify()
                    
       } 
    else:
        messagebox.showwarning("Cuidado", "Password incorrecto")




def hayInternet(): #Comprueba que exista alguna conexion a internet.
   try:
        response = urlopen('https://www.google.com/', timeout=10)
        return True
   except: 
        return False

def VentanaInternet ():
    internetWindow = Toplevel(mainMenu)
    internetWindow.title("Internet Window")
    internetWindow.geometry('380x380')
    internetWindow.configure(background='dark gray')
   
    internetWindow.resizable(0,0)
    e1=Label(internetWindow, text="Password:" , bg="pink", fg= "white")
    e1.pack(padx=5, pady=5, ipadx=5, ipady=5)
    entrada1=Entry(internetWindow)
    entrada1.pack(fill=X,padx=5,pady=58,ipadx=5, ipady=5)
    if hayInternet == False: #Comprueba si hay internet.
        ButtonInternet=Button(internetWindow,text="Por internet", fg="blue", state = 'disable' )
    else:
        ButtonInternet=Button(internetWindow,text="Por internet", fg="blue", state = 'normal' )

    ButtonInternet.pack(side=TOP)
    ButtonLocal=Button(internetWindow,text="Local", fg="blue")
    ButtonLocal.pack(side=BOTTOM)

def registroUsuario(username, contra):
    usuario_info = username
    contra_info = contra
    file = open("usuario_info.txt", "w")
    file.write(usuario_info + "\n")
    file.write(contra_info)
    file.close()



def verificarUsuario(ventana, username, contra):
    
    usuario_info = username
    contra_info = contra

    if usuario_info == '' or contra_info == '':
        messagebox.showwarning("Cuidado", "Revisa tus datos bro")
        
    else:
        print(usuario_info, contra_info)

        lista_archivos = os.listdir()
    #print(lista_archivos, sep=' ', end='\n', file=sys.stdout, flush=False) Imprimir lista de archivos.

   
        archivo = open("usuario_info.txt", "r")
        verificar = archivo.read().splitlines()
        print(verificar)
        if usuario_info in verificar:
            posicion = verificar.index(usuario_info)
            print (usuario_info)
            print(posicion)
            print(contra_info)
            if contra in verificar[posicion+1]:
                messagebox.showinfo("Listo", "Ya quedo bro")
                ventana.deiconify()
                loginWindow.destroy()
            else:
                messagebox.showwarning("Cuidado", "Password incorrecto")
        else:
            messagebox.showwarning("Cuidado", "Usuario incorrecto")
         

    
        
        
   
    




def VentanaAgregarUsuario ():
    #Vetana de agregar usuario
    addUserWindow = Toplevel(mainMenu)
    
    addUserWindow.title("Agregar usuario")
    addUserWindow.geometry('380x380')
    addUserWindow.configure(background='dark gray')

    addUserWindow.resizable(0,0)
    #
    EtiquetaUsuario=Label(addUserWindow, text="Usuario:" , bg="pink", fg= "white")
    EtiquetaUsuario.pack(padx=5, pady=5, ipadx=5, ipady=5)
    TxtUser=Entry(addUserWindow)
    TxtUser.pack(fill=X,padx=5,pady=5,ipadx=5, ipady=5)

    EtiquetaContra=Label(addUserWindow, text="Contraseña:", bg="pink", fg= "white")
    EtiquetaContra.pack(padx=5, pady=5, ipadx=5, ipady=5)
    TxtPass=Entry(addUserWindow)
    TxtPass.pack(fill=X,padx=5,pady=5,ipadx=5, ipady=5)
    ButtonRegistrar=Button(addUserWindow,text="Registrar", fg="blue", state = 'normal' , command=lambda:registroUsuario(TxtUser.get(), TxtPass.get()))
    
    ButtonRegistrar.pack(side=BOTTOM)
    #Fin ventana agregar usuario
    
    
   








    




#Creacion del login
loginWindow.title("Login")
loginWindow.geometry('380x380')
loginWindow.configure(background='dark gray')
loginWindow.resizable(0,0)
    #
EtiquetaUsuario=Label(loginWindow, text="Usuario:" , bg="pink", fg= "white")
EtiquetaUsuario.pack(padx=5, pady=5, ipadx=5, ipady=5)
TxtUsuario=Entry(loginWindow)
TxtUsuario.pack(fill=X,padx=5,pady=5,ipadx=5, ipady=5)

EtiquetaContra=Label(loginWindow, text="Contraseña:" , bg="pink", fg= "white")
EtiquetaContra.pack(padx=5, pady=5, ipadx=5, ipady=5)
TxtContra=Entry(loginWindow)
TxtContra.pack(fill=X,padx=5,pady=5,ipadx=5, ipady=5)

ButtonVerificar=Button(loginWindow,text="Verificar", fg="blue", state = 'normal' , command=lambda:verificarUsuario(mainMenu, TxtUsuario.get(), TxtContra.get()))

ButtonVerificar.pack(side=BOTTOM)



#Crea una ventana hija del loginWindow
splashScreen=Toplevel(loginWindow)
splashScreen.geometry("400x200")
splashScreen.config(bg="black")
splashScreen.protocol("WM_DELETE_WINDOW", "onexit")
splashScreen.resizable(0,0)

#Ocultamos loginWindow
ocultar(loginWindow)
ocultar(mainMenu)


#iniciamos la aplicacion abriendo el splash y manteniendo oculto el menu despues de 4000 milisegundos.
splashScreen.after(4000,cerrar_splashscreen)

#Agregamos una etiqueta al splash.
Label(splashScreen,text="BIENVENIDO A NUESTRA APLICACIÓN",bg="black",fg="white",font=(15)).pack()


#ProgressBar started
maxValue=100
progressbar=ttk.Progressbar(splashScreen,orient="horizontal",length=300,mode="determinate")
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
#ProgressBar finished.



#Creacion del menu
mainMenu.focus_set()
menu1 = Menu(mainMenu)
mainMenu.geometry('380x380')
mainMenu.config(menu=menu1)
menu1_1 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Conexion", menu=menu1_1)
menu1_1_1 = Menu(menu1_1, tearoff=0)
menu1_1.add_cascade(label="Ver conexiones", menu=menu1_1_1)
menu1_1_1.add_command(label="Arbrir Conexiones",command=lambda: imprimir("Guardar todo"))
if hayInternet == False:
    menu1_1_1.add_command(label="Internet", state = 'Disable')
else:
    menu1_1_1.add_command(label="Internet", command=VentanaInternet)

menu1_2 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Abrir", menu=menu1_2)
menu1_2.add_command(label="Abrir codigo",command=lambda: imprimir("Abrir codigo"))
menu1_2.add_separator()
menu1_2_1 = Menu(menu1_2, tearoff=0)
menu1_2.add_cascade(label="Abrir otra cosa", menu=menu1_2_1)
menu1_2_1.add_command(label="ARchivo",command=lambda: imprimir("ARchivo"))
menu1_2_1.add_command(label="Carpeta",command=lambda: imprimir("Carpeta") )


menu1_3 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Agregar Usuario", menu=menu1_3)
menu1_3.add_command(label="Agregar Usuario",command=lambda:VentanaAgregarUsuario())



loginWindow.mainloop()