def f1(func):
    print("hello from f1")
    return func

def f3(fun):
    print("hello f3")
    return fun

@f3
@f1
def f2():
    print("Hello from f2")
f2()