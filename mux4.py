def mux4(a,b,c,d,en):

    saida = 0

    if en[0] == 0 and en[1] == 0:
        saida = a
    if en[0] == 0 and en[1] == 1:
        saida = b
    if en[0] == 1 and en[1] == 0:
        saida = c
    if en[0] == 1 and en[1] == 1:
        saida = d

    return saida

def write(a,b,c,d,en,s):
    file = open("mux4.tv", "a")

    file.write(str(a))
    file.write("_")
    file.write(str(b))
    file.write("_")
    file.write(str(c))
    file.write("_")
    file.write(str(d))
    file.write("_")
    file.write(str(en[0]))
    file.write("_")
    file.write(str(en[1]))
    file.write("_")
    file.write(str(s))
    file.write('\n')
    file.close()


a = 0
b = 1
c = 1
d = 0
en0 = [0,0]
en1 = [1,0]
en2 = [0,1]
en3 = [1,1]
enx = ['x','x']
write('x','x','x','x',enx,'x')
s = mux4(a,b,c,d,en0)
write(a,b,c,d,en0,s)
s = mux4(a,b,c,d,en1)
write(a,b,c,d,en1,s)
s = mux4(a,b,c,d,en2)
write(a,b,c,d,en2,s)
s = mux4(a,b,c,d,en3)
write(a,b,c,d,en3,s)
