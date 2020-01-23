import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk


##Cambiar el grid por place para tener posiciones absolutas..

#Set up GUI
ventanaCalibrar = tk.Tk()  #Makes main ventanaCalibrar


ventanaCalibrar.iconbitmap("Imagenes/icono.ico")
ventanaCalibrar.wm_title("Calibracion manual")
ventanaCalibrar.config(background="#FFFFFF")
ventanaCalibrar.geometry("1000x600")


#Marcos
marcoVideo = tk.LabelFrame(ventanaCalibrar, width=600, height=450, relief="sunken")
marcoVideo.place(x=10 , y=10)

marcoAvance = tk.LabelFrame(ventanaCalibrar, width=335, height=150, relief="sunken")
marcoAvance.place(x=650, y=10)

marcoFlechas = tk.LabelFrame(ventanaCalibrar, width=335, height=400, relief="sunken")
marcoFlechas.place(x=650 , y=200)


#Capture video frames
labelVideo = tk.Label(marcoVideo,  height=438,  width=588)
labelVideo.place(x=2, y= 2)
cap = cv2.VideoCapture(0)


def obtenerRadio(Avance, direccion):
    
    unidades = unidadMedida.get()
    if unidades == 1:
        print("Centimetros")
        moverMotor("Centimetros",Avance, direccion)
    elif unidades == 2:
        print("Pulgadas")
        moverMotor("Pulgadas",Avance, direccion)
    else:
        print("An option must be selected")




def moverMotor(unidades, Avance, direccion):
    #Direccion: 1 Motor x+, 2 Hacia Motor x-, 3 Motor y+, 4 Motor y-, 5 Motor z+, 6 Motor z-.
    #Unidades: 1=Centimetros,  2= Pulgadas.
    
    print ("Unidades" + unidades)
    if unidades == "Centimetros":
        distancia = float(Avance)*1
        print("La distancia es: ")
        print(distancia)
    else:
        distancia = float(Avance)*2.54 
        print("La distancia es: ")
        print(distancia)
    
    if direccion == 1:
        #Mover el motor de x +
        print("unidades = ")
        print(unidades)
        print("distancia = ")
        print(distancia)
        print("direccion = ")
        print(direccion)

    if direccion == 2:
        #Mover el motor de x -
        print("unidades = ")
        print(unidades)
        print("distancia = ")
        print(distancia)
        print("direccion = ")
        print(direccion)
    if direccion == 3:
        #Mover el motor de y +
        print("unidades = ")
        print(unidades)
        print("distancia = ")
        print(distancia)
        print("direccion = ")
        print(direccion)
    if direccion == 4:
        #Mover el motor de y -
        print("unidades = ")
        print(unidades)
        print("distancia = ")
        print(distancia)
        print("direccion = ")
        print(direccion)
    if direccion == 5:
        #Mover el motor de z +
        print("unidades = ")
        print(unidades)
        print("distancia = ")
        print(distancia)
        print("direccion = ")
        print(direccion)
    if direccion ==6:
        #Mover el motor de z -
        print("unidades = ")
        print(unidades)
        print("distancia = ")
        print(distancia)
        print("direccion = ")
        print(direccion)
    

            



def video_loop():
    """ Get frame from the video stream and show it in Tkinter """
    
    ok, frame = cap.read()  # read frame from video stream
    if ok:  # frame captured without any errors
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # convert colors from BGR to RGBA
        cv2.circle(cv2image,(294,219), 40, (0,0,255), 2)
        cv2.line(cv2image,(250,219),(340,219),(0,255,0),1) #Horizontal
        cv2.line(cv2image,(294,175),(294,270),(255,100,255),1) #Linea vertical
        current_image = Image.fromarray(cv2image)  # convert image for PIL
        imgtk = ImageTk.PhotoImage(image=current_image)  # convert image for tkinter
        labelVideo.imgtk = imgtk  # anchor imgtk so it does not be deleted by garbage-collector
        labelVideo.config(image=imgtk)  # show the image
    ventanaCalibrar.after(30, video_loop)  # call the same function after 30 milliseconds
    





#imagenes de las flechas
flechaDerecha = tk.PhotoImage(file='Imagenes/flechaDerecha.png')
flechaIzquierda = tk.PhotoImage(file='Imagenes/flechaIzquierda.png')
flechaAbajo = tk.PhotoImage(file='Imagenes/flechaAbajo.png')
flechaArriba  = tk.PhotoImage(file='Imagenes/flechaArriba.png')







#TextField de la cantidad de movimiento que se necesita para cada eje
AvanceTxt = tk.Entry(marcoAvance)
AvanceTxt.place(x=60, y=20)

LabelAvance = tk.Label(marcoAvance, text = "Avance: ")
LabelAvance.place(x=30, y=20)



unidadMedida = tk.IntVar()
RadioCentimetros = tk.Radiobutton(marcoAvance, text="Centimetros:" , variable=unidadMedida, value = 1).place(x=200 , y=10)
RadioPulgadas = tk.Radiobutton(marcoAvance, text="Pulgadas: ", variable=unidadMedida, value = 2).place(x=200 , y=50)



ButtonDerecha=tk.Button(marcoFlechas,text="Derecha", fg="blue", state = 'normal', image=flechaDerecha , command = lambda: obtenerRadio(AvanceTxt.get(),1)).place(x=200, y=50)
ButtonIzquierda=tk.Button(marcoFlechas,text="Izquierda", fg="blue", state = 'normal', image=flechaIzquierda , command = lambda: obtenerRadio(AvanceTxt.get(),2)).place(x=50, y=50)
ButtonAbajo=tk.Button(marcoFlechas,text="Derecha", fg="blue", state = 'normal', image=flechaAbajo , command = lambda: obtenerRadio(AvanceTxt.get(),3)).place(x=150, y=100)
ButtonArriba=tk.Button(marcoFlechas,text="Izquierda", fg="blue", state = 'normal', image=flechaArriba , command = lambda: obtenerRadio(AvanceTxt.get(),4)).place(x=150, y=10)

ButtonAbajoZ=tk.Button(marcoFlechas,text="Derecha Z", fg="blue", state = 'normal', image=flechaAbajo , command = lambda: obtenerRadio(AvanceTxt.get(),6)).place(x=20, y=200)
ButtonArribaZ=tk.Button(marcoFlechas,text="Izquierda Z", fg="blue", state = 'normal', image=flechaArriba , command = lambda: obtenerRadio(AvanceTxt.get(),5)).place(x=250, y=200)


ButtonIniciar=tk.Button(marcoFlechas, text="Iniciar",  state = 'normal' , width = "5" , height= "2", background ="green" , command = lambda: obtenerRadio(AvanceTxt.get(),6)).place(x=250, y=330)
ButtonParar=tk.Button(marcoFlechas, text="Parar", state = 'normal',background ="red", width = "5" , height= "2", command = lambda: obtenerRadio(AvanceTxt.get(),5)).place(x=50, y=330)

video_loop()

ventanaCalibrar.mainloop()  #Starts GUI

