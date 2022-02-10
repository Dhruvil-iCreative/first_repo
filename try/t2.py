s=(input("Enter list:"))
l=s.split(",")
k=['a','e','i','o','u']
p=['A','E','I','O','U']
l1=[]
l2=[]
#1
def check(l):
    for i in l:
        if i.isalpha():
            if (i.istitle() & (i[0] not in k) & (i[0] not in p)):
                l1.append(i)
            else:
                l2.append(i)
        else:
            print("Enter alphabets only!! for ->",format(i))
check(l)
print(l1)
