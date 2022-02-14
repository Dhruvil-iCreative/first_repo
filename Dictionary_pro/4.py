'''
Write a Python script to check whether a given key already exists in a dictionary.
'''
dic={
        "a":"abc",
        "b":"abc",
        "c":"abc",
        "d":"abc"
}
def check(dic):
    for k in dic:
        if k=="j":
            return True

print(check(dic))



