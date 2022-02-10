'''
Write a Python program to rescale and shift numbers of a given list, so that they cover the range [0, 1].
Go to the editor
Input:
[18.5, 17.0, 18.0, 19.0, 18.0]
Output:
[0.75, 0.0, 0.5, 1.0, 0.5]
Input:
[13.0, 17.0, 17.0, 15.5, 2.94]
Output:
[0.7155049786628734, 1.0, 1.0, 0.8933143669985776, 0.0]
'''
l=[18.5, 17.0, 18.0, 19.0, 18.0]
mx=max(l)
mn=min(l)

for i in range(len(l)):
    l[i]=((l[i]-mn)/(mx-mn))

print(l)