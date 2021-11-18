def decode(img):

    
    msg_len=(img[len(img)-1][len(img[0])-1][0]*255)+img[len(img)-1][len(img[0])-1][1] #mistake here should be modified

    #print(img[len(img)-1][len(img[0])-1][0])
    #print((img[len(img)-1][len(img[0])-1][0]*255)+img[len(img)-1][len(img[0])-1][1])
    #print(msg_len)
    
    data=[]
    j=0
    k=0
    for i in range(0,msg_len):

        f=[]

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
        
        f.append(b_fr[5])
        f.append(b_fr[6])
        f.append(b_fr[7])

        f.append(b_fg[5])
        f.append(b_fg[6])
        f.append(b_fg[7])

        f.append(b_fb[6])
        f.append(b_fb[7])

        f=''.join(f)

        data.append(chr(int(f,2)))
        

        if k<(len(img[0])-1):
            k=k+1
        else:
            k=0
            j=j+1
    
    data=''.join(data)
    
    return data;
