'''
Write a Python program to find the coordinates of a triangle with the given side lengths. Go to the editor
Input:
[3, 4, 5]
Output:
[[0.0, 0.0], [3, 0.0], [3.0, 4.0]]
Input:
[5, 6, 7]
Output:
[[0.0, 0.0], [5, 0.0], [3.8, 5.878775382679628]]
'''
def test(sides):
   a, b, c = sorted(sides)
   s = sum(sides) / 2 # semi-perimeter
   area = (s * (s - a) * (s - b) * (s - c)) ** 0.5 # Heron's formula
   y = 2 * area / a # height
   x = (c ** 2 - y ** 2) ** 0.5
   return [[0.0, 0.0], [a, 0.0], [x, y]]
sides = [5,6,7]
print("Sides of the triangle:",sides)
print("Coordinates of a triangle with the said side lengths:")
print(test(sides))