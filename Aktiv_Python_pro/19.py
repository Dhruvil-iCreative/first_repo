'''
Please write a program to print the list after removing delete even numbers in
[5,6,77,45,22,12,24].
'''
l=[5,6,77,45,22,12,24]
for i in l:
    if i%2==0:
        l.remove(i)
print(l)