''''Exercise: Write a program to read the dimensions of a wall (in meters), then to calculate
    its area and how many liters of paint you need to paint it.'''

'''Each liter of paint color, 2 meters of the wall'''

width = float(input("Enter the width of the wall: "))
height = float(input("Enter the height of the wall: "))

area = width * height

print("This wall has a dimension {}×{} and your area is {} m².".format(width, height, area))
print("You'll need {} liter of paint to paint it.".format(area/2))

