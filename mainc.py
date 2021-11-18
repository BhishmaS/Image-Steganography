import cv2
import hidingt as o
import retrievingt as o1
import hidingi as o2
import retrievingi as o3

c=5

while c!=0:
    print ("\n1.Hide Data\n2.Retrieve Data\n3.Hide Image\n4.Retrieve Image\n0.Exit")
    c=int(input("Select your option:"))
    if c==1:
        img=cv2.imread("C:/Users/DELL-PC/Desktop/Project/Code - Final/sam1.jpg")
        file = open("Textfile.txt","r")

        f=file.read()
        file.close()
        o.hide(img,f)
    elif c==2:
        img=cv2.imread("C:/Users/DELL-PC/Desktop/Project/Code - Final/Data Image.bmp")
        o1.retrive(img)
    elif c==3:
        img=cv2.imread("C:/Users/DELL-PC/Desktop/Project/Code - Final/sam.jpg")
        img1=cv2.imread("C:/Users/DELL-PC/Desktop/Project/Code/sam1.jpg")
        o2.hide(img,img1)
    elif c==4:
        img=cv2.imread("C:/Users/DELL-PC/Desktop/Project/Code - Final/secreteImg.bmp")
        o3.retrive(img)

