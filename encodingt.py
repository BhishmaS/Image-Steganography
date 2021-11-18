def encode(img,f):

    img[len(img)-1][len(img[0])-1][0]=len(f)//255 #mistake here should be modified
    img[len(img)-1][len(img[0])-1][1]=len(f)%255

    #print(len(f))
    #print(len(img)*len(img[0]))
    j=0
    k=0
    for i in range(0,len(f)):
        c=f[i]
        
        b_f=format(ord(c), 'b')
        l=len(b_f)

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
        if l==8:
            b_fr[5]=b_f[0]
            b_fr[6]=b_f[1]
            b_fr[7]=b_f[2]

            b_fg[5]=b_f[3]
            b_fg[6]=b_f[4]
            b_fg[7]=b_f[5]

            b_fb[6]=b_f[6]
            b_fb[7]=b_f[7]
        elif l==7:
            b_fr[5]='0'
            b_fr[6]=b_f[0]
            b_fr[7]=b_f[1]

            b_fg[5]=b_f[2]
            b_fg[6]=b_f[3]
            b_fg[7]=b_f[4]

            b_fb[6]=b_f[5]
            b_fb[7]=b_f[6]
        elif l==6:
            b_fr[5]='0'
            b_fr[6]='0'
            b_fr[7]=b_f[0]

            b_fg[5]=b_f[1]
            b_fg[6]=b_f[2]
            b_fg[7]=b_f[3]

            b_fb[6]=b_f[4]
            b_fb[7]=b_f[5]
        elif l==5:
            b_fr[5]='0'
            b_fr[6]='0'
            b_fr[7]='0'

            b_fg[5]=b_f[0]
            b_fg[6]=b_f[1]
            b_fg[7]=b_f[2]
            
            b_fb[6]=b_f[3]
            b_fb[7]=b_f[4]
        elif l==4:
            b_fr[5]='0'
            b_fr[6]='0'
            b_fr[7]='0'

            b_fg[5]='0'
            b_fg[6]=b_f[0]
            b_fg[7]=b_f[1]

            b_fb[6]=b_f[2]
            b_fb[7]=b_f[3]
        elif l==3:
            b_fr[5]='0'
            b_fr[6]='0'
            b_fr[7]='0'

            b_fg[5]='0'
            b_fg[6]='0'
            b_fg[7]=b_f[0]

            b_fb[6]=b_f[1]
            b_fb[7]=b_f[2]
        elif l==2:
            b_fr[5]='0'
            b_fr[6]='0'
            b_fr[7]='0'

            b_fg[5]='0'
            b_fg[6]='0'
            b_fg[7]='0'

            b_fb[6]=b_f[0]
            b_fb[7]=b_f[1]
        elif l==1:
            b_fr[5]='0'
            b_fr[6]='0'
            b_fr[7]='0'

            b_fg[5]='0'
            b_fg[6]='0'
            b_fg[7]='0'

            b_fb[6]='0'
            b_fb[7]=b_f[0]
       
        b_fr=''.join(b_fr)
        b_fg=''.join(b_fg)
        b_fb=''.join(b_fb)
        
        img[j][k][0]=int(b_fr, 2)
        img[j][k][1]=int(b_fg, 2)
        img[j][k][2]=int(b_fb, 2)
        
        
        if k<(len(img[0])-1):
            k=k+1
        else:
            k=0
            j=j+1
    
    return img;
