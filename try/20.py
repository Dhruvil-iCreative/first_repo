n=input("Enter List:")
l=n.split(",")
l1=[]
for i in range(len(l)-1):
    if (l[i] != l[i+1]):
        if(l[i+1]>l[i]):
            ans="Increasing"
            l1.append(ans)
        else:
            ans1="Decreasing"
            l1.append(ans1)
    else:
        ans2="Non monotonic"
        l1.append(ans2)

if l1.count("Increasing")==(len(l1)):
    print("Increasing")
elif l1.count("Decreasing")==(len(l1)):
    print("Decreasing")
else:
    print("Non monotonic")