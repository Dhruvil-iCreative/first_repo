'''
Write a Python program to check a dictionary is empty or not
'''
import math
n=int(input("ENter number of students:"))
namel={}

d={}
for i in range(n):
    name=input("Enter student name:")
    marks=int(input("Enter student marks:"))
    d.__setitem__(name,marks)
l1=[]
#for i in range(0,2):
for k,v in d.items():
    if v==max(d.values()):
        l1.append(k)
for k in l1:
    del d[k]
d2=dict(d)
l2=[]
for k,v in d2.items():
    if v==max(d2.values()):
        l2.append(k)
for k in l2:
    del d2[k]

for k,v in d2.items():
     if v==max(d2.values()):
        namel.__setitem__(k,v)
print(sorted(namel))