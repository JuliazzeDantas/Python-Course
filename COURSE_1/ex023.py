'''Exercise: Write a program that reads a number between 0 and 9999 and displays each digit separately'''

import math

#Mode 1

number = float(input("Enter some number between 0 and 9999: "))

thousand = math.floor(number/1000)
hundred = math.floor((number - (thousand * 1000))/100)
ten = math.floor((number - (thousand * 1000) - (hundred * 100)) / 10)
unit = int(number - (thousand * 1000) - (hundred * 100) - (ten * 10))

print("thousand: {}  \n"
      "hundred: {}  \n"
      "ten: {} \n"
      "unit: {}".format(thousand, hundred, ten, unit))