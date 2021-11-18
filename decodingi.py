import cv2
import numpy as np

def decode(img):
#img=cv2.imread("C:/Users/DELL-PC/Desktop/Project/Code/secreteImg.bmp")
    #rows=int(img[len(img)-1][len(img[0])-1][0])
    #cols=int(img[len(img)-1][len(img[0])-1][1])

    cols=(img[len(img)-1][len(img[0])-1][0]*255)+img[len(img)-1][len(img[0])-1][1]
    rows=(img[len(img)-1][len(img[0])-2][0]*255)+img[len(img)-1][len(img[0])-2][1]
    #print(rows)
    #print(cols)
    #print(rows*cols)
    #print(img.size//3)

    img1= np.zeros([rows,cols,3], dtype = int)
    #print(img1)

    j=0
    k=0
    l=rows-1
    m=cols-1
    #for i in range(0,img.size//3):
    for i in range(0,rows*cols):
        b_fr=list(format(img[j][k][0],'b'))
        b_fg=list(format(img[j][k][1],'b'))
        b_fb=list(format(img[j][k][2],'b'))

        if len(b_fr)<8:
            l1=8-len(b_fr)
            for i in range(0,l1):
                b_fr.insert(0,'0')
        if len(b_fg)<8:
            l1=8-len(b_fg)
            for i in range(0,l1):
                b_fg.insert(0,'0')
        if len(b_fb)<8:
            l1=8-len(b_fb)
            for i in range(0,l1):
                b_fb.insert(0,'0')

        b_fr[0]=b_fr[5]       
        b_fr[1]=b_fr[6]
        b_fr[2]=b_fr[7]
        b_fr[3]=b_fr[4]
    
        b_fr[4]='0' 
        b_fr[5]='0'
        b_fr[6]='0'
        b_fr[7]='0'
    
    
        b_fg[0]=b_fg[5]       
        b_fg[1]=b_fg[6]
        b_fg[2]=b_fg[7]
        b_fg[3]=b_fg[4]
    
        b_fg[4]='0'    
        b_fg[5]='0'
        b_fg[6]='0'
        b_fg[7]='0'
    
    
        b_fb[0]=b_fb[5]   
        b_fb[1]=b_fb[6]
        b_fb[2]=b_fb[7]
        b_fb[3]=b_fb[4]
    
        b_fb[4]='0'
        b_fb[5]='0'
        b_fb[6]='0'
        b_fb[7]='0'
    
        #print(b_fr)
        #print(b_fg)
        #print(b_fb)
        
        b_fr=''.join(b_fr)
        b_fg=''.join(b_fg)
        b_fb=''.join(b_fb)
    
        #print(j)
        #print(k)
        img1[l][m][0]=int(b_fr, 2)
        img1[l][m][1]=int(b_fg, 2)
        img1[l][m][2]=int(b_fb, 2)   
    
    
        if k<(cols-1):
            k=k+1
            m=m-1
        elif j<(rows-1):
            k=0
            m=cols-1
            j=j+1
            l=l-1
    #print(len(img[0])-1)
    
    #print(img1)
    return img1
    
#cv2.imwrite("C:/Users/DELL-PC/Desktop/Project/Code/hiddenImg.bmp",img1)
    
