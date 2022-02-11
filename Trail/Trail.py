# '''
#
# '''
# l=[i for i in range(0,999,10)]
# print(l)
lists=[]
list_length=int(input("enter the number of elements you want to enter in a list"))
for i in range (list_length):
    lists.append(int(input("enter number:")))
x=int(input("enter the first i numbers:"))

bools=sum(lists[:x])==x
print(lists)
print(bools)
