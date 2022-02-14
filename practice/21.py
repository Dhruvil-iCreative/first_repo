# count = 0
# def fun():
#     # for i in range(5):
#     # count = 0
#     x=20
#     def f2():
#         nonlocal x
#         x=x+20
#
#     global count
#     count=count+10
#     while 0<count<100:
#         print(count)
#         fun()
#     while count > 100:
#         break
#
# fun()
#import cProfile
from line_profiler import LineProfiler


def decor1(func):
    def inner():
        x = func()
        return x * x

    return inner

def decor(func):
    def inner():
        x = func()
        return 2 * x

    return inner

def decor2(func):
    def inner():
        x = func()
        return x + 5

    return inner

@decor2
@decor1
@decor
def num():
    return 10
print(num())
#cProfile.run("num()")
pro=LineProfiler(num)
pro.print_stats()