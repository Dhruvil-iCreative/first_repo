str1="Winter Olympics in 2022 will take place in Beijing China"
#Type your answer here.

l1=["a","e","i","o","u","O"]
lst=list(filter(lambda x:x in l1,str1))

print(lst)