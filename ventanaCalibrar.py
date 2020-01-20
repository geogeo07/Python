import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk


##Cambiar el grid por place para tener posiciones absolutas..

#Set up GUI
ventanaCalibrar = tk.Tk()  #Makes main ventanaCalibrar
ventanaCalibrar.wm_title("Calibracion manual")
ventanaCalibrar.config(background="#FFFFFF")
ventanaCalibrar.geometry("1000x600")

#Graphics ventanaCalibrar
#imageFrame = tk.Frame(ventanaCalibrar, width=600, height=500)
#imageFrame.grid(row=0, column=0, padx=10, pady=2)

#Capture video frames
labelVideo = tk.Label(ventanaCalibrar)
labelVideo.place(x=10 , y=10)
cap = cv2.VideoCapture(1)


def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    #cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)


    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



    cv2.circle(cv2image,(255,255), 50, (0,0,255), 1)
    cv2.line(cv2image,(200,255),(320,255),(0,255,0),2) #Horizontal
    cv2.line(cv2image,(255,200),(255,310),(255,100,255),2) #Linea vertical


    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame) 



#Slider ventanaCalibrar (slider controls stage position)
#sliderFrame = tk.Frame(ventanaCalibrar, width=600, height=100)
#sliderFrame.grid(row = 800, column=0, padx=10, pady=2)


ButtonDerecha=tk.Button(ventanaCalibrar,text="Derecha", fg="blue", state = 'normal')
ButtonDerecha.place(x=800, y=200)

ButtonIzquierda=tk.Button(ventanaCalibrar,text="Izquierda", fg="blue", state = 'normal')
ButtonIzquierda.place(x=800, y=200)


show_frame()  #Display 2
ventanaCalibrar.mainloop()  #Starts GUI