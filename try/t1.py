sen=(input("Enter sentence:"))
l=sen.split(" ")
l2=[]
l3=[]
def check(l):
    for i in l:
        if l.count(i)>=2:
            if i not in l2:
                l2.append(i)
            else:
                pass
        else:
            l3.append(i)
check(l)
print(l2)
print("#".join(k for k in l2))