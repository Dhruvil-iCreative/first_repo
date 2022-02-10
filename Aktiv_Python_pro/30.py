'''
Write a program to generate below Pattern:
*
* *
* * *
* * * *
* * * * *
* * * * * *
'''

for i in range(1,7):
    str = "*"*i
    print(str.ljust(40))