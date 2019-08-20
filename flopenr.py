def flopenr(d,en,ck,rt):
        global flag,q
        
        if rt == 1:
            q = 0
            return q
        if ck == 0 and en == 0:
            flag = 0
            return q
        if ck == 0 and en == 1:
            flag = 1
            return q
        if ck == 1 and flag == 1:
            q = d
            return q
        if ck == 1 and flag == 0:
            return q
        
def write(d,en,ck,rt,q):
        
        file = open("flopenr.tv","a")
        file.write(str(d))
        file.write("_")
        file.write(str(en))
        file.write("_")
        file.write(str(ck))
        file.write("_")
        file.write(str(rt))
        file.write("_")
        file.write(str(q))
        file.write('\n')
        file.close()
        
def loop(d,en,ck,rt):
        global q
        
        for i in range(len(d)):

                q = flopenr(d[i],en[i],ck[i],rt[i])
                write(d[i],en[i],ck[i],rt[i],q)
        

ck = [0,1,0,1,0,1,0,1,0,1,0,1]
d = [0,0,0,0,1,1,1,1,0,0,1,1]
en = [0,0,1,1,0,0,1,1,0,0,1,1]
rt = [1,1,1,1,1,1,1,1,0,0,0,0]
q = 'x'
flag = 0

loop(d,en,ck,rt)

