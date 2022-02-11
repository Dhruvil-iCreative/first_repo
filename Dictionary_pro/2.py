'''
Write a Python script to add a key to a dictionary. Go to the editor

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
'''
sd={0: 10, 1: 20}
sd.__setitem__(2,60)
sd.update({3:80})
print(sd)