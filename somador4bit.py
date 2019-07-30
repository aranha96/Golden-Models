def somador1bit(a, b, cin):
    saida = 0
    cout = 0
    
    if cin == 0:
        if a + b == 0:
            saida = 0
            cout = 0
        if a + b == 1:
            saida = 1
            cout = 0
        if a + b == 2:
            saida = 0
            cout = 1
    else:
        if a + b == 0:
            saida = 1
            cout = 0
        if a + b == 1:
            saida = 0
            cout = 1
        if a + b == 2:
            saida = 1
            cout = 1

    return saida, cout

def somador4bit(a,b,cin):
    saida = [0]*len(a)
    cout = [0]*len(a)
    s = 0
    c = cin
    tamanho = len(a) - 1
    
    for i in range(len(a)):
        s,c = somador1bit(a[tamanho - i],b[tamanho - i],c)
        saida[tamanho - i] = s
        cout[tamanho - i] = c

    return saida, cout

def escrever(a, b, cin, saida, cout):
    file = open("somador4bit.tv", "a")

    for i in a:
        file.write(str(i))
    file.write("_")

    for j in b:    
        file.write(str(j))
    file.write("_")

    file.write(str(cin))
    file.write("_")

    for k in saida:
        file.write(str(k))
    file.write("_")

    for l in cout:
        file.write(str(l))
    file.write('\n')
    file.close()

def decimalconv(a):
    dec = 0
    tamanho = len(a)- 1

    for i in range(len(a)):
        dec = (dec + ((2**i)*a[tamanho - i]))

    return dec

a = [0,0,0,0]
b = [1,1,1,1]
c = [0,0,0,1]
d = [1,1,0,1]
e = [0,0,1,0]
f = [1,0,0,0]

s0,c0 = somador4bit(a,b,0) #1111 - 0000
s1,c1 = somador4bit(c,d,0) #1110 - 0001
s2,c2 = somador4bit(e,f,0) #1010 - 0000
s3,c3 = somador4bit(a,c,0) #0001 - 0000
s4,c4 = somador4bit(a,d,0) #1101 - 0000
s5,c5 = somador4bit(a,f,0) #1000 - 0000
s6,c6 = somador4bit(b,c,0) #0000 - 1111
s7,c7 = somador4bit(d,e,0) #1111 - 0000

escrever(a,b,0,s0,c0)
escrever(c,d,0,s1,c1)
escrever(e,f,0,s2,c2)
escrever(a,c,0,s3,c3)
escrever(a,d,0,s4,c4)
escrever(a,f,0,s5,c5)
escrever(b,c,0,s6,c6)
escrever(d,e,0,s7,c7)
