'''
Please write a program to generate all sentences where the subject is in ["I", "You"] and
verb is in ["Play", "Love"] and the object is in ["volleyball","cricket"]
'''
sub=["I", "You"]
verb=["Play", "Love"]
ob=['cricket','tennis']
for i in sub:
    for j in verb:
        for k in ob:
            print(i,j,k)
