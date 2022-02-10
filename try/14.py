s=input("Enter list \',\' :")
l=s.split(",")
l2=[]
def check(l):
    for i in l:
        l2.append(len(i))
    return l2

check(l)
print(l2)
