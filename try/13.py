'''[( ca,('cat', 'car', 'fear', 'center'))]'''

l=input("Enter list with \",\" :")
str=l.split(",")
s=input("Enter prefix:")
l2=[]
k=len(s)
def check(s,str):

    for i in str:
        r=i[0:k]
        if s==r:
            l2.append(i)
        else:
            continue

check(s,str)
print(l2)

