'''
Write a Python program to map two lists into a dictionary
'''
l1=["a","b","c","d"]
l2=[1,2,3,4]
d={}
if len(l1)==len(l2):
    for i in range(len(l1)):
        d.__setitem__(l1[i],l2[i])
else:
    print("Wrong input")
print(d)
'''
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)
'''

