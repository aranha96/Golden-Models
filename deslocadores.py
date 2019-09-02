def shift2left(a):

    s = [0]*len(a)

    for i in range(len(a)):

        if i < 30:
            s[i] = a[i + 2]
        else:
            s[i] = 0
            
    return s

def shiftPCleft(a,b):

    s = [0]*32

    for i in range(32):

        if i < 4:
            s[i] = a[i]
        elif i < 30:
            s[i] = b[i - 4]
        else:
            s[i] = 0

    return s

def shiftExtend(a):

    s = []
    
    if a[0] == 0:
        for i in range(16):
            s.append(0)
        for i in range(16):
            s.append(a[i])
    else:
        for i in range(16):
            s.append(1)
        for i in range(16):
            s.append(a[i])

    return s

def write1(a):
    s = shift2left(a)
    file = open("shif2left.tv","a")

    for i in a:
        file.write(str(i))
    file.write("_")
    for j in s:
        file.write(str(j))
    file.write('\n')

def write2(a,b):
    s = shiftPCleft(a,b)
    file = open("shifPCleft.tv","a")

    for i in a:
        file.write(str(i))
    file.write("_")
    for j in b:
        file.write(str(j))
    file.write("_")
    for k in s:
        file.write(str(k))
    file.write('\n')

def write3(a):
    s = shiftExtend(a)
    file = open("shifExtend.tv","a")

    for i in a:
        file.write(str(i))
    file.write("_")
    for j in s:
        file.write(str(j))
    file.write('\n')

a0 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
a1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
a2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
a3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
a4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
a5 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
a6 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
a7 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
a8 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
a9 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
b0 = [0,0,0,0]
b1 = [0,0,1,1]
b2 = [1,1,0,0]
b3 = [1,1,1,1]
c0 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
c1 = [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
c2 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0]
c3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
d0 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
d1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
d2 = [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
d3 = [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
d4 = [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
d5 = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

write1(a0)
write1(a1)
write1(a2)
write1(a3)
write1(a4)
write1(a5)
write1(a6)
write1(a7)
write1(a8)
write1(a9)
write2(b0,c0)
write2(b1,c1)
write2(b2,c2)
write2(b3,c3)
write3(d0)
write3(d1)
write3(d2)
write3(d3)
write3(d4)
write3(d5)
