import cv2
#Ruta
path='Prueba.jpg'
#Variables para modificar la geometria de la imagen
width,height=750,500

#Cargar imagen
imagen1=cv2.imread((path),cv2.IMREAD_UNCHANGED)
imagen2=cv2.imread((path),cv2.IMREAD_GRAYSCALE)
imagen3=cv2.imread((path),cv2.IMREAD_COLOR)

#Modificar Imagen
img1Resize=cv2.resize(imagen1,(width,height))
img2Resize=cv2.resize(imagen2,(width,height))
img3Resize=cv2.resize(imagen3,(width,height))

#Mostrar imagenes
cv2.imshow('Imagen sin cambiar', img1Resize)
cv2.imshow('Imagen a escala de colores', img2Resize)
cv2.imshow('Imagen a color', img3Resize)

#Guardar Imagenes
cv2.imwrite('Imagen 1.jpg',img1Resize)
cv2.imwrite('Imagen 2.jpg',img2Resize)
cv2.imwrite('Imagen 3.jpg',img3Resize)

#Cerrar ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
