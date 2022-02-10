

n=(input("Enter numbers:"))
l=n.split(",")
print(l)
l1=[]
def check(l):
    for k in l:
        if (len(k)<=4):
            if(int(k[0])%2==1 and int(k[3])%2==0):
                if(int(k)%3==0 or int(k)%7==0):
                    l1.append(k)
        else:
            print("Enter valid number")
check(l)
print(l1)