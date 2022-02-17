a = [1,2,3]

b = {
	1: [4,5,6],
	2: [7,8],
	3: [9, 10],
	4: [11, 12, 13],
	9: [14, 15],
	10: [16],
	13: [19, 20],
	19: [21],
    26: [111]
}
#Output: [1, 4, 11, 12, 13, 19, 21, 20, 5, 6, 2, 7, 8, 3, 9, 14, 15, 10, 16]
l=[]
# for i in a:
#    l.append(i)
#    c=b[i]
#    for x in c:
#       if x not in l:
#          l.append(x)
#          if x in b.keys():
#             d=b[x]
#             for y in d:
#                if y not in l:
#                   l.append(y)
#                   if y in b.keys():
#                      e = b[y]
#                      for f in e:
#                         l.append(f)
# print(l)

def solution1(i,a,b):
   if i not in l:
      l.append(i)
   c = b[i]
   for x in c:
      if x not in l:
         l.append(x)
      if x in b.keys():
         print(solution1(x,a,b))
   return l


for i in a:
   (solution1(i,a,b))

print(l)