
def hung(a):
    
    if  a<5:
         m=("not hungry")
    elif 5 <=a <=10:
         m=(" a bit hungry")
    elif 11 <=a<=15:
         m=("hungry")
    else:
        m= (" staving !!!")

    return str(m)
 

def wounded(b):
     
    if  b==100:
        d=("fighting fit !!")
    elif 70 <=b<=99:
        d=("in good health")
    elif 40<=b<=69:
        d=(" bleeding bad")
    else:
        d=("very wounded")

    return str(d)


def left_behind():
    
    print("functions that not been imported ")
