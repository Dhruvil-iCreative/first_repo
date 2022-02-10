'''
Write a program which are divisible by 7 and between a given range 0 and n.
'''
num=int(input("Enter range:"))
for n in range(0,num):
    if n%7==0:
        print(n)