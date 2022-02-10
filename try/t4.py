l=[{"Name":"Robert Downey","Designation":"Project-manager","Experience":"0","workingfor":"none"},
{"Name":"Anne Hathaway","Designation":"Project-manager","Experience":"0","workingfor":"none"},
{"Name":"Mark","Designation":["Team Leader","mentor"],"Experience":"8","workingfor":"RD"},
{"Name":"Samuel","Designation":"Team Leader","Experience":"8","workingfor":"RD"},
{"Name":"Paul","Designation":"Team Leader","Experience":"8","workingfor":"RD"},
{"Name":"Tom","Designation":["Team Leader","mentor"],"Experience":"8","workingfor":"RD"},
{"Name":"Chris","Designation":"Team Leader","Experience":"5","workingfor":"AH"},
{"Name":"Pratt","Designation":"Team Leader","Experience":"5","workingfor":"AH"},
{"Name":"Emma","Designation":"Team Leader","Experience":"5","workingfor":"AH"},
{"Name":"Will","Designation":["Team Leader","mentor"],"Experience":"5","workingfor":"AH"},
{"Name":"Smith","Designation":"Team Leader","Experience":"5","workingfor":"AH"},
{"Name":"James","Designation":["Team Leader","Junior Developer"],"Experience":"1.6","workingfor":"Tom"},
{"Name":"Jennifer","Designation":"Senior Developer","Experience":"3.8","workingfor":"James"},
{"Name":"Scott","Designation":"Senior Developer","Experience":"3.8","workingfor":"James"},
{"Name":"Sophie","Designation":"Senior Developer","Experience":"3.8","workingfor":"James"},
{"Name":"Fergal","Designation":"Senior Developer","Experience":"4.5","workingfor":"Paul"},
{"Name":"Paul","Designation":"Mentor","Experience":"0","workingfor":"none"},
{"Name":"Edge","Designation":"Senior Developer","Experience":"3","workingfor":"Will"},
{"Name":"Ryan","Designation":"Senior Developer","Experience":"3.5","workingfor":"Will"},
{"Name":"Jerry","Designation":"Junior Developer","Experience":"1.5","workingfor":"Tom"},
{"Name":"Leonardo","Designation":"Junior Developer","Experience":"1","workingfor":"Mark"},
{"Name":"Alexandra","Designation":"Junior Developer","Experience":"1","workingfor":"Mark"},
{"Name":"Walker","Designation":"Senior Developer","Experience":"2.7","workingfor":"Smith"},
{"Name":"Diana","Designation":"Senior Developer","Experience":"2.7","workingfor":"Smith"}]
print("A\n")

for i in l:
    if (i["workingfor"]=="RD"):
        print(i)
print("\nB\n")
for j in l:
    k=j["Experience"]
    if(float(k)>=4):
        print(j)
print("\nC\n")
for p in l:
    k = p["Experience"]
    if(float(k)>=3.5 and float(k)<=4.5):
        p["Experience"]="4.6"
        print(p)
print("\nD\n")
for q in l:
    if ("Team Leader" in q["Designation"]):
        if(q["Designation"]=="0"):
            q["Designation"]="N/A"
        print(q)
print("\nE\n")
for x in l:
    if(x["workingfor"]=="Smith"):
        x["workingfor"]="Ryan"
        print(x)
print("\nF\n")
for y in l:
    if(float(y["Experience"])<=2):
        print("True")
print("\nG\n")
for z in l:
    if (z["Name"]=="Edge"):
        if("Team Leader" not in z["Designation"]):
            z["Designation"]="Team Leader"
        print(z)

