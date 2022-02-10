'''
Write a Python program to check, for each string in a given list, whether the last character is an isolated letter or not. Return True or False. Go to the editor
Input:
['cat', 'car', 'fear', 'center']
Output:
[False, False, False, False]
Input:
['ca t', 'car', 'fea r', 'cente r']
Output:
[True, False, True, True]
'''

s=input("Enter values:")
l=s.split(",")
l1=[]
for i in l:
    if i[-2]==" ":
        ans="True"
        l1.append(ans)
    else:
        ans="False"
        l1.append(ans)
print(l1)
