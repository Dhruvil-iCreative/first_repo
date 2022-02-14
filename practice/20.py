s=input("Enter string:")
def f3(func):
    if s[0]=="a":
        return func
    else:
        return func
        
def f1(fun):
    if s.isalpha():
        return fun
    else:
        print("enter correct input")
        return fun
@f3
@f1
def f2():
    if s.islower():
        print(s)
    
f2()