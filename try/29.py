'''
Write a Python program to find the indices of two numbers that sum to 0 in a given list of numbers.
 Go to the editor
Input:
[1, -4, 6, 7, 4]
Output:
[4, 1]
Input:
[1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]
Output:
[1, 7]
'''
l=[1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]
l1=[]
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]+l[j]==0:
            if i not in l1 and j not in l1:
                l1.append(i)
                l1.append(j)
print(l1)