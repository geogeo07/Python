import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import socket
from urllib.request import urlopen


def progress(currentValue): #Llama
    progressbar["value"]=currentValue

def abrirVentana3():
    #Caracteristicas de la ventana inicial
    ventana3=tk.Tk()
    ventana3.title("Ventana 2")
    ventana3.geometry("568x516")

def abrirVentana2():
    #Caracteristicas de la ventana inicial
    ventana=tk.Tk()
    ventana.title("Ventana 1")
    ventana.geometry("568x516")
   

    #Widgets
    #labelUsuario
    labelUsuario=tk.Label(ventana, text="Usuario:" , bg="pink", fg= "white")
    labelUsuario.pack(padx=5, pady=5, ipadx=5, ipady=5)
    #TextBox
    textBoxUsuario=tk.Entry(ventana)
    textBoxUsuario.pack(fill=tk.X,padx=5,pady=58,ipadx=5, ipady=5)

    #labelContraseña
    labelContra=tk.Label(ventana, text="Contraseña:" , bg="black", fg= "white")
    labelContra.pack(padx=5, pady=5, ipadx=5, ipady=5)
    #TextBox
    textBoxContra=tk.Entry(ventana)
    textBoxContra.pack(fill=tk.X,padx=5,pady=58,ipadx=5, ipady=5)

    
    #Botones
    
    botonLogIn=tk.Button(ventana,text="Iniciar Sesion", fg="blue", command=abrirVentana3)
    botonLogIn.pack(side=tk.TOP)
    
    if internet_on() == False:
        boton2=tk.Button(ventana,text="Validar password", fg="blue", state = 'disable', command=validar)
    else:
        boton2=tk.Button(ventana,text="Validar password", fg="blue", state = 'normal', command=validar) 
    boton2.pack(side=tk.TOP)
    

def validar():
        messagebox.showwarning("Cuidado", "jolis")




def internet_on(): #Comprueba que exista alguna conexion a internet.
   try:
        response = urlopen('https://www.google.com/', timeout=10)
        return True
   except: 
        return False
            
        
if __name__ == '__main__':
    #Caracteristicas y creacion de la ventana del Splash
    SplashScreen = tk.Tk()
    SplashScreen.title("SplashScreen")
    SplashScreen.geometry("568x516")
    s = ttk.Style()
    s.theme_use('clam')

    #Imagen del Splash
    img = ImageTk.PhotoImage(Image.open("chavito.jpg"))
    panel = tk.Label(SplashScreen, image = img)
    panel.pack(side = "top", fill = "both", expand = "yes")

    #Caracteristicas y creacion del progressBar
    maxValue=100
    progressbar=ttk.Progressbar(SplashScreen,orient="horizontal",length=300,mode="determinate")
    progressbar.pack(side=tk.BOTTOM)
    currentValue=0
    progressbar["value"]=currentValue
    progressbar["maximum"]=maxValue
    divisions=10
    for i in range(divisions):
       currentValue=currentValue+20
       progressbar.after(500, progress(currentValue))
       # Force an update of the GUI
       progressbar.update()

    #Se abre la segunda ventana cuando termina el progressBar
    abrirVentana2()
    #Se cierra el Splash
    SplashScreen.destroy()
    
    
    
    
    







