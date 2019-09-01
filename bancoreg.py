def binconv(a):

    dec = 0
    tamanho = len(a)- 1

    for i in range(len(a)):
        dec = (dec + ((2**i)*a[tamanho - i]))

    return dec

def decoder(key):

    out = [0]*32
    tamanho = len(out) - 1

    i = binconv(key)

    out[tamanho - i] = 1

    return out

def mux4(a,b,c,d,s0,s1):

    y = 0

    if s0 == 0 and s1 == 0:
        y = a
    if s0 == 1 and s1 == 0:
        y = b
    if s0 == 0 and s1 == 1:
        y = c
    if s0 == 1 and s1 == 1:
        y = d

    return y

def mux2(a,b,s):

    y = 0
    
    if s == 0:
        y = a

    else:
        y = b

    return y
		
def mux32(a,s):

    yp = [0]*8
    yp_2 = [0]*2
    tamanho = len(a) - 1
    tamanho_2 = 7

    for i in range(8):
       yp[7 - i] = mux4(a[tamanho-(4*i)],a[tamanho-(4*i+1)],a[tamanho-(4*i+2)],a[tamanho-(4*i+3)],s[4],s[3])
        
    for j in range(2):
       yp_2[1 - j] = mux4(yp[tamanho_2-(4*j)],yp[tamanho_2-(4*j+1)],yp[tamanho_2-(4*j+2)],yp[tamanho_2-(4*j+3)],s[2],s[1])

    y = mux2(yp_2[1],yp_2[0],s[0])

    return y

def decconv(dec):
    
    conv = [0]*5
    pos = 0

    for i in bin(dec)[2:].zfill(5):
        conv[pos] = int(i)
        pos = pos + 1
        
    return conv

def bancoreg(sa,sb,key,reset,wd,we):

    data = ['x']*32
    out_dec = decoder(key)
    index = binconv(key)
    
    if we == 1:
        data[31 - index] = wd
    if reset == 1:
        data[31 - index] = 0
        
    reg1 = mux32(data,sa)
    reg2 = mux32(data,sb)

    return reg1,reg2

def write(reset,wd,we):
    
    file = open("bancoreg.tv","a")
    for i in range(32):
        sa = decconv(i)
        sb = decconv(i)
        key = decconv(i)
        reg1,reg2 = bancoreg(sa,sb,key,reset,wd,we)
        
        for c in range(2):
            for j in sa:
                file.write(str(j))
            file.write("_")

            for k in sb:
                file.write(str(k))
            file.write("_")

            for l in key:
                file.write(str(l))
            file.write("_")

            file.write(str(c))
            file.write("_")
            file.write(str(reset))
            file.write("_")
            file.write(str(wd))
            file.write("_")
            file.write(str(we))
            file.write("_")
            if c == 0:
                file.write(str(0))
                file.write("_")
                file.write(str(0))
            else:
                file.write(str(reg1))
                file.write("_")
                file.write(str(reg2))
            file.write('\n')
        


write(1,1,1)
write(0,1,1)

    
