import cv2
import numpy as np
from pyzbar.pyzbar import decode
import pyautogui
#img = cv2.imread('T-REX.png')
cap = cv2.VideoCapture(0)
cap.set(3,1000)
cap.set(4,500)

with open('data.txt') as f:
    myDataList = f.read().splitlines()

while True:

    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        

        if myData in myDataList:
            myOutput =  'Verified shipment'
            myColor = (0,255,0)
            pyautogui.alert(myData)
        else:
            myOutput =  myData
            myColor = (0, 0, 255)

        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,myColor,5)
        pts2 = barcode.rect
        cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,myColor,2)

    cv2.imshow('Result',img)
    cv2.waitKey(1)
