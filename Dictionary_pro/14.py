'''
Write a Python program to sort a given dictionary by key.
'''
dic={
        "a":"abc",
        "b":"abc",
        "d":"abc",
        "c": "abc",
}
for k,v in sorted(dic.items()):
        print(k,v)


