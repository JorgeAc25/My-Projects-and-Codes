import numpy as np
import cv2
import time


def nothing(x):
    pass


cv2.namedWindow('Image')
Images = ['Imagen 1.jpg', 'Imagen 2.jpg', 'Imagen 3.jpg']

cv2.createTrackbar('Values', 'Image', 0, 2, nothing)

while True:
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    s = cv2.getTrackbarPos('Values', 'Image')

    if s == 0:
        for i in range(0, 1):
            img = cv2.imread(Images[i])
            img = cv2.imshow('Image', img)

    elif s == 1:
        for i in range(0, 2):
            img = cv2.imread(Images[i])
            img = cv2.imshow('Image', img)

    elif s == 2:
        for i in range(0, 3):
            img = cv2.imread(Images[i])
            img = cv2.imshow('Image', img)

cv2.destroyAllWindows()
