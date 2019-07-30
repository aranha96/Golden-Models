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

def escrever(a, b, cin, cout, saida):
    file = open("mux.tv", "a")

    
    file.write(str(a))
    file.write("_")
        
    file.write(str(b))
    file.write("_")
    
    file.write(str(cin))
    file.write("_")
    
    file.write(str(saida))
    file.write("_")

    file.write(str(cout))
    file.write('\n')
    file.close()


s0,c0 = somador1bit(0,0,0)
s1,c1 = somador1bit(0,0,1)
s2,c2 = somador1bit(0,1,0)
s3,c3 = somador1bit(0,1,1)
s4,c4 = somador1bit(1,0,0)
s5,c5 = somador1bit(1,0,1)
s6,c6 = somador1bit(1,1,0)
s7,c7 = somador1bit(1,1,1)

escrever(0,0,0,c0,s0)
escrever(0,0,1,c1,s1)
escrever(0,1,0,c2,s2)
escrever(0,1,1,c3,s3)
escrever(1,0,0,c4,s4)
escrever(1,0,1,c5,s5)
escrever(1,1,0,c6,s6)
escrever(1,1,1,c7,s7)

