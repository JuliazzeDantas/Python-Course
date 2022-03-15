'''Exercise: Write a program to read the name of four people and to print a random name'''
import random
from random import choice

name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
name3 = input("Enter the third name: ")
name4 = input("Enter the fourth name: ")

list = [name1, name2, name3, name4]

print("The chosen was ", random.choice(list))