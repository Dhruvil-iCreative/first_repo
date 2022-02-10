'''
Write a program which can compute the factorial of a given numbers.The results should
be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''
def fact(i):
    if i==1:
        return i
    else:
        i=i*fact(i-1)
        return i
print(fact(8))