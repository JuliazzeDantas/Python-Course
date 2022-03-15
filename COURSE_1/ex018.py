'''Exercise: Write a program to read an angle and to print its sine, cosine an tangent'''

import math

angle = float(input("Enter the angle: "))
if(angle < 0):
    angle = angle + 360
if(angle > 360):
    angle = angle - 360
print("Its sine is {:.2f}".format(math.sin(math.radians(angle))))
print("Its cosine is {:.2f}".format(math.cos(math.radians(angle))))
print("Its tangent is {:.2f}".format(math.tan(math.radians(angle))))