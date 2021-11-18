import cv2
import encodingt as o
def hide(img,f):

    """img=cv2.imread("C:/Users/DELL-PC/Desktop/Project/Code - Final/sam.jpg")
    file = open("Textfile.txt","r")

    f=file.read()
    file.close()"""

    if len(f)+10<(img.size//3):
        img2=o.encode(img,f);
    else:
        print("Data is larger than image")

    cv2.imwrite("Data Image.bmp",img2)

    print("\nData has been encoded in the given Image sucessfully\n")

    return;
