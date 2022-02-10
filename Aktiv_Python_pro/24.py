'''
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to
make a list whose elements are intersection of the above given lists.
'''
l1=[1,3,6,78,35,55]
l2=[12,24,35,24,88,120,155]
l3=[]
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)