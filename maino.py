import cv2
import tkinter
#import codecs
from PIL import Image,ImageTk
import hidingt as o
import retrievingt as o1
import hidingi as o2
import retrievingi as o3

def hideText3(img,f):
    #print(img)
    #print(f)
    o.hide(img,f)
    text1=tkinter.Text(innerFrame2,height='1', width="50")
    text1.pack(padx="55",pady=(20,20))
    text1.insert(tkinter.END,"Text Hidden in Image named 'Data Image'")
    text1.configure(state='disabled')
    
def hideText2(img):
    filename = tkinter.filedialog.askopenfilename(title = "Select File",filetypes = [("Text File", "*.txt")])
    file = open(filename,"r")
    f=file.read()
    file.close()
    tkinter.Button(innerFrame2, text = "Hide",command= lambda:hideText3(img,f), width = 25).pack(padx="160",pady=(50,20))
    
def hideText1():
    filename = tkinter.filedialog.askopenfilename(title = "Select Image",filetypes = (("Image Files", "*.jpg"),("Image Files", "*.png"),("Image Files", "*.bmp") ))
    #print(filename)
        
    img=cv2.imread(filename)
    tkinter.Button(innerFrame2, text = "BrowseFile",command= lambda:hideText2(img), width = 25).pack(padx="160",pady=(30,20))
    #return img

def hideText():
    for widget in innerFrame2.winfo_children():
        widget.destroy()

    tkinter.Button(innerFrame2, text = "BrowseImage",command=hideText1, width = 25).pack(padx="160",pady=(30,20))
    
    #filename = tkinter.filedialog.askopenfilename(title = "Select Image",filetypes = (("Image Files", "*.jpg"),("Image Files", "*.png"),("Image Files", "*.bmp") ))
    #print(filename)
    #img=cv2.imread(filename)
    #print(img)

    #file = open("Textfile.txt","r")
    #f=file.read()
    #file.close()
    
    #print(rimage)
    #print(rfile)

    
    #tkinter.Button(innerFrame2, text = "BrowseFile",command= lambda:hideText(img,f), width = 10).pack()

    #innerFrame2.destroy()
    #innerFrame3=tkinter.Frame(root,width="500",height="300",bg="black",bd="5", relief=tkinter.SUNKEN)#,colormap="new")
    #innerFrame3.pack(side="right",fill="both",padx=(200),pady=(90,90))

def retriveText2(img):
    o1.retrive(img)
    
    text1=tkinter.Text(innerFrame2,height='2', width="50")
    text1.pack(padx="55",pady=(20,20))
    text1.insert(tkinter.END,"Text Retrieved and saved in File named 'SecreteData'")
    text1.configure(state='disabled')
    
def retrieveText1():
    filename = tkinter.filedialog.askopenfilename(title = "Select Image",filetypes = (("Image Files", "*.jpg"),("Image Files", "*.png"),("Image Files", "*.bmp") ))
    img=cv2.imread(filename)
    tkinter.Button(innerFrame2, text = "Retrieve",command= lambda:retriveText2(img), width = 25).pack(padx="160",pady=(30,20))
    
def retrieveText():
    for widget in innerFrame2.winfo_children():
        widget.destroy()
        #print(widget.getName())
    img=tkinter.Button(innerFrame2, text = "BrowseImage",command=retrieveText1, width = 25).pack(padx="160",pady=(30,20))


def hideImage3(img,img1):
    o2.hide(img,img1)
    text1=tkinter.Text(innerFrame2,height='1', width="50")
    text1.pack(padx="55",pady=(40,20))
    text1.insert(tkinter.END,"Secrete Image was Hidden in the Image named 'Data Image'")
    text1.configure(state='disabled')
    
def hideImage2(img):
    filename = tkinter.filedialog.askopenfilename(title = "Select Image",filetypes = (("Image Files", "*.jpg"),("Image Files", "*.png"),("Image Files", "*.bmp") ))
    img1=cv2.imread(filename)
    tkinter.Button(innerFrame2, text = "Hide",command= lambda:hideImage3(img,img1), width = 25).pack(padx="160",pady=(30,20))
    
def hideImage1():
    filename = tkinter.filedialog.askopenfilename(title = "Select Image",filetypes = (("Image Files", "*.jpg"),("Image Files", "*.png"),("Image Files", "*.bmp") ))
    img=cv2.imread(filename)
    tkinter.Button(innerFrame2, text = "BrowseImage2",command= lambda:hideImage2(img), width = 25).pack(padx="160",pady=(30,20))
    
