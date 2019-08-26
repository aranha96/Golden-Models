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

def write(key,out):

    file = open("decoder.tv", "a")

    for i in key:
        file.write(str(i))
    file.write("_")
    for j in out:
        file.write(str(j))
    file.write('\n')
    file.close
    

a0 = [0,0,0,0,0]
a1 = [0,0,0,0,1]
a2 = [0,0,0,1,0]
a3 = [0,0,0,1,1]
a4 = [0,0,1,0,0]
a5 = [0,0,1,0,1]
a6 = [0,0,1,1,0]
a7 = [0,0,1,1,1]
a8 = [0,1,0,0,0]
a9 = [0,1,0,0,1]
a10 = [0,1,0,1,0]
a11 = [0,1,0,1,1]
a12 = [0,1,1,0,0]
a13 = [0,1,1,0,1]
a14 = [0,1,1,1,0]
a15 = [0,1,1,1,1]
a16 = [1,0,0,0,0]
a17 = [1,0,0,0,1]
a18 = [1,0,0,1,0]
a19 = [1,0,0,1,1]
a20 = [1,0,1,0,0]
a21 = [1,0,1,0,1]
a22 = [1,0,1,1,0]
a23 = [1,0,1,1,1]
a24 = [1,1,0,0,0]
a25 = [1,1,0,0,1]
a26 = [1,1,0,1,0]
a27 = [1,1,0,1,1]
a28 = [1,1,1,0,0]
a29 = [1,1,1,0,1]
a30 = [1,1,1,1,0]
a31 = [1,1,1,1,1]


out = decoder(a0)
write(a0,out)
out = decoder(a1)
write(a1,out)
out = decoder(a2)
write(a2,out)
out = decoder(a3)
write(a3,out)
out = decoder(a4)
write(a4,out)
out = decoder(a5)
write(a5,out)
out = decoder(a6)
write(a6,out)
out = decoder(a7)
write(a7,out)
out = decoder(a8)
write(a8,out)
out = decoder(a9)
write(a9,out)
out = decoder(a10)
write(a10,out)
out = decoder(a11)
write(a11,out)
out = decoder(a12)
write(a12,out)
out = decoder(a13)
write(a13,out)
out = decoder(a14)
write(a14,out)
out = decoder(a15)
write(a15,out)
out = decoder(a16)
write(a16,out)
out = decoder(a17)
write(a17,out)
out = decoder(a18)
write(a18,out)
out = decoder(a19)
write(a19,out)
out = decoder(a20)
write(a20,out)
out = decoder(a21)
write(a21,out)
out = decoder(a22)
write(a22,out)
out = decoder(a23)
write(a23,out)
out = decoder(a24)
write(a24,out)
out = decoder(a25)
write(a25,out)
out = decoder(a26)
write(a26,out)
out = decoder(a27)
write(a27,out)
out = decoder(a28)
write(a28,out)
out = decoder(a29)
write(a29,out)
out = decoder(a30)
write(a30,out)
out = decoder(a31)
write(a31,out)






































