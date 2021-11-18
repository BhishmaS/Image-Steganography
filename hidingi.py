import cv2
import encodingi as o

def hide(img,img1):

    #img=cv2.imread("C:/Users/DELL-PC/Desktop/Project/Code - Final/sam.jpg")
    #img1=cv2.imread("C:/Users/DELL-PC/Desktop/Project/Code/sam1.jpg")

    if img.size>img1.size:
        img2=o.encode(img,img1)
        cv2.imwrite("Data Image.bmp",img2)
        print("\nSecret Image has been encoded in the given Image sucessfully\n")
        return 1;
    else:
        print("Size of secret image should be less than the image in which it should be hidden")
        print(len(img[0]))
        print(len(img))
        return 0;
