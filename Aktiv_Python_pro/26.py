'''
Use a list comprehension to square each odd number in a list. The list is input by a
sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
'''
s=input("Enter string for list:")
l=s.split(",")
l1=[int(i)*int(i) for i in l if int(i)%2==1]
print(l1)