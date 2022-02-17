# from collections import ChainMap
#l=[{"a":"abc","b":"abc","c":"abc"},{1:123,2:123,3:123},{"p":"pqr","q":"pqr"}]
# d=dict(ChainMap(*l))
# print(d)
x={}
def mk(l):
    x.update(l)
    return x
d=[{'e':4,'f':5,'g':6},{'a':1,'b':2,'c':3},{'p':8,'o':90},{'x':00,'y':89,'z':88}]
x1=tuple(map(mk,d))
l1=list(x.keys())
l2=list(x.values())
d=dict(zip(l1,l2))
print(d)
