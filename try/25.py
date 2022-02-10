'''
Write a Python program to find the XOR of two given strings interpreted as binary numbers. Go to the editor
Input:
['0001', '1011']
Output:
0b1010
Input:
['100011101100001', '100101100101110']
Output:
0b110001001111
'''
l=['0001', '1011']
for n in range(len(l)-1):
    n1=int(l[n])
    n2=int(l[n+1])
    ans=n1^n2
print("0b",ans)
