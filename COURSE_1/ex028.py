'''Exercise: Write a program that saves a random number between 0 and 5 and says if the user enter the correctly number'''
import random

user_number = int(input("Enter the chosen number: "))
random_number =  random.randint(0,5)

if(user_number == random_number):
    print("You choose the correctly number!")
else:
    print("You choose the wrong number! The right is number is {}".format(random_number))
