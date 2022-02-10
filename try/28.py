'''
Write a Python program to select a string from a given list of strings with the most unique characters.
 Go to the editor
Input:
['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
Output:
abcdefhijklmnop
Input:
['Green', 'Red', 'Orange', 'Yellow', '', 'White']
Output:
Orange
'''
l=['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']

l2=[]

for s in l:
    count=0
    l1 = []
    for i in range(len(s)):
        if s[i] not in l1:
            l1.append(s[i])
            count=count+1
    l2.append(count)
for j in range(len(l2)):
    if l2[j]==max(l2):
        print(l[j])
