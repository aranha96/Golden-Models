def escrever(d,q):
        file = open("registrador.tv","a")
        for i in d:
                file.write(str(i))
        file.write("_")
        for j in q:
                file.write(str(j))
        file.write('\n')
        file.close()

def acumulador(clk,d):
        q = ["x"]*len(d)

        for i in range(len(clk)):
                if clk[i] > clk[i-1]:
                        escrever(d,q)
                        q = d
                else:
                        q = q
                

clock = [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]
d = [0,0,1,0]

acumulador(clock,d)



