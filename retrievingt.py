import cv2
import codecs
import decodingt as o
def retrive(img):

    #img=cv2.imread("C:/Users/DELL-PC/Desktop/Project/Code - Final/secreteImg.bmp")

    f=o.decode(img)

    """
    file = codecs.open("SecreteData.txt","w",encoding="utf8")
    #print(f)
    file.write(f)
    file.close()"""
    
    print("\nData has been decoded from the image and stored in a fle, check for data in the file named SecreteData\n")

    return f; 
