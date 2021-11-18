import cv2
import codecs
import tkinter
from PIL import Image,ImageTk
import hidingt as o
import retrievingt as o1
import hidingi as o2
import retrievingi as o3
import encryption as o4
import decryption as o5


def hideText3(img,f,textk):
    k=textk.get("1.0","end-1c")

    f1=o4.encrypt(f,k)
    o.hide(img,f1)
    
    text1=tkinter.Text(innerFrame2,height='1', width="50")
    text1.pack(padx="55",pady=(20,10))
    text1.insert(tkinter.END,"Text Hidden in Image named 'Data Image'")
    text1.configure(state='disabled')
    
def hideText2(img):
    filename = tkinter.filedialog.askopenfilename(title = "Select File",filetypes = [("Text File", "*.txt"),("Document File","*.doc")])
    file = open(filename,"r")
    f=file.read()
    file.close()

    label=tkinter.Label(innerFrame2, text="Enter Key:",height='1', width="22",font= "Verdana 10 underline").pack(padx="28",pady=(10,0))
    textk=tkinter.Text(innerFrame2,height='1', width="50")
    #textk.insert(tkinter.0,"Enter Key")
    textk.pack(padx="55",pady=(0,20))    

    tkinter.Button(innerFrame2, text = "Hide",bg="red",bd="5",command= lambda:hideText3(img,f,textk), width = 25).pack(padx="160",pady=(10,10))
    
def hideText1():
    filename = tkinter.filedialog.askopenfilename(title = "Select Image",filetypes = (("Image Files", "*.jpg"),("Image Files", "*.png"),("Image Files", "*.bmp") ))
        
    img=cv2.imread(filename)
    tkinter.Button(innerFrame2, text = "BrowseFile",bg="red",bd="5",command= lambda:hideText2(img), width = 25).pack(padx="160",pady=(10,20))

def hideText():
    for widget in innerFrame2.winfo_children():
        widget.destroy()

    if2bimage = tkinter.Label(innerFrame2, image=image2)
    if2bimage.place(x=0, y=0, relwidth=1, relheight=1)

    tkinter.Button(innerFrame2, text = "BrowseImage",bg="red",bd="5",command=hideText1, width = 25).pack(padx="160",pady=(10,20))
    
def retriveText2(img,textk):
    k=textk.get("1.0","end-1c")
    f=o1.retrive(img)
    f1=o5.decrypt(f,k)
    
    file = open("SecreteData.txt","w",encoding="utf8")
    #print(f1)
    file.write(f1)
    file.close()
    
    text1=tkinter.Text(innerFrame2,height='1', width="57")
    text1.pack(padx="50",pady=(20,20))
    text1.insert(tkinter.END,"Text Retrieved and saved in File named 'SecreteData'")
    text1.configure(state='disabled')
    
def retrieveText1():
    filename = tkinter.filedialog.askopenfilename(title = "Select Image",filetypes = (("Image Files", "*.jpg"),("Image Files", "*.png"),("Image Files", "*.bmp") ))
    img=cv2.imread(filename)

    label=tkinter.Label(innerFrame2, text="Enter Key:",height='1', width="22",font= "Verdana 10 underline").pack(padx="28",pady=(10,0))
    textk=tkinter.Text(innerFrame2,height='1', width="50")
    #textk.insert(tkinter.0,"Enter Key")
    textk.pack(padx="55",pady=(0,20))    
    
    tkinter.Button(innerFrame2, text = "Retrieve",bg="red",bd="5",command= lambda:retriveText2(img,textk), width = 25).pack(padx="160",pady=(30,20))
    
def retrieveText():
    for widget in innerFrame2.winfo_children():
        widget.destroy()

    if2bimage = tkinter.Label(innerFrame2, image=image2)
    if2bimage.place(x=0, y=0, relwidth=1, relheight=1)
        
    img=tkinter.Button(innerFrame2, text = "BrowseImage",bg="red",bd="5",command=retrieveText1, width = 25).pack(padx="160",pady=(30,20))


def hideImage3(img,img1):
    rv=o2.hide(img,img1)
    if (rv==1):
        text1=tkinter.Text(innerFrame2,height='1', width="57")
        text1.pack(padx="15",pady=(20,20))
        text1.insert(tkinter.END,"Secrete Image was Hidden in the Image named 'Data Image'")
        text1.configure(state='disabled')
    else:
        text1=tkinter.Text(innerFrame2,height='1', width="57")
        text1.pack(padx="15",pady=(20,20))
        text1.insert(tkinter.END,"Size of secret image should be less than main image")
        text1.configure(state='disabled')
    
def hideImage2(img):
    filename = tkinter.filedialog.askopenfilename(title = "Select Image",filetypes = (("Image Files", "*.jpg"),("Image Files", "*.png"),("Image Files", "*.bmp") ))
    img1=cv2.imread(filename)
    tkinter.Button(innerFrame2, text = "Hide",bg="red",bd="5",command= lambda:hideImage3(img,img1), width = 25).pack(padx="160",pady=(30,20))
    
