'''
Write a Python program to find the sum of the numbers of a given list among the
 first k with more than 2 digits. Go to the editor
Input: [4, 5, 17, 9, 14, 108, -9, 12, 76]
Value of K: 4
Output:
0
Input: [4, 5, 17, 9, 14, 108, -9, 12, 76]
Value of K: 6
Output:
108
'''
l=[114, 215, -117, 119, 14, 108, -9, 12, 76]
k=int(input("Enter Number:"))
sum=0
for n in range(k):
    if l[n]>99 or l[n]<-99:
        sum=sum+l[n]
print(sum)