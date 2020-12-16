import cv2, numpy as np, time
from tkinter import *
from tkinter import messagebox

ventana=Tk()
ventana.title('Captura')
ventana.geometry('100x80')
ventana.resizable(False,False)
ventana.configure(bg='Azure')
button_color=('snow')
def Captura():
    cap=cv2.VideoCapture(1)
    
    ret, frame=cap.read()
    cv2.imwrite('Imagen.png',frame)
    messagebox.showinfo('Info', '¡Foto capturada!')
    cap.release()

btn=Button(ventana, text="¡Presioname!", command=Captura,bg=button_color).grid(column=2, row=2, pady=10,padx=10)

ventana.mainloop()


