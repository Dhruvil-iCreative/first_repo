emp = {
        "pro-man": {
                'rd': {
                        'tl': {'mark': {'exp': 8}, 'samual': {'exp': 8}, 'paul': {'exp': 8}, 'tom': {'exp': 8}
                                },
                        },
                'ah': {
                        'tl': {"chris": {'exp': 5}, 'pratt': {'exp': 5}, 'emma': {'exp': 5}, 'will': {'exp': 5},
                               'smith': {'exp': 5}
                               },
                        }
                 },
        "manager": {
                'chris': {
                        'sen-dev': {'jenifer': {'exp': 3.5}, 'scott': {'exp': 3.5}, 'sophie': {'exp': 3.5}},
                },
                'will': {
                        'sen-dev': {'edge': {'exp': 3}, 'ryan': {'exp': 3.5}},
                }
        },
        "reporting manager": {
                'smith': {
                        'sen-dev': {'walker': {'exp': 2.7}, 'diana': {'exp': 2.7}},
                }
        },
        "mentor": {
                'mark': {
                        'jun-dev': {'leonardo': {'exp': 1}, 'alexandera': {'exp': 1}},
                },
                'tom': {
                        'jun-dev': {'jerry': {'exp': 1.5}, 'james': {'exp': 1.6}},

                },
                'paul': {
                        'sen-dev': {'fergal': {'exp': 4.5}},
                }
        }
}

#1

for i in emp["pro-man"].values():
        print(i.values())
print("\nB\n")
'''
l=[]
for p in emp.values():
        for q in p.values():
                for r in q.values():
                        for x in r.values():
                                for y in x.values():
                                        if (y>4):
                                                for name in (r.keys()):
                                                        if name not in l:
                                                                l.append(name)
print(l)
'''
def second(i):
        for k, v in i.items():
                if type(v) == dict:
                        second(v)
                        if k == "tl" or k == "sen-dev" or k == "jun-dev":
                                for k1, v1 in v.items():
                                        if v1["exp"] > 4:
                                                print(k1, v1)
second(emp)

print("\nC\n")
def third(i):
        for k,v in i.items():
                if type(v)==dict:
                        third(v)
                        if k=="tl" or k=="sen-dev" or k=="jun-dev":
                                for k1,v1 in v.items():
                                        if v1["exp"]>3 or v1["exp"]<4.5:
                                                v1["exp"]=4.6
                                                print(k1,v1)
third(emp)

print("\n D\n")
def fourth(i):
        for k,v in i.items():
                if type(v)==dict:
                        fourth(v)
                        if k=="tl":
                                for k1,v1 in v.items():
                                        if v1["exp"]==0:
                                                v1["exp"]="N/A"
                                        print(k1,v1)
fourth(emp)
print("\n E \n")
k1="Ryan"
for k,v in zip(emp["reporting manager"].keys(),emp["reporting manager"].values()):
        emp["reporting manager"].clear()
        emp["reporting manager"].__setitem__(k1,v)
print(emp["reporting manager"])

print("\nF\n")
def sixth(i):
        for p in i.values():
                if type(p)==int or type(p)==float:
                       if p<2:
                               print("True")
                else:
                        sixth(p)
sixth(emp)

print("\nG\n")
for p in emp["pro-man"].values():
        if "edge" not in p.values():
                emp["pro-man"]["rd"]["tl"].__setitem__("edge",{'exp':3})
print(emp["pro-man"])