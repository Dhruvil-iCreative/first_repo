'''
Write a program that computes the net amount of a bank account based a transaction log
from console input. The transaction log format is shown as following:
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
D means deposit while W means withdrawal.
Then, the output should be:
500
'''

sum=0
for i in range(5):
    tra=input("Enter transaction")
    if tra[0]=='d':
        s=int(tra[1:])
        sum=sum-s
    elif tra[0]=='c':
        s=int(tra[1:])
        sum=sum+s
    else:
        continue
print(sum)

