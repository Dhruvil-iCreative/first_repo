'''
Write a program that accepts a sentence and calculate the number of uppercase letters
and lowercase letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''
str=input("Enter the sentence:")
count=0
count1=0
for s in str:
    if s.isupper():
        count=count+1
    elif s.islower():
        count1=count1+1
    else:
        print("Wrong input")
print("Capitals:",count)
print("Smalls:",count1)