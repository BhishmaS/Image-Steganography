import cv2

#img=cv2.imread("C:/Users/DELL-PC/Desktop/Project/Code/sam.jpg")
#img1=cv2.imread("C:/Users/DELL-PC/Desktop/Project/Code/sam1.jpg")

#print(len(img[0]))
#print(len(img1[0]))
#print(len(img1))
#print(img1.size//3)
def encode(img,img1):
    
    img[len(img)-1][len(img[0])-1][0]=len(img1[0])//255
    img[len(img)-1][len(img[0])-1][1]=len(img1[1])%255
    img[len(img)-1][len(img[0])-2][0]=len(img1)//255
    img[len(img)-1][len(img[0])-2][1]=len(img1)%255
    rows=(img[len(img)-1][len(img[0])-1][0]*255)+img[len(img)-1][len(img[0])-1][1]
    cols=(img[len(img)-1][len(img[0])-2][0]*255)+img[len(img)-1][len(img[0])-2][1]
    #print(rows)
    #print(cols)

    j=0
    k=0
    l=len(img1)-1
    m=len(img1[0])-1
    #print(l)
    #print(m)
    for i in range(0,img1.size//3):
        b_fr=list(format(img[j][k][0],'b'))
        b_fg=list(format(img[j][k][1],'b'))
        b_fb=list(format(img[j][k][2],'b'))
    
        b_fr1=list(format(img1[l][m][0],'b'))
        b_fg1=list(format(img1[l][m][1],'b'))
        b_fb1=list(format(img1[l][m][2],'b'))
        
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

        if len(b_fr1)<8:
            l1=8-len(b_fr1)
            for i in range(0,l1):
                b_fr1.insert(0,'0')
        if len(b_fg1)<8:
            l1=8-len(b_fg1)
            for i in range(0,l1):
                b_fg1.insert(0,'0')
        if len(b_fb1)<8:
            l1=8-len(b_fb1)
            for i in range(0,l1):
                b_fb1.insert(0,'0')

    
        b_fr[4]=b_fr1[3]       
        b_fr[5]=b_fr1[0]
        b_fr[6]=b_fr1[1]
        b_fr[7]=b_fr1[2]
    
        b_fg[4]=b_fg1[3]       
        b_fg[5]=b_fg1[0]
        b_fg[6]=b_fg1[1]
        b_fg[7]=b_fg1[2]

        b_fb[4]=b_fb1[3]   
        b_fb[5]=b_fb1[0]
        b_fb[6]=b_fb1[1]
        b_fb[7]=b_fb1[2]
    
        #print(b_fr)
        #print(b_fg)
        #print(b_fb)
    
        b_fr=''.join(b_fr)
        b_fg=''.join(b_fg)
        b_fb=''.join(b_fb)
        
        img[j][k][0]=int(b_fr, 2)
        img[j][k][1]=int(b_fg, 2)
        img[j][k][2]=int(b_fb, 2)   

        if k<(len(img1[0])-1):
            k=k+1
            m=m-1
        else:
            k=0
            m=len(img1[0])-1
            l=l-1
            j=j+1

    return img
#cv2.imwrite("C:/Users/DELL-PC/Desktop/Project/Code/secreteImg.bmp",img)
