def encrypt(f,k):

    f1=[]
    for i in range(0,len(f)):
        #print(ord(f[i]))
        #print(chr(ord(f[i])))
        f1.append(chr(ord(f[i])+int(k)))

    f=''.join(f1)
       
    return f;
