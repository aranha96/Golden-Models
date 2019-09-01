def mux4(a,b,c,d,s0,s1):

    y = 0

    if s0 == 0 and s1 == 0:
        y = a
    if s0 == 1 and s1 == 0:
        y = b
    if s0 == 0 and s1 == 1:
        y = c
    if s0 == 1 and s1 == 1:
        y = d

    return y

def mux2(a,b,s):

    y = 0
    
    if s == 0:
        y = a

    else:
        y = b

    return y
	
	
def mux32(a,s):

    yp = [0]*8
    yp_2 = [0]*2
    tamanho = len(a) - 1
    tamanho_2 = 7

    for i in range(8):
       yp[7 - i] = mux4(a[tamanho-(4*i)],a[tamanho-(4*i+1)],a[tamanho-(4*i+2)],a[tamanho-(4*i+3)],s[4],s[3])
        
    for j in range(2):
       yp_2[1 - j] = mux4(yp[tamanho_2-(4*j)],yp[tamanho_2-(4*j+1)],yp[tamanho_2-(4*j+2)],yp[tamanho_2-(4*j+3)],s[2],s[1])

    y = mux2(yp_2[1],yp_2[0],s[0])

    return y

def write(a,s,y):

    file = open("mux32.tv","a")

    for i in a:
        file.write(str(i))
    file.write("_")
    for j in s:
        file.write(str(j))
    file.write("_")
    file.write(str(y))
    file.write('\n')
    file.close()

a = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
s0 = [0,0,0,0,0]
s1 = [0,0,0,0,1]
s2 = [0,0,0,1,0]
s3 = [0,0,0,1,1]
s4 = [0,0,1,0,0]
s5 = [0,0,1,0,1]
s6 = [0,0,1,1,0]
s7 = [0,0,1,1,1]
s8 = [0,1,0,0,0]
s9 = [0,1,0,0,1]
s10 = [0,1,0,1,0]
s11 = [0,1,0,1,1]
s12 = [0,1,1,0,0]
s13 = [0,1,1,0,1]
s14 = [0,1,1,1,0]
s15 = [0,1,1,1,1]
s16 = [1,0,0,0,0]
s17 = [1,0,0,0,1]
s18 = [1,0,0,1,0]
s19 = [1,0,0,1,1]
s20 = [1,0,1,0,0]
s21 = [1,0,1,0,1]
s22 = [1,0,1,1,0]
s23 = [1,0,1,1,1]
s24 = [1,1,0,0,0]
s25 = [1,1,0,0,1]
s26 = [1,1,0,1,0]
s27 = [1,1,0,1,1]
s28 = [1,1,1,0,0]
s29 = [1,1,1,0,1]
s30 = [1,1,1,1,0]
s31 = [1,1,1,1,1]

y0 = mux32(a,s0)
write(a,s0,y0)
y1 = mux32(a,s1)
write(a,s1,y1)
y2 = mux32(a,s2)
write(a,s2,y2)
y3 = mux32(a,s3)
write(a,s3,y3)
y4 = mux32(a,s4)
write(a,s4,y4)
y5 = mux32(a,s5)
write(a,s5,y5)
y6 = mux32(a,s6)
write(a,s6,y6)
y7 = mux32(a,s7)
write(a,s7,y7)
y8 = mux32(a,s8)
write(a,s8,y8)
y9 = mux32(a,s9)
write(a,s9,y9)
y10 = mux32(a,s10)
write(a,s10,y10)
y11 = mux32(a,s11)
write(a,s11,y11)
y12 = mux32(a,s12)
write(a,s12,y12)
y13 = mux32(a,s13)
write(a,s13,y13)
y14 = mux32(a,s14)
write(a,s14,y14)
y15 = mux32(a,s15)
write(a,s15,y15)
y16 = mux32(a,s16)
write(a,s16,y16)
y17 = mux32(a,s17)
write(a,s17,y17)
y18 = mux32(a,s18)
write(a,s18,y18)
y19 = mux32(a,s19)
write(a,s19,y19)
y20 = mux32(a,s20)
write(a,s20,y20)
y21 = mux32(a,s21)
write(a,s21,y21)
y22 = mux32(a,s22)
write(a,s22,y22)
y23 = mux32(a,s23)
write(a,s23,y23)
y24 = mux32(a,s24)
write(a,s24,y24)
y25 = mux32(a,s25)
write(a,s25,y25)
y26 = mux32(a,s26)
write(a,s26,y26)
y27 = mux32(a,s27)
write(a,s27,y27)
y28 = mux32(a,s28)
write(a,s28,y28)
y29 = mux32(a,s29)
write(a,s29,y29)
y30 = mux32(a,s30)
write(a,s30,y30)
y31 = mux32(a,s31)
write(a,s31,y31)
