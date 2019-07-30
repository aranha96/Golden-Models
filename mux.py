def mux(entrada_A, entrada_B, en):

    saida = []
    if en == 0:
        for i in entrada_A:
            saida.append(i)

    else:
        for j in entrada_B:
            saida.append(j)

    return saida

def escrever(a,b, enable, saida):
    file = open("mux.tv", "a")
    
    for i in a:
        file.write(str(i))

    file.write("_")
		
    for k in b:
        file.write(str(k))
        
    file.write("_")
    file.write(str(enable))
    file.write("_")
    
    for j in saida:
        file.write(str(j))
    file.write('\n')
    file.close()

a = [1,0,0,1]
b = [0,0,0,0]

s = mux(a,b,0)
escrever(a,b,0,s)