def hideImage1():
    filename = tkinter.filedialog.askopenfilename(title = "Select Image",filetypes = (("Image Files", "*.jpg"),("Image Files", "*.png"),("Image Files", "*.bmp") ))
    img=cv2.imread(filename)
    tkinter.Button(innerFrame2, text = "Browse Secret Image",bg="red",bd="5",command= lambda:hideImage2(img), width = 25).pack(padx="160",pady=(20,20))
    
def hideImage():
    for widget in innerFrame2.winfo_children():
        widget.destroy()

    if2bimage = tkinter.Label(innerFrame2, image=image2)
    if2bimage.place(x=0, y=0, relwidth=1, relheight=1)
    
    tkinter.Button(innerFrame2, text = "BrowseImage1",bg="red",bd="5",command=hideImage1, width = 25).pack(padx="160",pady=(20,0))

    text2=tkinter.Text(innerFrame2,height='1', width="57")
    text2.pack(padx="15",pady=(0,20))
    text2.insert(tkinter.END,"Please ensure that the Image1 is darker than SecretImage")
    text2.configure(state='disabled')
    
def retrieveImage2(img):
    o3.retrive(img)
    text1=tkinter.Text(innerFrame2,height='1', width="50")
    text1.pack(padx="30",pady=(40,20))
    text1.insert(tkinter.END,"Image Retrieved and stored with name 'Hidden Image'")
    text1.configure(state='disabled')

def retrieveImage1():
    filename = tkinter.filedialog.askopenfilename(title = "Select Image",filetypes = (("Image Files", "*.jpg"),("Image Files", "*.png"),("Image Files", "*.bmp") ))
    img=cv2.imread(filename)
    tkinter.Button(innerFrame2, text = "Retrive",bg="red",bd="5",command= lambda:retrieveImage2(img), width = 25).pack(padx="160",pady=(30,20))

def retrieveImage():
    for widget in innerFrame2.winfo_children():
        widget.destroy()
        
    if2bimage = tkinter.Label(innerFrame2, image=image2)
    if2bimage.place(x=0, y=0, relwidth=1, relheight=1)
    
    tkinter.Button(innerFrame2, text = "BrowseImage",bg="red",bd="5",command=retrieveImage1, width = 25).pack(padx="160",pady=(30,20))

    
root=tkinter.Tk()
root.geometry("1000x500")
root.resizable(width="False",height="False")
root.title("Image Stegnography")


image1 =Image.open('1.jpeg')
image = ImageTk.PhotoImage(image1)
rbimage = tkinter.Label(root, image=image)
rbimage.place(x=0, y=0, relwidth=1, relheight=1)


innerFrame1=tkinter.Frame(root,width="260",height="500",bg="red",bd="4", relief=tkinter.SUNKEN)#,colormap="new")
innerFrame1.pack(side="left",fill="y")

image5 =Image.open('5.jpg')
image4 = ImageTk.PhotoImage(image5)
if2bimage = tkinter.Label(innerFrame1, image=image4)
if2bimage.place(x=0, y=0, relwidth=1, relheight=1)



label=tkinter.Label(innerFrame1, text="Select Your Operation:",height='1', width="22",font= "Verdana 10 underline").pack(padx="28",pady=(80,20))

button1=tkinter.Button(innerFrame1, text="Hide Text",width=25,bg="red",bd="5",command=hideText)
button2=tkinter.Button(innerFrame1, text="Retrieve Text",width=25,bg="red",bd="5",command=retrieveText)
button3=tkinter.Button(innerFrame1, text="Hide Image",width=25,bg="red",bd="5",command=hideImage)
button4=tkinter.Button(innerFrame1, text="Retrieve Image",width=25,bg="red",bd="5",command=retrieveImage)

button1.pack(padx=30, pady=(0,40))
button2.pack(padx=30, pady=(20,40))
button3.pack(padx=30, pady=(20,40))
button4.pack(padx=30, pady=(20,40))


innerFrame2=tkinter.Frame(root,width="1000",height="500",bg="red",bd="4", relief=tkinter.SUNKEN)#,colormap="new")
innerFrame2.pack(side="right",fill="both",padx=(100),pady=(90,90))

image3 =Image.open('2.jpg')
image2 = ImageTk.PhotoImage(image3)
if2bimage = tkinter.Label(innerFrame2, image=image2)
if2bimage.place(x=0, y=0, relwidth=1, relheight=1)

text1=tkinter.Text(innerFrame2,height='1', width="50")
text1.pack(padx="50",pady=(80,20))
text1.insert(tkinter.END,"Keep your Sensitive Data Secret")
text1.configure(state='disabled')

root.mainloop()
