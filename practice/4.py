def f1(x,y,z):
    return x,y*15,z
a,b,c=f1(y=50,x=40,z={})

print(a,b,c)