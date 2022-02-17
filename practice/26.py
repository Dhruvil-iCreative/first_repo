my_chars = ['a', 'b', 'c', 'd', 'e']
my_nums = [1,2,3,4,5]
c=[1,2]

result = list(zip(my_chars, my_nums,c))
for x in zip(my_chars, my_nums,c):
    print(x)



print(result)