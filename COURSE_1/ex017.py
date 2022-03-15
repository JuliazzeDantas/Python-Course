'''Exercise: Write a program to read the two sides of a right triangle and to print the value of the hypotenuse'''

import math


side1 = float(input("Enter the first side of the triangle: "))
side2 = float(input("Enter the second side of the triangle: "))

hypotenuse = math.sqrt(math.pow(side1,2) + math.pow(side2, 2))
# hypotenuse = math.hypot(side1, side2)
print("The hypotenuse is {}".format(hypotenuse))
