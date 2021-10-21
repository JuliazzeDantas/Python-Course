'''Exercise: Write a program to read a number and print its double, triple, and square root.'''

import math

number = int(input("Enter any integer number: "))

print("Double: ", number*2)
print("Triple: ", number*3)
print("Square Root: ", math.sqrt(number)) #I can use math.sqrt(number) or pow(number,1/2)