import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk


##Cambiar el grid por place para tener posiciones absolutas..

#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("Digital Microscope")
window.config(background="#FFFFFF")
window.geometry("1000x600")

#Graphics window
imageFrame = tk.Frame(window, width=600, height=500)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

#Capture video frames
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)


def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    cv2.circle(cv2image,(255,255), 50, (0,0,255), 1)
    cv2.line(cv2image,(200,255),(320,255),(0,255,0),2) #Horizontal
    cv2.line(cv2image,(255,200),(255,310),(255,100,255),2) #Linea vertical


    img = Image.fromarray(cv2image)

    


    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame) 



#Slider window (slider controls stage position)
sliderFrame = tk.Frame(window, width=600, height=100)
sliderFrame.grid(row = 800, column=0, padx=10, pady=2)


ButtonDerecha=tk.Button(window,text="Derecha", fg="blue", state = 'normal')
ButtonDerecha.grid(row = 800, column=75, padx=5, pady=2)

ButtonIzquierda=tk.Button(window,text="Izquierda", fg="blue", state = 'normal')
ButtonIzquierda.grid(row = 800, column=50, padx=15, pady=2)


show_frame()  #Display 2
window.mainloop()  #Starts GUI