x = {(1,2,3):"steel",(1,2,4):"steel",(1,2,6):"steel",(1,3,3):"steel",(1,3,3):"steel",(2,2,6):"steel",(2,3,3):"steel",(2,3,1):"steel"}


def getOnX(d,i):
    c = {}
    for k,v in d.items():
        if k[0] == i:
            c[k]=v
    return c


def getOnY(d,i):
    c = {}
    for k,v in d.items():
        if k[1] == i:
            c[k]=v
    return c


def getOnZ(d,i):
    c = {}
    for k,v in d.items():
        if k[2] == i:
            c[k]=v
    return c

def getOnXY(d,x,y):
    return getOnY(getOnX(d,x),y)

def getOnYZ(d,y,z):
    return getOnY(getOnZ(d,z),y)

def getOnXZ(d,x,z):
    return getOnZ(getOnX(d,x),z)





