'''
Write a Python script to sort (ascending and descending) a dictionary by value.

import operator

d={
    "a":1,
    "b":2,
    "c":3,
    "d":10,
    "e":5
}
print(sorted(d.items(),key=lambda kv:(kv[1],kv[0])))

'''
from collections import OrderedDict

dict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
dict1 = OrderedDict (sorted(dict.items()))
dict2 =(sorted(dict.keys()))
dict3 =(sorted(dict.values()))
dict4 = (sorted(dict.items(),key=lambda kv:(kv[1],kv[0])))
dict5 = (sorted(dict.items(),key=lambda kv:(kv[1],kv[0]),reverse=True))
print(dict1)
print(dict2)
print(dict3)
print(dict4)
print(dict5)