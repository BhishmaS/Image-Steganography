import cv2
import decodingi as o

def retrive(img):
    
    #img=cv2.imread("C:/Users/DELL-PC/Desktop/Project/Code - Final/secreteImg.bmp")

    img1=o.decode(img)

    cv2.imwrite("hiddenImg.bmp",img1)
    print("\nSecret Image has been decoded from the given image \n")

    return;
