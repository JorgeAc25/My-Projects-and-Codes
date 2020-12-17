import numpy as np
import cv2

# Crear ventana en blanco
img = 255*np.ones((500, 500, 3), np.uint8)

# Creacion del logo
x = 50
for i in range(15, 45):
    for j in range(0, 1):
        img = cv2.ellipse(img, (255, 155), (x, x), 125, 0, 295, (0, 0, 255), 2)
        img = cv2.ellipse(img, (193, 250), (x, x), 0, 0, 303, (0, 240, 0), 2)
        img = cv2.ellipse(img, (312, 250), (x, x), -58, 0, 295, (255, 0, 0), 2)
        x = x-1

# Texto
cv2.putText(img, 'OpenCV', (135, 360), 0, 2, (0, 0, 0), 5, cv2.LINE_AA)
# Mostrar imagen
cv2.imshow('Imagen', img)
# Cerrar ventana
cv2.waitKey(0)
cv2.destroyAllWindows()
