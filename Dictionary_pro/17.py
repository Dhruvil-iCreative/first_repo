'''
Write a Python program to remove duplicates from Dictionary.
'''
dic={'x': 'red', 'y': 'Yellow', 'z': 'Green','w':"red","p":"Yellow"}
l=[]
l1=[]
for k,v in dic.items():
    if v not in l:
        l.append(v)
    else:
        l1.append(k)
for k in l1:
    dic.pop(k)
print(dic)


