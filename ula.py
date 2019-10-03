def funand(a,b):

    if a == b:
        s = a
    else:
        s = 0
    return s

def funor(a,b):

    if a == b:
        s = a
    else:
        s = 1
    return s

def somador(a, b, cin):
    s = 0
    cout = 0
    
    if cin == 0:
        if a + b == 0:
            s = 0
            cout = 0
        if a + b == 1:
            s = 1
            cout = 0
        if a + b == 2:
            s = 0
            cout = 1
    else:
        if a + b == 0:
            s = 1
            cout = 0
        if a + b == 1:
            s = 0
            cout = 1
        if a + b == 2:
            s = 1
            cout = 1

    return s, cout

def funnor(a,b):

    if a == b:
        if a == 1:
            s = 0
        else:
            s = 1
    else:
        s = 0
    return s

def funxor(a,b):

    if a == b:
        s = 0
    else:
        s = 1
    return s

def funnand(a,b):

    if a == b:
        if a == 1:
            s = 0
        else:
            s = 1
    else:
        s = 1
    return s

def funset(a):

    if a == 0:
        s = 1
        cout = 0       
    else:
        s = 0
        cout = 1
    return s,cout

def funslt(a,b):

    if a < b:
        s = 1
    else:
        s = 0
    return s

def ULA(a,b,en):

    s = 0
    
    switch = {
        0: funand(a,b),
        1: funor(a,b),
        2: somador(a,b,0),
        3: funnor(a,b),
        4: funxor(a,b),
        5: funnand(a,b),
        6: funset(a),
        7: funslt(a,b)
    }

    return switch.get(en, "erro")


