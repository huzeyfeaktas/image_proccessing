import cv2

def boyutlandirma(img,x,y):
    return cv2.resize(img,(x,y))