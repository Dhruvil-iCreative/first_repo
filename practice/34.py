
l=[{"a":"abc","b":"abc","c":"abc"},{1:123,2:123,3:123},{1:123,2:123,3:123}]
def Merge(dict1, dict2, dict3):
    res = {**dict1, **dict2, **dict3}
    return res
dict1 = l[0]
dict2 = l[1]
dict3=l[2]
dict4 = Merge(dict1, dict2, dict3)
print(dict4)
