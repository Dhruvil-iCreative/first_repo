def f1(x=20,y=50,z=90):
    return x,y*15,z
a,b,c=f1(y=40,x=40,z={})
print(a,b,c)