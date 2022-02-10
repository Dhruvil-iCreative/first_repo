'''
Write a Python program to find the list of strings that has fewer total characters (including repetitions).
 Go to the editor
Input:
[['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]
Output:
['this', 'list', 'is', 'narrow']
Input:
[['Red', 'Black', 'Pink'], ['Green', 'Red', 'White']]
Output:
['Red', 'Black', 'Pink']
'''
l=[['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]
for i in l:
    count=0
    l1=[]
    for j in i:
        k=len(j)
        count=count+k
    l1.append(count)
for n in range(len(l1)):
    if l1[n]==max(l1):
        print(l[n])