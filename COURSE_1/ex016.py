'''Exercise: Write a program to read a real number from the keyboard and print the integer part.'''
import math
from math import trunc

number = float(input("Enter a real number: "))

numberFloor = math.trunc(number)

print("The integer part of the number is {}".format(numberFloor))