def hideImage():
    for widget in innerFrame2.winfo_children():
        widget.destroy()
    tkinter.Button(innerFrame2, text = "BrowseImage1",command=hideImage1, width = 25).pack(padx="160",pady=(30,20))

def retrieveImage2(img):
    o3.retrive(img)
    text1=tkinter.Text(innerFrame2,height='1', width="50")
    text1.pack(padx="30",pady=(40,20))
    text1.insert(tkinter.END,"Image Retrieved and stored with name 'Hidden Image'")
    text1.configure(state='disabled')

def retrieveImage1():
    filename = tkinter.filedialog.askopenfilename(title = "Select Image",filetypes = (("Image Files", "*.jpg"),("Image Files", "*.png"),("Image Files", "*.bmp") ))
    img=cv2.imread(filename)
    tkinter.Button(innerFrame2, text = "Retrive",command= lambda:retrieveImage2(img), width = 25).pack(padx="160",pady=(30,20))
    """text1=tkinter.Text(innerFrame2,height='1', width="50")
    text1.pack(padx="30",pady=(40,20))
    text1.insert(tkinter.END,"processing....")
    text1.configure(state='disabled')"""

def retrieveImage():
    for widget in innerFrame2.winfo_children():
        widget.destroy()  
    tkinter.Button(innerFrame2, text = "BrowseImage",command=retrieveImage1, width = 25).pack(padx="160",pady=(30,20))

    
    
    
root=tkinter.Tk()
#root.geometry('{}x{}'.format(1000,500))
root.geometry("1000x500")
root.resizable(width="FALSE",height="FALSE")
root.title("Image Stegnography")



#b=tkinter.Button(root, text="Barre Chaitanya")
#tkinter.Label(text="Bondam Shankar").pack()
#b.pack(padx=0, pady=0)

innerFrame1=tkinter.Frame(root,width="260",height="500",bg="red",bd="5", relief=tkinter.SUNKEN)#,colormap="new")
innerFrame1.pack(side="left",fill="y")

label=tkinter.Label(innerFrame1, text="Select Your Operation:",height='1', width="22",font= "Verdana 10 underline").pack(padx="28",pady=(80,20))

"""text=tkinter.Text(innerFrame1,height='1', width="22",font= "Verdana 10 underline")
text.pack(padx="30",pady=(40,20))
text.insert(tkinter.END,"Select Your Operation:")
text.configure(state='disabled')"""


button1=tkinter.Button(innerFrame1, text="Hide Text",width=25,command=hideText)
button2=tkinter.Button(innerFrame1, text="Retrieve Text",width=25,command=retrieveText)
button3=tkinter.Button(innerFrame1, text="Hide Image",width=25,command=hideImage)
button4=tkinter.Button(innerFrame1, text="Retrieve Image",width=25,command=retrieveImage)

button1.pack(padx=30, pady=(0,40))
button2.pack(padx=30, pady=(20,40))
button3.pack(padx=30, pady=(20,40))
button4.pack(padx=30, pady=(20,40))

#innerFrame1.bind("<Button-1>", callback())

innerFrame2=tkinter.Frame(root,width="1000",height="500",bg="black",bd="5", relief=tkinter.SUNKEN)#,colormap="new")
innerFrame2.pack(side="right",fill="both",padx=(100),pady=(90,90))

text1=tkinter.Text(innerFrame2,height='1', width="50")
text1.pack(padx="50",pady=(80,20))
text1.insert(tkinter.END,"Keep your Sensitive Data Secret")
text1.configure(state='disabled')

root.mainloop()
"""
c=5

while c!=0:
    print ("\n1.Hide Data\n2.Retrieve Data\n3.Hide Image\n4.Retrieve Image\n0.Exit")
    c=int(input("Select your option:"))
    if c==1:
        img=cv2.imread("C:/Users/DELL-PC/Desktop/Project/Code - Final/sam.jpg")
        file = open("Textfile.txt","r")

        f=file.read()
        file.close()
        o.hide(img,f)
    elif c==2:
        img=cv2.imread("C:/Users/DELL-PC/Desktop/Project/Code - Final/secreteImg.bmp")
        o1.retrive(img)
    elif c==3:
        img=cv2.imread("C:/Users/DELL-PC/Desktop/Project/Code - Final/sam.jpg")
        img1=cv2.imread("C:/Users/DELL-PC/Desktop/Project/Code/sam1.jpg")
        o2.hide(img,img1)
    elif c==4:
        img=cv2.imread("C:/Users/DELL-PC/Desktop/Project/Code - Final/secreteImg.bmp")
        o3.retrive(img)

"""
