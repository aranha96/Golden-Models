def tristate(entrada, enable):
    saida = []
    
    if enable == 1:
        for i in entrada:
            saida.append(i)
    else:
        for j in entrada:
            saida.append("z")
            
    return saida

def escrever(entrada, enable, saida):
    file = open("tristate.tv", "a")
    
    for i in entrada:
        file.write(str(i))
        
    file.write("_")
    file.write(str(enable))
    file.write("_")
    
    for j in saida:
        file.write(str(j))
    file.write('\n')
    file.close()

a = [0,0,0,0]
b = [1,1,1,1]
en0 = 0
en1 = 1

s0 = tristate(a, en0)
escrever(a,en0,s0)
s1 = tristate(a, en1)
escrever(a,en1,s1)
s2 = tristate(b, en0)
escrever(b,en0,s2)
s3 = tristate(b, en1)
escrever(b,en1,s3)
