'''
Write a Python program to get a dictionary from an object's fields.
'''


class dictObj(object):
    def __init__(self):
        self.x = 'red'
        self.y = 'Yellow'
        self.z = 'Green'
test = dictObj()
print(test.__dict__)
