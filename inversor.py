

def inversor(lista):
    saida = []

    for i in lista:
        if i == 1:
            saida.append(0)
        elif i == 0:
            saida.append(1)
        else:
            return print("error non binary value detected")

    return saida

def escrever(lista, saida):
    file = open("inv.tv", "w")
    
    for i in lista:
        file.write(str(i))
        
    file.write("_")
    
    for j in saida:
        file.write(str(j))

    file.close()
  
    
    
a = [0,1,1,0,0,0,0,0,1,0,1,1,1,1]
s = inversor(a)
escrever(a, s)
