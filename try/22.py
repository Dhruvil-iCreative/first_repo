'''
Write a Python program to compute the sum of the ASCII values of the upper-case characters in a
 given string. Go to the editor
Input:
PytHon ExerciSEs
Output:
373
Input:
JavaScript
Output:
1572
'''
s=input("Enter String:")
if " " in s:
    s.replace(" ","")
sum=0
for i in s:
    if ord(i)<97:
        sum=sum+ord(i)
print(sum)

