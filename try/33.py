'''
Write a Python program to find the positions of all uppercase vowels (not counting Y) in even
 indices of a given string. Go to the editor
Input: w3rEsOUrcE
Output:
[6]
Input: AEIOUYW
Output:
[0, 2, 4]
'''
s=input("Enter string:")
l1=[]
for i in range(0,len(s),2):
    if 65<ord(s[i])<90:
        if s[i] in ["A","E","I","O","U"]:
            l1.append(i)
print(l1)