'''
Write a Python program to compute the product of the odd digits in a given number,
or 0 if there aren't any. Go to the editor
Input: 123456789
Output:
945
Input: 2468
Output:
0
Input: 13579
Output:
945
'''
i=input("Enter number:")
prod=1
for n in range(len(i)):
    if (int(i[n])%2)==1:
        prod=prod*int(i[n])

print(prod)