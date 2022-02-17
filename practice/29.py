l1=[3,6,9,11,15,27,88,20]
l2=sorted(l1,key=lambda x:x%3==0,reverse=True)
print(l2)