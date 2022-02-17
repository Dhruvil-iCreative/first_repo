count=0
def fun(x):
    def inner():
        global count
        count = count + 10
        while 0 < count <= 100:
            print(count)
            inner()
        while count > 100:
             break
    return inner

@fun
def num():
    return 5

num()