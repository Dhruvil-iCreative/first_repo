'''
By using list comprehension, please write a program to print the list after removing the
0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
'''
l=[12,24,35,70,88,120,155]
l1=[l[i] for i in range(len(l)) if i not in range(0,7,2)]
print(l1)