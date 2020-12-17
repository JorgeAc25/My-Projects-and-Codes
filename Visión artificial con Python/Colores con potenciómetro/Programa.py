import serial
import cv2
import numpy as np
import time

ser = serial.Serial('/dev/ttyACM0', 115200)
cap = cv2.VideoCapture(0)

while (1):
    val = ser.readline()
    line = val.decode('latin-1').strip()
    time.sleep(0.1)
    Data = line.split()

    Blue = int(Data[0])
    Green = int(Data[1])
    Red = int(Data[2])

    ColorBGR = np.uint8([[[Blue, Green, Red]]])
    ColorHSV = cv2.cvtColor(ColorBGR, cv2.COLOR_BGR2HSV)
    ColorHSV = line.split()

    Hue = int(ColorHSV[0])
    Sat = int(ColorHSV[1])
    Value = int(ColorHSV[2])

    lowerColor = np.array([0, 0, 0], np.uint8)
    Colors = np.array([Hue, Sat, Value], np.uint8)

    ret, frame = cap.read()
    HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(HSV, lowerColor, Colors)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Capture', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
