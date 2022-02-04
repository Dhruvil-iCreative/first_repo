nl=int(input("Enter Number of inner list:"))
main_l=[]
for o in range(nl):
    s=input("Enter List:")
    l=s.split(",")
    main_l.append(l)

n=int(input("Enter Number:"))
str=str(n)
print(main_l)
l2=[]
for i in main_l:
    if (str in i):

        d=(main_l.index(i))
        r=(i.index(str))
        l1=[]
        l1.append(d)
        l1.append(r)
    l2.append(l1)
print(l2)



