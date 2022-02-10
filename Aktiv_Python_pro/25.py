'''
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list
after removing all duplicate values with original order reserved.
'''
l= [12,24,35,24,88,120,155,88,120,155]
l2=[]
for i in reversed(l):
    if i not in l2:
        l2.append(i)
print(l2)