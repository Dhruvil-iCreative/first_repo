s="( ()) ((()()())) (()) ()"
l=s.split(" ")
print(l)

for i in range(len(l)):
    if(l[i].count("(")!=l[i].count(")")):
       
       l[i + 1] = l[i] + l[i + 1]
print(l)


