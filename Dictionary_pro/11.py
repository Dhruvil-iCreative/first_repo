'''
Write a Python program to multiply all the items in a dictionary
'''
dic={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 10}
ans=1
for v in dic.values():
    ans=ans*v
print(ans)
