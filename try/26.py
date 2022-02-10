'''
Write a Python program to find the largest number where commas or periods are decimal points. Go to the editor
Input:
['100', '102,1', '101.1']
Output:
102.1
'''
l2=[]
l=['100', '102,1', '101.1']
for i in l:
    if ("," in i):
        j=i.replace(",",".")
        l2.append(float(j))
print(max(l2))
