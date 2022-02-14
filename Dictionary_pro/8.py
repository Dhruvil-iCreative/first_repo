'''
Write a Python script to merge two Python dictionaries.
'''
dic1={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
dic2={"a":"abc",
        "b":"abc",
        "c":"abc",
        "d":"abc"
      }
dic=(dic1,dic2)
d={}
for di in dic:
    d.update(di)
print(d)