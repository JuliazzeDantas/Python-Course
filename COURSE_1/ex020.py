'''Exercise: Write a program to read the name of four people and to print all names in a random order'''

import random
from random import shuffle
from random import choice

name1 = input("Enter the first name: ")
name2 = input("Enter the first name: ")
name3 = input("Enter the first name: ")
name4 = input("Enter the first name: ")

list = [name1, name2, name3, name4]

for i in range(0,4): ###########My method
    randomName = random.choice(list)
    print(randomName)
    list.remove(randomName)
